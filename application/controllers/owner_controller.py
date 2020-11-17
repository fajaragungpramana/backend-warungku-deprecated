import random

from http.client import HTTPException
from flask_mail import Message
from flask import render_template

from application.models.owner_model import OwnerModel
from application.models.verification_model import VerificationModel
from application.utils import is_none, response_util, security_util
from application import db, mail


# This is function to do owner registration
def register(owner: OwnerModel):
    if is_none(owner.full_name) or is_none(owner.store[0].name) or is_none(owner.email) or is_none(owner.password):
        return response_util.http_bad_request('Fill all the request body!')
    else:
        owner_query = OwnerModel.query.filter_by(email=owner.email).first()
        if owner_query:
            return response_util.http_not_acceptable('Owner with a same email is already exist!')
        else:
            owner.verification = [(
                VerificationModel(
                    owner_id=owner.id,
                    name=owner.full_name,
                    account='OWNER'
                )
            )]

            try:
                db.session.add(owner)
                db.session.add(owner.store[0])
                db.session.add(owner.verification[0])
                db.session.commit()
            except HTTPException:
                return response_util.http_internal_server_error()

        return response_util.http_created('Owner account has been created!', {
            'id': owner.id
        })


# This function to do owner login
def login(owner: OwnerModel):
    if is_none(owner.email) or is_none(owner.password):
        return response_util.http_bad_request('Fill all the request body!')
    else:
        owner_query = OwnerModel.query.filter_by(email=owner.email).first()
        if not owner_query:
            return response_util.http_not_acceptable('Account is not registered!')
        else:
            if not security_util.verify_password(owner_query.password, owner.password):
                return response_util.http_unauthorized('Wrong password account!')
            else:
                return response_util.http_ok('Owner login success!', {
                    'id': owner_query.id
                })


# This function to sent a code verification through email
def verification_code(account_id: str, account_email: str):
    if is_none(account_id) or is_none(account_email):
        return response_util.http_bad_request('Fill all the request body!')
    else:
        verification_query = VerificationModel.query.filter_by(owner_id=account_id).first()
        if not verification_query:
            return response_util.http_not_acceptable('account id not found!')
        else:
            generated_code = random.randint(000000, 999999)
            verification_query.code = generated_code

            try:
                db.session.commit()

                mail_message = Message(
                    subject='Verification Code',
                    html=render_template(
                        'mail_template.html',
                        full_name=verification_query.name,
                        code=generated_code
                    ),
                    sender=('WarungKu', 'warungku.implizstudio@gmail.com'),
                    recipients=[account_email]
                )
                mail.send(mail_message)

            except HTTPException:
                return response_util.http_internal_server_error()

            token = security_util.access_token(account_id)

            return response_util.http_ok('Code verification has been sent!', {
                'token': 'Bearer {}'.format(token),
                'expired': '1 Minutes'
            })

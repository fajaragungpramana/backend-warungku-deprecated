import random

from http.client import HTTPException
from flask_mail import Message
from flask import render_template

from application import db, mail, VerificationModel
from application.utils import is_none, response_util, security_util

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
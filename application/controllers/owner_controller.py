from http.client import HTTPException

from application.utils import is_none, response_util, security_util, date_now
from application import db, OwnerModel, VerificationModel


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
            return response_util.http_not_found('Account is not registered!')
        else:
            if not security_util.verify_password(owner_query.password, owner.password):
                return response_util.http_not_acceptable('Wrong password account!')
            else:
                verification_query = VerificationModel.query.filter(
                    (VerificationModel.owner_id == owner_query.id) or VerificationModel.email
                ).first()
                data = {'id': owner_query.id}
                if not verification_query:
                    return response_util.http_accepted('Owner login success, but account is not verified!', data)
                else:
                    return response_util.http_ok('Owner login success!', data)


# This method serve trade report result
def report_result(account_id: str, report_date: str = date_now('%d-%m-%Y')):
    if is_none(account_id):
        return response_util.http_bad_request('Fill all the request body!')
    else:
        return response_util.http_ok("Owner trade result!", {
            'date': report_date,
            'income': 10_454_000,
            'net_income': 1_609_916,
            'percentage': '+15.4%'
        })
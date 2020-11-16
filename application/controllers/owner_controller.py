from http.client import HTTPException

from application.models.owner_model import OwnerModel
from application.utils import is_none, response_util
from application import db

# This is function to do owner registration
def register(owner: OwnerModel):
    if is_none(owner.full_name) or is_none(owner.email) or is_none(owner.password):
        return response_util.http_bad_request('Fill all the request body!')
    else:
        owner_query = OwnerModel.query.filter_by(email=owner.email).first()
        if owner_query:
            return response_util.http_not_acceptable('Owner with a same email is already exist!')
        else:
            try:
                db.session.add(owner)
                db.session.add(owner.store[0])
                db.session.commit()
            except HTTPException:
                return response_util.http_internal_server_error()

        return response_util.http_created('Owner account has been created!')
from flask import request
from flask_jwt_extended import jwt_required

from application import app, OwnerModel, StoreModel, ProductModel, ProductImageModel
from application.controllers import owner_controller, verification_controller, tip_controller, product_controller
from application.utils import get_post, get_param, security_util, get_unique_id


# Route owner registration
@app.route('/warungku/owner/auth/register', methods=['POST'])
@security_util.access_key_owner
def owner_register():
    generated_id = get_unique_id()

    owner = OwnerModel(
        id=generated_id,
        full_name=get_post('full_name'),
        store=[StoreModel(
            owner_id=generated_id, name=get_post('store_name')
        )],
        email=get_post('email'),
        password=security_util.hash_password(get_post('password'))
    )
    return owner_controller.register(owner)


# Route owner login
@app.route('/warungku/owner/auth/login', methods=['POST'])
@security_util.access_key_owner
def owner_login():
    return owner_controller.login(
        OwnerModel(email=get_post('email'), password=get_post('password'))
    )


# Route owner verification code
@app.route('/warungku/owner/auth/code', methods=['GET'])
@security_util.access_key_owner
def owner_verification_code():
    return verification_controller.verification_code(
        get_param('account_id'), get_param('account_email')
    )


# Route account verification
@app.route('/warungku/owner/auth/verification', methods=['POST'])
@security_util.access_key_owner
@jwt_required
def owner_verification_email():
    return verification_controller.verification_account(
        get_post('account_id'), get_post('account_code')
    )


# Route account report result
@app.route('/warungku/owner/report/today', methods=['GET'])
@security_util.access_key_owner
def owner_report_result():
    return owner_controller.report_result(get_param('account_id'))


# Route tip
@app.route('/warungku/tip', methods=['GET'])
def warungku_tip():
    return tip_controller.tip_data(get_param('category'))


# Route add product
@app.route('/warungku/owner/<account_id>/new/product', methods=['POST'])
@security_util.access_key_owner
def new_product(account_id):
    return product_controller.new_product(
        ProductModel(
            id=get_unique_id(),
            owner_id=account_id,
            name=get_post('name'),
            weight=get_post('weight'),
            weight_unit=get_post('weight_unit'),
            available=get_post('available'),
            available_unit=get_post('available_unit'),
            minimal_order=get_post('minimal_order'),
            purchase_price=get_post('purchase_price'),
            sell_price=get_post('sell_price'),
            description=get_post('description'),
            barcode=get_post('barcode'),
            category=get_post('category'),
            expired=get_post('expired'),
        ), request.files.getlist('images')
    )


if __name__ == '__main__':
    app.run()

from application import app, OwnerModel, StoreModel
from application.controllers import owner_controller, global_controller
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
    return global_controller.verification_code(
        get_param('account_id'), get_param('account_email')
    )


if __name__ == '__main__':
    app.run()

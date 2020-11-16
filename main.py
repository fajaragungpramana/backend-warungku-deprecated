from application import app, OwnerModel, StoreModel
from application.controllers import owner_controller
from application.utils import get_post, security_util, get_unique_id


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


if __name__ == '__main__':
    app.run()

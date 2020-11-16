from application import app
from application.controllers import owner_controller
from application.models.owner_model import OwnerModel
from application.utils import get_post, security_util

# Route owner registration
@app.route('/warungku/owner/auth/register', methods=['POST'])
@security_util.access_key_owner
def owner_register():
    owner = OwnerModel(
        full_name=get_post('full_name'),
        email=get_post('email'),
        password=security_util.hash_password(get_post('password'))
    )
    return owner_controller.register(owner)


if __name__ == '__main__':
    app.run()
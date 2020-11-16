from application import app
from application.controllers import owner_controller
from application.models.owner_model import OwnerModel
from application.utils.security_util import access_key_owner
from application.utils import get_post
from application.utils import security_util

@app.route('/warungku/owner/auth/register', methods=['POST'])
@access_key_owner
async def owner_register():
    owner = OwnerModel(
        full_name=get_post('full_name'),
        email=get_post('email'),
        password=security_util.hash_password(get_post('password'))
    )
    return await owner_controller.register(owner)


if __name__ == '__main__':
    app.run()
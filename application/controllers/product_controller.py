import os
from http.client import HTTPException

from application import app, db, ProductImageModel, ProductModel
from application.utils import get_unique_id, is_none, response_util


def new_product(product: ProductModel, images):
    if is_none(product.name) or is_none(product.weight) or \
            is_none(product.weight_unit) or is_none(product.available) or \
            is_none(product.available_unit) or is_none(product.minimal_order) or \
            is_none(product.minimal_order) or is_none(product.purchase_price) or \
            is_none(product.sell_price) or is_none(product.description) or \
            is_none(product.barcode) or is_none(product.category) or \
            is_none(product.expired) or is_none(images):
        return response_util.http_bad_request('Fill all the request body!')
    else:
        path = app.config['UPLOAD_FOLDER'] = '../backend-warungku/application/static/product'

        for image in images:
            image.filename = get_unique_id() + '.jpg'
            image.save(os.path.join(path, image.filename))

            separate_path = path.replace('../backend-warungku/application/', '')
            url = 'http://127.0.0.1:5000/{}/{}'.format(separate_path, image.filename)

            db.session.add(ProductImageModel(
                product_id=product.id,
                image=url
            ))

        db.session.add(product)

        try:
            db.session.commit()
        except HTTPException:
            return response_util.http_internal_server_error()

        return response_util.http_ok('New product has been successfully added!')

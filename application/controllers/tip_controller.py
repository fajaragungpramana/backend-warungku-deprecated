from application.utils import is_none, response_util
from application import TipModel

def tip_data(category: str):
    if is_none(category):
        return response_util.http_bad_request('Fill all the request body!')
    else:
        query_tip = TipModel.query.filter_by(category=category).limit(10).all()
        if not query_tip:
            return response_util.http_not_found('No tip found!')
        else:
            data = []
            for tip in query_tip:
                data.append({
                    'image': tip.image,
                    'title': tip.title,
                    'body': tip.body,
                    'create_at': tip.create_at
                })
            return response_util.http_ok("This is tips for {}".format(category), data)
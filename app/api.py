from flask import jsonify

from app import app, get_conn


# @app.route('/api/all')
# def get_all():
#     conn = get_conn()
#     count = conn.get_nums
#     datas = conn.get_all()
#     all = []
#
#     return jsonify({
#         'paper': conn.get_all(),
#         'count': count
#     })


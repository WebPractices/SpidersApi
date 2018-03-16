from flask import Flask, g, render_template

from db import MongodbClient


app = Flask(__name__)

def get_conn():
    """
    链接Mongodb
    """
    if not hasattr(g, 'mongodb_conn'):
        g.mongodb_conn = MongodbClient()
    return g.mongodb_conn

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

from . import views, api

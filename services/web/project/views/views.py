from flask import Blueprint, render_template, request, redirect, flash, jsonify
from flask_login import login_required, current_user
from flask import url_for, send_from_directory

from .. import db, app

import json

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def login_test():
    #return 'user: ' + current_user.nickname
    return redirect(url_for('chats.contacts'))



@views.route('/')
def test():
    return 'test'


@views.route("/static/<path:filename>", methods=['GET'])
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)

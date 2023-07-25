from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from .. import db

import json

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def login_test():
    return 'user: ' + current_user.nickname



@views.route('/')
def test():
    return 'test'
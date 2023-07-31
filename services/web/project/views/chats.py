from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from ..models import Users, Contacts
from .. import db

import json


chats = Blueprint('chats', __name__)



@chats.route('/chats')
@login_required
def home():
    return render_template("chats.html", user=current_user)


@chats.route('/contacts')
@login_required
def contacts():
    return render_template("contacts.html", user=current_user)
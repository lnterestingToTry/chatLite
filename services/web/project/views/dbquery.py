from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from ..models import Users, Contacts, Notifications
from .. import db




dbquery = Blueprint('dbquery', __name__)



@dbquery.route('/get_contacts', methods=['GET'])
@login_required
def get_contacts():
    current_user_id = current_user.get_id()
    
    contacts = Contacts.query.get(initiator_id=current_user_id)
    return jsonify(contacts)


@dbquery.route('/get_users', methods=['GET'])
@login_required
def get_users():    
    users = Users.query.all()
    contacts_data = []
    
    current_user_id = current_user.get_id()
    
    for user in users:
        
        contact_info = {
            'id': user.id,
            'username': user.nickname,
            'email': user.email
        }
        
        if Contacts.query.filter_by(initiator_id=current_user_id, invitee_id=user.id).first():
            contact_info['in_contacts'] = 'true'
        else:
            contact_info['in_contacts'] = 'false'
        

        contacts_data.append(contact_info)
        
    #contacts_data = [{'id': user.id, 'username': user.nickname, 'email': user.email} for user in contacts]
    return jsonify(contacts_data)


@dbquery.route('/adding_contact', methods=['POST'])
@login_required
def adding_contact():
    data = request.get_json()
    invitee_id = data.get('user_id')
    
    current_user_id = current_user.get_id()
    
    if invitee_id == current_user_id:
        flash('помилка додавання (не можна додати себе в свої ж контакти)', category='error')
    else:
        new_contact = Contacts(initiator_id=current_user_id, invitee_id=invitee_id)
        db.session.add(new_contact)
        db.session.commit()
        flash('контакт додано', category='success')
    
    return jsonify({})


@dbquery.route('/user_bynickname_search', methods=['POST'])
@login_required
def user_bynickname_search():
    data = request.get_json()
    string = data.get('input_value')
    
    users = Users.query.filter(Users.nickname.like(f'%{string}%')).all()

    if users:
        users_data = []
        for user in users:
            
            user_info = {
            'id': user.id,
            'username': user.nickname,
            'email': user.email
            }

            users_data.append(user_info)
        return jsonify(users_data)
        
    return jsonify({})



@dbquery.route('/is_notification', methods=['GET'])
def is_notification():
    current_user_id = current_user.get_id()
    
    notifications = Notifications.query.filter_by(user_id=current_user_id, checked=False).first()
    is_notification = None
        
    if notifications:
        is_notification = 'true'
    else:
        is_notification = 'false'
        
    answer = [{'is_notification': is_notification}]
    
    return jsonify(answer)
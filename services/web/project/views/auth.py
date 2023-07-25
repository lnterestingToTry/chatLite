from flask import Blueprint, render_template, request, flash, redirect
from flask import url_for
from ..models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import login_user, login_required, logout_user, current_user


from . import (email_maxlength, email_minlength, 
nickname_maxlength, nickname_minlength,
password_maxlength, password_minlength)

auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    email = ''
    password = ''
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('харош харош', category='success')
                login_user(user, remember=True)
                
                return redirect(url_for('chats.home'))
            else:
                flash('невірний пароль, спробуйте ще раз', category='error')
        else:
            flash('користувача з такою @поштою не існує', category='error')
    
    form_data = {'email': email, 'password': password}
    
    
    return render_template("login.html", user=current_user, form_data=form_data)



@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    email = ''
    nickname = ''
    password1 = ''
    password2 = ''
    
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Users.query.filter_by(email=email).first()

        if user:
            flash('на даний емейл вже існує зареєстрований користувач', category='error')
        elif len(email) < email_minlength:
            flash('емейл не може бути коротшим ' + str(email_minlength) + ' символів', category='error')
        elif len(email) > email_maxlength:
            flash('емейл не може бути довшим ' + str(email_maxlength) + ' символів', category='error')
        
        elif len(nickname) < nickname_minlength:
            flash('псевдонім не може бути коротшим ' + str(nickname_minlength) + ' символів', category='error')
        elif len(nickname) > nickname_maxlength:
            flash('псевдонім не може бути довшим ' + str(nickname_maxlength) + ' символів', category='error')
        
        elif password1 != password2:
            flash('паролі не співпадають', category='error')
        elif len(password1) < password_minlength:
            flash('пароль не може бути коротшим ' + str(password_minlength) + ' символів', category='error')
        elif len(password1) > password_maxlength:
            flash('пароль не може бути довшим ' + str(password_maxlength) + ' символів', category='error')
        
        else:
            new_user = Users(email=email, nickname=nickname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            
            flash('профіль створено', category='success')
            
            return redirect(url_for('auth.login'))
    
    form_data = {'email': email, 'nickname': nickname,
                 'password1': password1, 'password2': password2}
    
    return render_template("sign_up.html", user=current_user, form_data=form_data)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
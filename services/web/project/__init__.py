from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


login_mananger = LoginManager()
login_mananger.login_view = 'auth.login'
login_mananger.init_app(app)


from .models import Users

@login_mananger.user_loader
def load_user(id):
    return Users.query.get(int(id))


from .views.views import views
from .views.auth import auth
from .views.chats import chats
from .views.dbquery import dbquery


app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(chats, url_prefix='/')
app.register_blueprint(dbquery, url_prefix='/')

from .models import Contacts, Notifications, usersMessages

models = [Users, Contacts, Notifications, usersMessages]
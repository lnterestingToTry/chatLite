from flask import Flask
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


app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(chats, url_prefix='/')
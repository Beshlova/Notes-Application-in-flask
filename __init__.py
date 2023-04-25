from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import os

#Initializes the login manager variable
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"

#Initializes the db variable
db = SQLAlchemy()

#Initializes the migrate variable
migrate = Migrate()

#Initializes the bcrypt variable
bcrypt = Bcrypt()

#Initializes the mail variable
mail = Mail()

#Sets the name of the db file
DB_NAME = 'database.db'

#The application factory
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['MAIL_SERVER'] = 'imap-mail.outlook.com'
    app.config['MAIL_PORT'] = 993
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')



    from .views import views
    from .auth import auth
    
    

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    mail.init_app(app)

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app





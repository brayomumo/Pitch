from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import  UploadSet, configure_uploads,IMAGES
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'Strong'
login_manager.login_view = 'auth,login'
db = SQLAlchemy()
bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)
mail = Mail()

#create application function 
def create_app(config_name):
    #init app
    app = Flask(__name__)

    #configurations 
    app.config.from_objec(config_options[config_name])


    #config uploads

    i#nitialize flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)







    return app

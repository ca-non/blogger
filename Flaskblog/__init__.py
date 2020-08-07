from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from Flaskblog.config import Config



# extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'  # set the login route
login_manager.login_message_category = 'info' # for flash msg 
mail = Mail()




# extension doesn't go here
def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	# registering routes from blueprints
	from Flaskblog.users.routes import users
	from Flaskblog.posts.routes import posts
	from Flaskblog.main.routes import main
	from Flaskblog.errors.handlers import errors

	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)
	app.register_blueprint(errors)


	return app


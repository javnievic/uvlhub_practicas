import os
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from dotenv import load_dotenv
from flask_migrate import Migrate
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from core.configuration.configuration import get_app_version
from core.managers.module_manager import ModuleManager
from core.managers.config_manager import ConfigManager
from core.managers.error_handler_manager import ErrorHandlerManager
from core.managers.logging_manager import LoggingManager



# Load environment variables
load_dotenv()

# Create the instances
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

# For generating secure tokens
serializer = URLSafeTimedSerializer('contrasena')


def create_app(config_name='development'):
    app = Flask(__name__)
    # Load configuration according to environment
    config_manager = ConfigManager(app)
    config_manager.load_config(config_name=config_name)

    # Initialize SQLAlchemy and Migrate with the app
    db.init_app(app)
    migrate.init_app(app, db)
    app.config['SECRET_KEY'] = 'secret_key'
     
    # Configure mail settings
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'pruebasegc71@gmail.com'
    app.config['MAIL_PASSWORD'] = 'hykf iymv omwu rfjy '
    app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME'] 
    
    # Initialize mail
    mail.init_app(app)

    # Register modules
    module_manager = ModuleManager(app)
    module_manager.register_modules()

    # Register login manager
    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        from app.modules.auth.models import User
        return User.query.get(int(user_id))

    # Set up logging
    logging_manager = LoggingManager(app)
    logging_manager.setup_logging()

    # Initialize error handler manager
    error_handler_manager = ErrorHandlerManager(app)
    error_handler_manager.register_error_handlers()

    @app.route("/send_email/<email>", methods=["GET"])
    def send_verification_email(email):
        try:
            # Generate a secure token
            token = serializer.dumps(email, salt='email-confirm-salt')
            
            # Create the verification link
            link = url_for('confirm_email', token=token, _external=True)
            
            # Prepare the email message
            msg = Message('Confirm Your Email', recipients=[email])
            msg.body = f'Please click the following link to verify your email: {link}'
            
            # Send the email
            mail.send(msg)

            return f"A verification email has been sent to {email}"
        except Exception as e:
            print(e)
            return "Failed to send email"

    @app.route("/confirm_email/<token>")
    def confirm_email(token):
        try:
            email = serializer.loads(token, salt='email-confirm-salt', max_age=3600)
            # Here you can activate the user in the database
            return f'Email {email} has been verified!'
        except SignatureExpired:
            return 'The verification link has expired.'
        
    # Inject environment variables into Jinja context
    @app.context_processor
    def inject_vars_into_jinja():
        return {
            'FLASK_APP_NAME': os.getenv('FLASK_APP_NAME'),
            'FLASK_ENV': os.getenv('FLASK_ENV'),
            'DOMAIN': os.getenv('DOMAIN', 'localhost'),
            'APP_VERSION': get_app_version()
        }

    return app

app = create_app()

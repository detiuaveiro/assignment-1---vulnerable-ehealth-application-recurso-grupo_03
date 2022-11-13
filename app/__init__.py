from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')
    app.config['SECRET_KEY'] = 'shhhsecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    with app.app_context():
        db.create_all()
        admin = User.query.filter_by(email='admin@localhost').first()
        if not admin:
            admin = User(email='admin@localhost', password='admin', name='admin')
            db.session.add(admin)
            db.session.commit()

        # Read SQL data and execute it
        # with open('inserts.sql', 'r') as f:
        #     for line in f:
        #         db.session.execute(line)
        #         db.session.commit()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .contact import ctc as contact_blueprint
    app.register_blueprint(contact_blueprint)

    return app

from flask import Flask,redirect,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
import os


db=SQLAlchemy()

def createapp():
    app=Flask(__name__)

    app.config['SECRET_KEY']='your_sec_key'
    db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'instance', 'todo.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    

    return app

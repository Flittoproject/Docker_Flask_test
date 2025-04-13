from flask import Flask
from .db import db
from .routes import bp

def create_app():
    app = Flask(
        __name__,
        template_folder="/app/templates"  
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/mydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

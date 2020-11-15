from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.ProductionConfig')

    from .core.routes import blueprint as core_bp
    app.register_blueprint(core_bp)
    
    return app
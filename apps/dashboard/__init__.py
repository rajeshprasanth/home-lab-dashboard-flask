import os.path
import sys

# directory reach
directory = os.path.dirname(os.path.abspath("__file__"))
# setting path
sys.path.append(os.path.dirname(os.path.dirname(directory)))


# Flask Import
from flask import Flask


def register_blueprints(app):
    from apps.dashboard import routes
    app.register_blueprint(routes.routes_bp)
        
def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    with app.app_context():
            register_blueprints(app)
    
    @app.route('/testpage/')
    def test_page():
        return '<h1>Testing page for the Flask Application Factory Pattern</h1>'
        
    return app
from flask import Flask


def init_app():
    app = Flask(__name__, instance_relative_config = False)
    with app.app_context():
        from . import routes
        from .Dash.dashapp import init_dashboard
        
        print(f"[INFO] Initializing App...")
        app = init_dashboard(app)

        return app
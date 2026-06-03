import os
from flask import Flask, app, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'hantavirusr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    from . import auth
    from . import patients
    
    app.register_blueprint(auth.bp)
    db.init_app(app)
    app.register_blueprint(patients.bp, url_prefix='/patients')
    app.add_url_rule('/', endpoint='home')

    import os
from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'hantavirusr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    from . import auth
    from . import patients
    
    app.register_blueprint(auth.bp)
    db.init_app(app)
    app.register_blueprint(patients.bp, url_prefix='/patients')

    @app.route('/')
    def home():
        return render_template('home.html')
    
    return app
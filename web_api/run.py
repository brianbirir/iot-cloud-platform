from src import create_app


if __name__ == "__main__":
    """
    This module should only be used for development when running this application using the Flask web server.
    Running this is in production is not recommended hence look at other production level WSGI like Gunicorn
    """
    create_app('config.DevelopmentConfig').run(host='0.0.0.0', debug=True)

from flask import Flask, render_template
from logging.handlers import RotatingFileHandler
import json
import logging
import os
import argparse
from gunicorn.app.base import BaseApplication
from waitress import serve

app = Flask(__name__)

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure Flask logging to write to a file in the logs directory
log_file = "logs/flask.log"
handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

def load_data():
    try:
        with open('data.json', 'r') as jsonfile:
            return json.load(jsonfile)
    except FileNotFoundError:
        app.logger.error("data.json not found.")
        return []
    except json.JSONDecodeError:
        app.logger.error("Error decoding data.json.")
        return []

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
    devices = load_data()
    return render_template('template.html', devices=devices)

class FlaskApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def run_gunicorn(ip_address, port):
    options = {
        'bind': f'{ip_address}:{port}',
        'workers': 4,
        'threads': 2,
        'loglevel': 'info',
        'accesslog': 'logs/gunicorn-access.log',
        'errorlog': 'logs/gunicorn-error.log'
    }

    FlaskApplication(app, options).run()

def run_waitress(ip_address, port):
    log_file = 'logs/waitress.log'

    # Use the 'with' statement to ensure the log file is closed properly
    with open(log_file, 'w') as f:
        serve(app, host=ip_address, port=port, threads=4, ident=None, _quiet=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Flask app with different servers.')
    parser.add_argument('server', choices=['flask', 'gunicorn', 'waitress'], help='Select the server (flask, gunicorn, or waitress)')
    parser.add_argument('--ip', default='127.0.0.1', help='IP address to bind')
    parser.add_argument('--port', default='5000', help='Port to bind')

    args = parser.parse_args()

    if args.server == 'gunicorn':
        run_gunicorn(args.ip, args.port)
    elif args.server == 'waitress':
        run_waitress(args.ip, args.port)
    else:
        app.run(host=args.ip, port=int(args.port), debug=True)

from flask import Flask
import os

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')

@app.after_request
def add_header(response):
    """Add headers to prevent caching issues"""
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def index():
    """Serve the main Help Genie page"""
    return app.send_static_file('index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'healthy', 'service': 'Help Genie'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)

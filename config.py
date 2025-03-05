import os
import json

CONFIG_FILE = 'config.json'

default_config = {
    "ngrok_auth_token": "",
    "server_port": 5000,
    "save_logs": True,
    "log_file": "login_logs.txt"
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return default_config

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def setup_configuration():
    config = load_config()
    
    print("Welcome to the server configuration setup!")
    print("=" * 50)
    
    # Get ngrok auth token
    if not config['ngrok_auth_token']:
        print("\nPlease enter your ngrok auth token")
        print("(You can get it from: https://dashboard.ngrok.com/get-started/your-authtoken)")
        config['ngrok_auth_token'] = input("Auth Token: ").strip()
    
    # Configure port
    port = input(f"\nEnter server port (press Enter for default {config['server_port']}): ").strip()
    if port:
        config['server_port'] = int(port)
    
    # Configure logging
    save_logs = input("\nDo you want to save login attempts to a file? (y/n, default: y): ").strip().lower()
    config['save_logs'] = save_logs != 'n'
    
    if config['save_logs']:
        log_file = input(f"\nEnter log file name (press Enter for default {config['log_file']}): ").strip()
        if log_file:
            config['log_file'] = log_file
    
    # Save configuration
    save_config(config)
    print("\nConfiguration saved successfully!")
    return config

if __name__ == "__main__":
    setup_configuration() 
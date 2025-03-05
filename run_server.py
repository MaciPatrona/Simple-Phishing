from pyngrok import ngrok, exception
import subprocess
import sys
import os
import time
from config import load_config, setup_configuration

def connect_ngrok(port, max_retries=3):
    """Attempt to connect to ngrok with retries"""
    for attempt in range(max_retries):
        try:
            http_tunnel = ngrok.connect(port)
            return http_tunnel
        except exception.PyngrokNgrokError as e:
            if "context deadline exceeded" in str(e) or "failed to check for update" in str(e):
                if attempt < max_retries - 1:
                    print(f"\nNgrok connection attempt {attempt + 1} failed. Retrying in 5 seconds...")
                    time.sleep(5)
                    continue
            raise e
    raise Exception("Failed to connect to ngrok after multiple attempts")

def run_with_ngrok():
    # Load or create configuration
    config = load_config()
    
    # If no auth token is set, run the configuration setup
    if not config['ngrok_auth_token']:
        config = setup_configuration()
    
    print("\nInitializing server...")
    
    try:
        # Set ngrok auth token
        ngrok.set_auth_token(config['ngrok_auth_token'])
        
        # Start ngrok with retry mechanism
        http_tunnel = connect_ngrok(config['server_port'])
        public_url = http_tunnel.public_url
        
        print("\n" + "=" * 70)
        print(f"Public URL: {public_url}")
        print("=" * 70)
        
        if config['save_logs']:
            print(f"\nLogin attempts will be saved to: {os.path.abspath(config['log_file'])}")
        print("\nServer logs will appear below:\n")

        # Run the Flask application
        subprocess.run([sys.executable, "app.py"])
    
    except exception.PyngrokNgrokError as e:
        if "token" in str(e).lower():
            print("\nError: Invalid ngrok auth token. Please run 'python config.py' to update your token.")
        else:
            print(f"\nError connecting to ngrok: {str(e)}")
        print("\nPlease check your internet connection and try again.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nShutting down the server...")
    finally:
        try:
            ngrok.kill()
        except:
            pass

if __name__ == "__main__":
    run_with_ngrok() 
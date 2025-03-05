# 🔒 Login Logger

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A powerful Flask-based login logging system that captures detailed information about login attempts through a public URL using ngrok. Perfect for security research and monitoring login attempts.

## ✨ Features

- 🌐 **Public URL Access**: Instantly get a public URL using ngrok
- 📝 **Detailed Logging**: Captures comprehensive information for each login attempt:
  - Real IP Address
  - Geographic Location (City, Country)
  - User Agent (Browser/Device info)
  - Timestamp
- 🔄 **Auto-Retry**: Smart connection handling with automatic retries
- 💾 **File Logging**: Option to save all login attempts to a file
- ⚙️ **Easy Configuration**: Simple setup with interactive configuration
- 🎨 **Clean UI**: Modern and responsive login interface

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- ngrok account (free) - [Sign up here](https://dashboard.ngrok.com/signup)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/login-logger.git
cd login-logger
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python run_server.py
```

On first run, you'll be prompted to:
- Enter your ngrok auth token
- Configure the port number (default: 5000)
- Set up logging preferences

## 📝 Configuration

You can reconfigure the application at any time:
```bash
python config.py
```

Configuration options:
- `ngrok_auth_token`: Your ngrok authentication token
- `server_port`: Port number for the Flask server
- `save_logs`: Enable/disable file logging
- `log_file`: Custom log file name

## 📊 Log Format

Each login attempt is logged in the following format:
```
new login [username] [password] | IP: [real_ip] | Location: [city], [country] | User-Agent: [browser_info] | Time: [timestamp]
```

Example:
```
new login admin password123 | IP: 203.0.113.1 | Location: New York, United States | User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) | Time: 2024-02-20 15:30:45
```

## 🛡️ Security Features

- Real IP detection through proxy
- Geographic location tracking
- Browser fingerprinting
- Automatic retry mechanism for connection issues
- Secure configuration storage

## 🔧 Advanced Usage

### Custom Port

You can change the port during setup or by editing `config.json`:
```json
{
    "server_port": 8080
}
```

### Custom Log File

Specify a custom log file name during setup or in `config.json`:
```json
{
    "log_file": "custom_logs.txt"
}
```

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Do not use it for unauthorized access or malicious purposes. Always comply with applicable laws and regulations.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions:
- Open an issue
- Submit a pull request
- Contact the maintainers

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/login-logger&type=Date)](https://star-history.com/#yourusername/login-logger&Date)

---
Made with ❤️ by [Your Name] 
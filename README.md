# Help Genie 🤝💯

An AI-powered code editor with multi-language support that helps you build applications using natural language. Get instant coding help, explanations, and code suggestions with our intelligent coding assistant.

## Features

### 🚀 AI-Powered Development
- **AI Code Generation**: Get instant code suggestions and snippets with AI-powered assistance
- **Intelligent Chat**: Chat with AI to explain code, debug issues, and get real-time coding help
- **Multi-Language Support**: Support for 21+ programming languages including Python, JavaScript, Java, C++, Go, Rust, and more

### 💻 Advanced Code Editor
- **Monaco Editor Integration**: Industry-standard code editor with syntax highlighting
- **Real-time Code Execution**: Run and test your code directly in the browser
- **Multi-Language Support**: Python, JavaScript, Java, C++, TypeScript, Rust, Go, Ruby, PHP, Swift, Kotlin, C#, Scala, SQL, R, HTML, CSS, Perl, Lua, Bash, and C

### 🎨 Modern UI/UX
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Interactive Code Mockup**: Live code demonstrations with syntax highlighting
- **Smooth Animations**: Professional transitions and hover effects

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Code Editor**: Monaco Editor (VS Code's editor)
- **AI Integration**: HuggingFace Transformers
- **Backend**: Flask (Python)
- **Icons**: Font Awesome
- **Fonts**: Cormorant Garamond, Karla, Spectral, IBM Plex Mono, Elianto

## Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Setup

1. **Clone or download the repository**
   ```bash
   # If using git
   git clone <repository-url>
   cd help-genie
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install Flask manually:
   ```bash
   pip install flask
   ```

3. **Set environment variables (optional)**
   ```bash
   export SESSION_SECRET="your-secret-key-here"
   export FLASK_ENV="development"  # For development mode
   ```

## Running the Application

### Development Mode

Run the Flask application:
```bash
python app.py
```

The application will start on `http://localhost:5000`

### Production Deployment

For production deployment, use a production-ready WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Project Structure

```
help-genie/
├── app.py                 # Flask backend application
├── static/
│   └── index.html        # Main webpage with embedded CSS/JS
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore file (if applicable)
```

## Usage

1. **Home Page**: View the landing page with feature highlights
2. **Code Editor**: Click "Start Coding" to access the multi-language code editor
3. **AI Chat**: Click "Try AI Chat" to interact with the AI coding assistant

## Configuration

### Environment Variables

- `SESSION_SECRET`: Secret key for Flask sessions (default: 'dev-secret-key-change-in-production')
- `PORT`: Port number for the server (default: 5000)
- `FLASK_ENV`: Environment mode ('development' or 'production')

### Customization

The main HTML file (`static/index.html`) is served as a static file and contains embedded CSS and JavaScript for easy customization:
- Modify styles in the `<style>` section
- Update JavaScript functionality in the `<script>` section
- Change content directly in the HTML

Note: The HTML is served as a static file (not as a Jinja2 template) to preserve all embedded code and avoid template parsing conflicts.

## Features Overview

### Supported Programming Languages

- 🐍 Python
- ⚡ JavaScript
- ☕ Java
- ⚙️ C++
- 🔷 TypeScript
- 🦀 Rust
- 🐹 Go
- 💎 Ruby
- 🐘 PHP
- 🍎 Swift
- 🤖 Kotlin
- 💻 C#
- 🎯 Scala
- 🗄️ SQL
- 📊 R
- 🌐 HTML
- 🎨 CSS
- 🐪 Perl
- 🌙 Lua
- 💻 Bash
- ⚡ C

## API Endpoints

- `GET /` - Main application page
- `GET /health` - Health check endpoint

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Opera

## Performance Optimization

The application includes several optimizations:
- Responsive hero section for better desktop viewing
- Lazy loading for resources
- CDN-hosted libraries for faster loading
- Cache control headers for optimal performance

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is available for educational and personal use.

## Support

For questions or issues, please contact the development team.

---

**Note**: This application uses CDN-hosted libraries for development. For production use, consider hosting these resources locally or using a build process.

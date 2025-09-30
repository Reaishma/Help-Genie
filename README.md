
<centre># Help Genie 🤝💯</centre>

An AI-powered code editor with multi-language support that helps you build applications using natural language. Get instant coding help, explanations, and code suggestions with our intelligent coding assistant. The application combines a Monaco-based code editor with HuggingFace's AI models to offer code generation, explanations, and debugging support across 21+ programming languages.

# Access the project 

**Try Live on https://help-genie.vercel.app/**

**Web Interface on https://reaishma.github.io/Help-Genie/**

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
- **Code Editor**: Monaco Editor (VS Code's editor)for Industry-standard code editor (VS Code's editor engine) for syntax highlighting and code editing across multiple languages
- **AI Integration**: HuggingFace Transformers
- **Tailwind CSS**: Utility-first CSS framework for responsive, mobile-first design
- **Backend**: Flask (Python)
- **Icons**: Font Awesome
- **Fonts**: Cormorant Garamond, Karla, Spectral, IBM Plex Mono, Elianto

## External Dependencies

### Third-Party Services
- **HuggingFace CDN**: Delivers Transformers.js library and AI models for client-side inference
- **Cloudflare CDN**: Hosts Monaco Editor, Font Awesome icons, and Tailwind CSS
- **Google Fonts API**: Serves custom web fonts (Cormorant Garamond, Karla, Spectral)
- **OnlineWebFonts**: Serves Elianto font family

### Python Dependencies
- **Flask 3.1.2**: Lightweight WSGI web framework for serving static files
- **Werkzeug 3.1.3**: WSGI utility library (Flask dependency)
- **Jinja2 3.1.6**: Template engine (Flask dependency, minimal usage)
- **Click 8.3.0**: Command-line interface toolkit (Flask dependency)

### Frontend Libraries (CDN-based)
- **Monaco Editor 0.44.0**: Code editor component
- **HuggingFace Transformers.js 3.0.0**: Browser-based AI model inference
- **Tailwind CSS**: Latest version via CDN (utility-first CSS framework)
- **Font Awesome 6.4.0**: Icon library

### Browser APIs & Features
The application relies on modern browser capabilities:
- ES6 Modules for HuggingFace integration
- WebAssembly for AI model execution
- Service Workers (potentially, for offline functionality)

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

## Deployment Configuration
- **Environment Variables**: 
  - `PORT`: Server port (default: 5000)
  - `FLASK_ENV`: Development/production mode toggle
  - `SESSION_SECRET`: Flask secret key for security

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

This project is available for educational and personal use.and licensed under MIT LICENCE 

## Support

For questions or issues, please contact the developer
**Reaishma N**
**email ID vra.9618@gmail.com**

---



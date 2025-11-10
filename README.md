# Treasure Island Project

## Overview
A web-based interactive adventure game written in Python/Flask where players navigate through a treasure hunt by making choices at different decision points. Originally a terminal/console-based game, it has been converted to a modern web application with rich multimedia content including videos and images that enhance the storytelling experience.

## Live Demo
- **Deployment URL**: https://day-3-treasure-island-project-andreszubi.replit.app

## Project Type
Web Application - Interactive Adventure Game with Multimedia Content

## Technology Stack
- **Framework**: Flask 3.1.2
- **Language**: Python 3.13.5 (requires Python >=3.11)
- **Frontend**: HTML5, CSS3 (external stylesheet)
- **Template Engine**: Jinja2 (Flask's default)
- **Session Management**: Flask sessions with secure token-based secret keys
- **Package Manager**: uv
- **Deployment**: Replit Autoscale (web server)

## Project Structure
```
.
├── app.py                          # Flask web application with game logic
├── templates/
│   └── game.html                   # HTML template with video/image integration
├── static/
│   ├── style.css                   # External CSS stylesheet
│   ├── images/
│   │   ├── three-doors.png         # House scene image
│   │   └── goblin-encounter.png    # Goblins game over image
│   └── video/
│       ├── mystical-treasure.mp4   # Start screen video
│       ├── lake-video.mp4          # Lake scene video
│       ├── piranhas-video.mp4      # Piranhas game over video
│       ├── troll-video.mp4         # Troll game over video
│       ├── chimera-video.mp4       # Chimera game over video
│       └── fairies-video.mp4       # Win screen video
├── Treasure-Island-Project.py      # Original console version (preserved for reference)
├── pyproject.toml                  # Python dependencies (managed by uv)
├── uv.lock                         # Lock file for dependencies
├── .venv/                          # Virtual environment
├── .vscode/                        # VS Code configuration
├── .gitignore                      # Git ignore file
├── .python-version                 # Python version specification
└── README.md                       # Project documentation
```

## Features
- **Interactive Storytelling**: Multiple decision points leading to different outcomes
- **Rich Multimedia Content**: 
  - Video content for key scenes (start, lake, game over scenarios, win screen)
  - High-quality images for house and goblin encounter scenes
- **Responsive Design**: Mobile-friendly interface with adaptive video/image sizing
- **Session Management**: Multiple players can play simultaneously with independent game states
- **Visual Feedback**: Status badges for win/lose states, styled game over screens
- **HD Quality Media**: Hardware-accelerated video rendering with smooth playback

## How It Works
The Flask app uses a state machine approach with a dictionary-based story structure:
- Story nodes are defined in `STORY_NODES` dictionary
- Each node contains: title, text, options, and game state flags (game_over, win)
- Player progress is tracked using Flask sessions
- Form submissions navigate between story nodes via POST requests
- Session-based state ensures multiple players can play simultaneously

### Game Flow
1. Player visits root `/` → redirects to `/play` with fresh session
2. `/play` renders current story node from session with appropriate media (video/image)
3. Player clicks choice button → POST to `/play` with choice value
4. App validates choice and updates session to next node
5. Redirects back to `/play` to render new node
6. Game ends when reaching win or game_over nodes
7. "Play Again" button restarts via `/restart` route

### Story Paths
- **Start** → Choose Left (Lake) or Right (Cave/Troll)
- **Lake** → Wait for boat (House) or Swim (Piranhas)
- **House** → Choose Red Door (Chimera), Yellow Door (Win/Fairies), or Blue Door (Goblins)
- **Multiple Endings**: 1 winning path, 4 game over scenarios

## Development Setup

### Prerequisites
- Python 3.11 or higher (tested with Python 3.13.5)
- uv package manager (or pip)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/andreszubi/Day-3-Treasure-Island-Project.git
   cd Day-3-Treasure-Island-Project
   ```

2. **Create and activate virtual environment**
   ```bash
   # Using uv (recommended)
   uv sync
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   
   # Alternatively, using venv
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   # Using uv
   uv sync
   
   # Alternatively, using pip
   pip install -r requirements.txt  # If you have one
   # Or install directly
   pip install flask>=3.1.2
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`
   - The application runs on `0.0.0.0:5000` with debug mode enabled

### Development Configuration
- **Host**: `0.0.0.0` (accessible from all network interfaces)
- **Port**: `5000`
- **Debug Mode**: Enabled (auto-reload on code changes)
- **Secret Key**: Generated dynamically using `secrets.token_hex(16)`

### VS Code Setup
The project includes VS Code configuration in `.vscode/settings.json`:
- Python interpreter path: `.venv/bin/python`
- Virtual environment detection enabled
- Type checking mode: basic

## Deployment Configuration

### Replit Deployment
- **Type**: Autoscale (web server)
- **Run Command**: `["python", "app.py"]`
- **Port**: `5000`
- **Host**: `0.0.0.0`
- **Environment**: Python 3.11+

### Production Considerations
- **Debug Mode**: Should be disabled in production (`debug=False`)
- **Secret Key**: Use environment variable for production (`os.environ.get('SECRET_KEY')`)
- **Static Files**: All media files (videos/images) are served from `static/` directory
- **Session Security**: Consider using secure cookies in production (`SESSION_COOKIE_SECURE=True`)

### Deployment Steps
1. Ensure all dependencies are listed in `pyproject.toml`
2. Verify all static files (videos/images) are in the repository
3. Set environment variables if needed
4. Configure web server to run `python app.py`
5. Ensure port 5000 is accessible (or configure reverse proxy)

## Media Assets
The project includes the following media files:
- **Videos** (6 files, ~19MB total):
  - `mystical-treasure.mp4` - Welcome screen (3.5MB)
  - `lake-video.mp4` - Lake scene (1.8MB)
  - `piranhas-video.mp4` - Piranhas game over (6.5MB)
  - `troll-video.mp4` - Troll game over (2.0MB)
  - `chimera-video.mp4` - Chimera game over (2.7MB)
  - `fairies-video.mp4` - Win screen (2.9MB)

- **Images** (2 files):
  - `three-doors.png` - House scene with three doors (361KB)
  - `goblin-encounter.png` - Goblins game over scene (340KB)

All media files are optimized for web delivery and use responsive sizing for different screen sizes.

## File Descriptions

### `app.py`
Main Flask application file containing:
- Flask app initialization
- Story nodes dictionary (`STORY_NODES`)
- Route handlers (`/`, `/play`, `/restart`)
- Session management logic
- Game state machine implementation

### `templates/game.html`
Jinja2 template file containing:
- HTML structure for game interface
- Conditional rendering for videos/images based on current node
- Form handling for player choices
- Status badges for win/lose states

### `static/style.css`
External stylesheet containing:
- Responsive design rules
- Video and image container styling
- Button and form styling
- Mobile-friendly media queries
- HD quality rendering optimizations

## Contributing
This is a personal project, but suggestions and feedback are welcome!

## License
This project is open source and available for educational purposes.

## Author
Andres Zubizarreta

## Version
1.0.0 - Initial web version with multimedia content

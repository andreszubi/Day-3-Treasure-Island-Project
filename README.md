# Treasure Island Project

## Overview
A web-based adventure game written in Python/Flask where players navigate through a treasure hunt by making choices at different decision points. Originally a console-based game, it has been converted to a deployable web application with a beautiful browser interface.

## Project Type
Web Application - Interactive Adventure Game

## Technology Stack
- **Framework**: Flask 3.1.2
- **Language**: Python 3.11
- **Frontend**: HTML5 with embedded CSS
- **Session Management**: Flask sessions with secure tokens
- **Deployment**: Replit Autoscale (web server)

## Project Structure
```
.
├── app.py                       # Flask web application with game logic
├── templates/
│   └── game.html                # HTML template with styling and forms
├── Treasure-Island-Project.py   # Original console version (preserved for reference)
├── README.md                    # Project documentation
├── replit.md                    # Project memory and configuration
├── .gitignore                   # Python gitignore
├── pyproject.toml              # Python dependencies (managed by uv)
└── uv.lock                     # Lock file for dependencies
```

## How It Works
The Flask app uses a state machine approach:
- Story nodes are defined in a structured dictionary (`STORY_NODES`)
- Each node contains: title, text, options, and game state flags
- Player progress is tracked using Flask sessions
- Form submissions navigate between story nodes
- Session-based state ensures multiple players can play simultaneously

Game Flow:
1. Player visits root `/` → redirects to `/play` with fresh session
2. `/play` renders current story node from session
3. Player clicks choice button → POST to `/play` with choice
4. App updates session to next node, redirects back to `/play`
5. Game ends when reaching win or game_over nodes
6. "Play Again" button restarts via `/restart` route

## Development Setup
- **Runtime**: Python 3.11
- **Package Manager**: uv (Replit's Python package manager)
- **Workflow**: Runs `python app.py` on port 5000 with webview output
- **Host**: 0.0.0.0 (required for Replit's proxy system)

## Deployment Configuration
- **Type**: Autoscale (web server)
- **Run Command**: `["python", "app.py"]`
- **Port**: 5000
- **Ready for Production**: Yes

## Recent Changes
- **2025-11-09**: Converted console game to web application
  - Created Flask application with session-based state management
  - Built responsive HTML template with gradient styling
  - Restructured game logic into data-driven STORY_NODES dictionary
  - Installed Flask via uv package manager
  - Updated workflow to run Flask app with webview on port 5000
  - Configured Autoscale deployment for public access
  - Updated all documentation (README.md and replit.md)
  - Preserved original console version for reference

## User Preferences
- User wanted to deploy/publish the application online
- Required conversion from console-based to web-based interface

## Architecture Notes
- **Why Flask**: Lightweight, simple routing perfect for small game
- **Why Sessions**: Stateless HTTP requires state tracking between requests
- **Why Autoscale**: Game is stateless (session in cookies), scales with traffic
- **Security**: Uses `secrets.token_hex(16)` for session key
- **Code Organization**: All story content in one data structure for easy editing

## Potential Future Enhancements
- Add sound effects and background music
- Create multiple story paths/adventures
- Add player achievements or high scores
- Implement save/load progress feature
- Add difficulty levels or randomized encounters
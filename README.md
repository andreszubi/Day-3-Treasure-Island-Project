# Treasure Island Project

## Overview
A web-based adventure game written in Python/Flask where players navigate through a treasure hunt by making choices at different decision points. Originally a terminal ID console-based game, it has been converted to a deployable web application with a beautiful browser interface.

## Link 

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
- **Host**: 0.0.0.0 

## Deployment Configuration
- **Type**: Autoscale (web server)
- **Run Command**: `["python", "app.py"]`
- **Port**: 5000
- **Ready for Production**: Yes

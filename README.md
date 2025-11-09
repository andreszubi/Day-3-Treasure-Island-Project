# Treasure Island Project

## Overview
A web-based adventure game written in Python/Flask where players navigate through a treasure hunt by making choices at different decision points. The game features beautiful ASCII art and an interactive browser-based interface.

## Project Type
Web Application - Interactive Adventure Game

## Technology Stack
- **Framework**: Flask 3.1.2
- **Language**: Python 3.11
- **Frontend**: HTML5 with embedded CSS
- **Session Management**: Flask sessions with secure tokens
- **Deployment**: Replit Autoscale

## Project Structure
```
.
├── app.py                       # Flask web application with game logic
├── templates/
│   └── game.html                # HTML template with styling and forms
├── Treasure-Island-Project.py   # Original console version (legacy)
├── README.md                    # Project documentation
└── replit.md                    # Project memory and configuration
```

## How It Works
The game presents players with a series of choices through a web interface:
1. Start at a crossroad (left or right)
2. If left: encounter a lake (swim or wait for boat)
3. If wait: reach a house with three colored doors (red, yellow, or blue)
4. Only the correct path leads to treasure!

Game state is managed using Flask sessions, ensuring each player's progress is tracked independently.

## Running Locally
The app runs automatically in Replit. The workflow is configured to:
```bash
python app.py
```
The server runs on `http://0.0.0.0:5000`

## Deployment
This app is configured for Replit Autoscale deployment:
- **Deployment Target**: Autoscale (web server)
- **Run Command**: `python app.py`
- **Port**: 5000
- **Host**: 0.0.0.0

To deploy:
1. Click the "Publish" button in Replit
2. The app will be deployed automatically with the configured settings
3. Your game will be accessible via a public URL

## Game Features
- Beautiful retro-style ASCII art
- Responsive design (mobile-friendly)
- Session-based state management
- Multiple story paths and endings
- Game Over and Victory screens
- Play Again functionality

## Recent Changes
- **2025-11-09**: Converted to web application for deployment
  - Created Flask web application with session management
  - Built responsive HTML/CSS interface
  - Restructured game logic into data-driven format
  - Configured autoscale deployment
  - Added deployment documentation

## Technical Notes
- The original console version (`Treasure-Island-Project.py`) is preserved for reference
- The web version uses Flask's session management for state tracking
- All story nodes are defined in a structured dictionary for easy modification
- The app uses secure session tokens for player identification

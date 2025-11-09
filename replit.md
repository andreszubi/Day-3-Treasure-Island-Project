# Treasure Island Adventure Game

## Overview

Treasure Island is an interactive web-based adventure game built with Flask where players navigate through a story-driven treasure hunt by making choices at decision points. The game uses a state machine architecture with session-based progress tracking, allowing multiple concurrent players. Originally a console application, it has been transformed into a modern web experience while preserving the nostalgic ASCII art aesthetic.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Application Architecture

**Pattern**: Model-View-Controller (MVC) with Session-Based State Management
- **Model**: Story nodes stored in a Python dictionary (`STORY_NODES`) representing the game's state machine
- **View**: Single HTML template (`game.html`) with embedded CSS for all game screens
- **Controller**: Flask routes handle navigation between story nodes based on player choices

**Rationale**: This approach keeps the game logic centralized and easily extensible. New story branches can be added by simply extending the `STORY_NODES` dictionary without modifying routing logic.

### Frontend Architecture

**Single Template Design**: One HTML file (`game.html`) dynamically renders different game states
- Uses Jinja2 templating to display current story node content
- Form-based interaction for player choices
- Embedded CSS for self-contained styling without external dependencies

**Pros**: 
- Simple deployment with no build process
- Fast page loads with minimal HTTP requests
- Easy to understand and modify

**Cons**: 
- Limited scalability for complex UI interactions
- No client-side state management

### Backend Architecture

**State Machine Pattern**: Game progression managed through node-based navigation
- Each node contains: title, story text, available choices, and terminal state flags (win/game_over)
- Player's current position stored in Flask session
- POST requests with choice values trigger state transitions

**Session Management**: 
- Server-side sessions using Flask's built-in session handling
- Secure secret key generated with `secrets.token_hex(16)`
- Session data persists player's current node across requests
- Enables multiple simultaneous players without interference

**Routing Strategy**:
- `/` - Landing page that initializes fresh session and redirects to `/play`
- `/play` - Main game route (GET displays current state, POST processes choices)
- `/restart` - Clears session and returns to start

**Alternative Considered**: Client-side state with JavaScript
- Rejected because server-side sessions provide better security and simpler implementation for a story-driven game

### Data Storage

**In-Memory Dictionary**: Story content stored in Python dictionary structure
- No database required for current scope
- Story nodes are static content defined at application startup
- Session data handled by Flask's session mechanism (signed cookies)

**Rationale**: For a small-scale adventure game with static story content, a database would add unnecessary complexity. The dictionary approach allows rapid iteration on story content and keeps the entire game logic readable in a single file.

**Future Consideration**: If user progress persistence or analytics are needed, a lightweight database like SQLite could be integrated without major refactoring.

## External Dependencies

### Python Packages (via uv)
- **Flask 3.1.2**: Web framework providing routing, templating, and session management
  - Core dependency for the entire web application
  - Includes Jinja2 for HTML templating
  - Built-in session support with signed cookies

### Runtime Environment
- **Python 3.11**: Application runtime
- **uv**: Python package manager (Replit's standard)
- **Deployment**: Replit Autoscale deployment platform
  - Web server runs on port 5000
  - Host configured as 0.0.0.0 for external access

### Development Tools
- **pyproject.toml**: Python project configuration and dependency specification
- **uv.lock**: Locked dependency versions for reproducible builds

**Note**: No external APIs, databases, or third-party services are currently integrated. The application is completely self-contained.
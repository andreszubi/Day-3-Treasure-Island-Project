# Treasure Island - Interactive Adventure Game

## Overview

Treasure Island is a web-based choose-your-own-adventure game built with Flask. Players navigate through a treasure hunt by making choices at different story nodes, with each decision leading to different outcomes including game over scenarios or winning the treasure. The application uses a state machine pattern where story progression is managed through session-based tracking, allowing multiple concurrent players.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Application Pattern: State Machine with Session Management

**Problem**: Need to track individual player progress through a branching narrative while supporting multiple concurrent users.

**Solution**: Implemented a stateless server design using Flask sessions to store current game state (node position) client-side.

**Key Design Decisions**:

- **Story Data Structure**: All narrative content stored in a centralized `STORY_NODES` dictionary where each node contains title, text, choice options, and game state flags (win/game_over)
- **Session-Based State**: Current node tracked in Flask session rather than server memory, enabling horizontal scaling and stateless deployments
- **POST/Redirect/GET Pattern**: Form submissions POST to `/play`, update session, then redirect back to GET `/play` to prevent duplicate submissions on refresh

**Alternatives Considered**: 
- Database-backed progress tracking (rejected: overkill for simple game with no save/load requirements)
- Client-side JavaScript state (rejected: wanted server-controlled game logic)

**Pros**: Simple architecture, no database needed, naturally supports multiple players, easy to extend with new story nodes

**Cons**: Session data lost if cookies cleared, no persistent save games across devices

### Frontend Architecture

**Problem**: Need engaging, retro-style interface that works across devices.

**Solution**: Server-side rendered HTML templates with embedded CSS, no JavaScript framework.

**Key Decisions**:
- Single template (`game.html`) with conditional rendering based on game state
- ASCII art preserved from original console version for nostalgic aesthetic
- Responsive CSS with gradient backgrounds and monospace fonts for retro gaming feel
- Form-based navigation using POST requests for choice selection

**Pros**: Fast page loads, works without JavaScript, simple deployment

**Cons**: Full page reloads on each choice (acceptable for this use case)

### Routing Architecture

Three-route design:
- `GET /` - Entry point, initializes fresh session and redirects to `/play`
- `GET /play` - Renders current story node from session state
- `POST /play` - Processes player choice, updates session to next node, redirects back to GET `/play`
- `GET /restart` - Clears session and redirects to root for new game

**Rationale**: Minimal routing keeps codebase simple while POST/Redirect/GET pattern prevents form resubmission issues.

### Security

**Session Security**: Uses `secrets.token_hex(16)` to generate cryptographically secure session keys on application startup.

**Consideration**: Secret key regenerates on each deployment/restart, invalidating existing sessions. For production with persistent sessions, would need environment variable or key management solution.

## External Dependencies

### Core Framework
- **Flask 3.1.2**: Lightweight WSGI web framework, chosen for simplicity and low overhead for small application

### Python Runtime
- **Python 3.11**: Modern Python version with performance improvements
- **Package Manager**: uv (Replit's fast Python package manager) manages dependencies via `pyproject.toml`

### Deployment Platform
- **Replit Autoscale**: Hosts the web application, provides automatic HTTPS and deployment
- **No Database**: Application is entirely stateless with client-side session storage
- **No External APIs**: Self-contained game logic with no third-party service integrations

### Development Dependencies
None beyond Flask - application intentionally kept minimal with no additional libraries for templating, validation, or utilities.
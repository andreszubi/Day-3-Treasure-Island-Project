# Treasure Island Adventure Game

## Overview

Treasure Island is a web-based interactive adventure game built with Flask. Players navigate through a treasure hunt by making choices at different decision points. The game uses a state machine architecture where each story node contains narrative text, available choices, and game state flags. Originally a console-based Python game, it has been converted to a web application with session-based state management to support multiple concurrent players.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Application Architecture

**Framework Choice: Flask 3.1.2**
- *Problem*: Need a lightweight web framework to convert console game to web application
- *Solution*: Flask chosen for its simplicity and minimal boilerplate
- *Rationale*: Small project scope doesn't require heavy frameworks like Django; Flask's built-in session management and templating perfectly suits single-page game interaction

**State Management: Server-Side Sessions**
- *Problem*: Track player progress through story nodes while supporting multiple concurrent players
- *Solution*: Flask sessions with secure token-based keys
- *Implementation*: `app.secret_key = secrets.token_hex(16)` for cryptographic security
- *Rationale*: Server-side sessions prevent client manipulation of game state and naturally isolate player instances without requiring database

**Game Logic: Dictionary-Based State Machine**
- *Problem*: Represent branching narrative with multiple decision points and outcomes
- *Solution*: `STORY_NODES` dictionary where each key represents a game state containing title, text, choice options, and terminal state flags (win/game_over)
- *Structure*: Each node defines next states via choice values, creating a directed graph of story progression
- *Rationale*: Simple, readable data structure that's easy to extend; no database needed for static content

### Frontend Architecture

**Single Template Pattern**
- *Problem*: Display dynamic game content without page reloads feeling jarring
- *Solution*: Single `game.html` template that renders current node state
- *Implementation*: Form POST submissions with redirects maintain clean URL structure
- *Rationale*: Keeps UI consistent; all game rendering logic centralized in one template

**Styling Approach: Embedded CSS**
- *Problem*: Create retro terminal aesthetic for treasure hunt game
- *Solution*: Embedded CSS in template with ASCII art display and gradient backgrounds
- *Design Choices*: Monospace font family, dark terminal-style ASCII container, blue gradient background
- *Rationale*: Small project doesn't warrant separate CSS files; embedded styles keep deployment simple

### Routing Architecture

**Three-Route Design**
1. `/` - Entry point that initializes session and redirects to `/play`
2. `/play` - Main game route (GET displays current node, POST processes choices)
3. `/restart` - Clears session and redirects to start

- *Problem*: Handle game initialization, progression, and restart
- *Solution*: Minimal route structure with redirect-after-POST pattern
- *Rationale*: Prevents form resubmission issues; clean separation of concerns

### Data Flow

1. Player visits root → session initialized with 'current_node' = 'start'
2. Redirect to `/play` → template renders node from `STORY_NODES[session['current_node']]`
3. Player submits choice → POST handler finds matching option, updates session to next node
4. Redirect back to `/play` → new node renders
5. Terminal nodes (win/game_over) display restart button instead of choices

## External Dependencies

### Python Packages (via uv)

- **Flask 3.1.2**: Core web framework for routing, templating, and session management
- **secrets** (stdlib): Cryptographic token generation for session security
- No database dependencies (game data stored in-memory as Python dictionary)

### Deployment Platform

- **Replit Autoscale**: Hosting environment
- **Configuration**: Runs on port 5000, bound to 0.0.0.0 for external access
- **Runtime**: Python 3.11 with uv package manager

### No External Services

- No third-party APIs
- No external databases
- No authentication providers
- No CDN dependencies for frontend assets
- Self-contained application with all resources embedded or stored in code
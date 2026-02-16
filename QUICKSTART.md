# Getting Started - Robot Mover Flask Web App

## Installation

Prerequisites: Python 3.7+

```bash
# Install dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
# Start the Flask development server
python app.py
```

The app will be available at: **http://localhost:5000**

## Project Structure

```
Robot-Mover/
├── models/                 # Core game logic
│   ├── __init__.py
│   ├── direction.py       # Direction enum (NORTH, EAST, SOUTH, WEST)
│   ├── position.py        # Position class
│   ├── grid.py           # Grid and Cell classes
│   └── roomba.py         # Roomba robot class
├── controllers/          # Application controllers
│   ├── __init__.py
│   └── app_controller.py # Game state management
├── templates/           # HTML templates
│   └── index.html      # Main UI
├── static/             # Static assets
│   ├── style.css      # Styling
│   └── script.js      # Client-side logic
├── tests/             # Test suite
│   └── test_models.py # Unit tests
├── app.py            # Flask application entry point
├── requirements.txt  # Python dependencies
└── README.md        # Original project requirements
```

## How It Works

### Models Layer
- **Direction**: Enum for roomba orientation with rotation logic
- **Position**: Simple x,y coordinate class
- **Grid**: 10×10 grid with boundary walls
- **Cell**: Individual grid cells (wall or empty)
- **Roomba**: Robot with movement and collision detection

### Controller Layer
- **AppController**: Manages game state and coordinates moves

### Web Layer
- **Flask Routes**:
  - `GET /` - Render main page
  - `POST /api/move-forward` - Move roomba or turn on collision
  - `POST /api/turn-right` - Rotate 90° right
  - `POST /api/reset` - Reset to starting position
  - `GET /api/state` - Get current game state

### UI Layer
- **HTML/CSS**: Responsive grid display with direction indicator
- **JavaScript**: AJAX calls to backend, dynamic UI updates

## Features

✓ 10×10 grid with boundary walls  
✓ Roomba movement in 4 directions  
✓ Automatic right-turn on wall collision  
✓ Visual direction indicator (↑ ↓ ← →)  
✓ Manual step-by-step control  
✓ Real-time position and direction display  
✓ Reset button to return to starting position  

## Testing

Run the test suite to verify all game logic:

```bash
python tests/test_models.py
```

All tests should pass, verifying:
- Direction rotation
- Position tracking
- Grid bounds checking
- Roomba movement
- Wall collision detection
- Edge collision handling
- Controller state management

## Architecture Highlights

### Clean Separation of Concerns
- **Models** (models/) - Pure game logic, no dependencies
- **Controllers** (controllers/) - State management, orchestrates models
- **Views** (templates/static/) - Presentation and user interaction
- **Entry Point** (app.py) - Flask app initialization and routing

### Collision Handling
When the roomba encounters a wall:
1. Next position is checked via `getNextPosition(grid)`
2. If invalid (out of bounds or wall), `moveForward()` calls `turnRight()` instead
3. No movement occurs, only rotation

### Server-Side State
Game state is managed server-side, with clients using AJAX to send commands and receive updated state as JSON.

## Browser Compatibility

Works with modern browsers supporting:
- ES6 JavaScript
- Fetch API
- CSS Grid/Flexbox

## Customization Options

### Modify Grid Size
Edit [controllers/app_controller.py](controllers/app_controller.py):
```python
self.grid = Grid(width=15, height=15)  # Change dimensions
```

### Add Internal Walls
Edit [models/grid.py](models/grid.py) `_create_grid()` method to mark specific cells as walls.

### Change Starting Position
Edit [controllers/app_controller.py](controllers/app_controller.py) to modify the initial Roomba coordinates.

## API Response Format

```json
{
  "grid": {
    "width": 10,
    "height": 10,
    "cells": [
      [{"x": 0, "y": 0, "isWall": true}, ...],
      ...
    ]
  },
  "roomba": {
    "x": 1,
    "y": 1,
    "direction": "NORTH"
  }
}
```

## Future Enhancements

- Add automatic movement (play/pause mode)
- Draw custom obstacles via UI
- Record and replay movement history
- Multiple roombas
- Different grid layouts
- WebSocket for real-time updates

---

Enjoy your Robot Mover simulator! 🤖

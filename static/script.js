/**
 * JavaScript for Robot Mover Roomba Simulator
 */

const directionArrows = {
    'NORTH': '↑',
    'EAST': '→',
    'SOUTH': '↓',
    'WEST': '←'
};

const directionNames = {
    'NORTH': 'North ↑',
    'EAST': 'East →',
    'SOUTH': 'South ↓',
    'WEST': 'West ←'
};

// Get DOM elements
const moveBtn = document.getElementById('moveBtn');
const turnBtn = document.getElementById('turnBtn');
const resetBtn = document.getElementById('resetBtn');
const posXSpan = document.getElementById('pos-x');
const posYSpan = document.getElementById('pos-y');
const directionSpan = document.getElementById('direction');
const directionIndicator = document.getElementById('direction-indicator');

// Event listeners
moveBtn.addEventListener('click', handleMoveForward);
turnBtn.addEventListener('click', handleTurnRight);
resetBtn.addEventListener('click', handleReset);

/**
 * Handle move forward action
 */
async function handleMoveForward() {
    try {
        const response = await fetch('/api/move-forward', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Failed to move forward');
        }

        const state = await response.json();
        updateUI(state);
    } catch (error) {
        console.error('Error:', error);
        alert('Error moving forward');
    }
}

/**
 * Handle turn right action
 */
async function handleTurnRight() {
    try {
        const response = await fetch('/api/turn-right', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Failed to turn right');
        }

        const state = await response.json();
        updateUI(state);
    } catch (error) {
        console.error('Error:', error);
        alert('Error turning right');
    }
}

/**
 * Handle reset action
 */
async function handleReset() {
    try {
        const response = await fetch('/api/reset', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Failed to reset');
        }

        const state = await response.json();
        updateUI(state);
    } catch (error) {
        console.error('Error:', error);
        alert('Error resetting game');
    }
}

/**
 * Update UI with new state
 * @param {Object} state - Game state object containing grid and roomba info
 */
function updateUI(state) {
    const roomba = state.roomba;
    const grid = state.grid;

    // Remove all roomba classes from cells
    document.querySelectorAll('.grid td.roomba.active').forEach(cell => {
        cell.classList.remove('roomba', 'active');
        cell.innerHTML = '';
    });

    // Update position
    posXSpan.textContent = roomba.x;
    posYSpan.textContent = roomba.y;

    // Update direction
    directionSpan.textContent = directionNames[roomba.direction];

    // Update roomba cell
    const newCell = document.getElementById(`cell-${roomba.x}-${roomba.y}`);
    if (newCell) {
        newCell.classList.add('roomba', 'active');
        
        // Create direction indicator
        const indicator = document.createElement('div');
        indicator.className = 'roomba-indicator';
        indicator.innerHTML = `<span>${directionArrows[roomba.direction]}</span>`;
        newCell.appendChild(indicator);
    }
}

/**
 * Initialize the game on page load
 */
document.addEventListener('DOMContentLoaded', function() {
    console.log('Robot Mover Simulator loaded');
    // UI is already initialized with server-rendered template
});

from flask import Flask, render_template, jsonify, request
from controllers.app_controller import AppController

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Initialize the app controller
controller = AppController()


@app.route('/')
def index():
    """Render the main page."""
    state = controller.get_state()
    return render_template('index.html', 
                         grid=state['grid'],
                         roomba=state['roomba'])


@app.route('/api/move-forward', methods=['POST'])
def api_move_forward():
    """API endpoint for moving the roomba forward."""
    state = controller.move_forward()
    return jsonify(state)


@app.route('/api/turn-right', methods=['POST'])
def api_turn_right():
    """API endpoint for turning the roomba right."""
    state = controller.turn_right()
    return jsonify(state)


@app.route('/api/reset', methods=['POST'])
def api_reset():
    """API endpoint for resetting the game."""
    state = controller.reset()
    return jsonify(state)


@app.route('/api/state', methods=['GET'])
def api_state():
    """API endpoint for getting the current state."""
    state = controller.get_state()
    return jsonify(state)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

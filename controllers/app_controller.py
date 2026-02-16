from models import Grid, Roomba, Direction


class AppController:
    """Controller managing the game state and logic."""

    def __init__(self):
        """Initialize the application controller."""
        self.grid = Grid(width=10, height=10)
        # Start at (1, 1) to avoid starting on boundary walls
        self.roomba = Roomba(x=1, y=1, direction=Direction.NORTH)

    def move_forward(self):
        """
        Execute move forward command.

        Returns:
            dict: Updated game state
        """
        self.roomba.move_forward(self.grid)
        return self.get_state()

    def turn_right(self):
        """
        Execute turn right command.

        Returns:
            dict: Updated game state
        """
        self.roomba.turn_right()
        return self.get_state()

    def reset(self):
        """
        Reset the game to initial state.

        Returns:
            dict: Reset game state
        """
        self.roomba = Roomba(x=1, y=1, direction=Direction.NORTH)
        return self.get_state()

    def get_state(self):
        """
        Get the current game state.

        Returns:
            dict: Current state with grid and roomba information
        """
        return {
            "grid": self.grid.to_dict(),
            "roomba": self.roomba.to_dict()
        }

from .direction import Direction
from .position import Position


class Roomba:
    """Represents the roomba robot."""

    def __init__(self, x=0, y=0, direction=Direction.NORTH):
        """
        Initialize a roomba at a specific position with a direction.

        Args:
            x (int): Starting X coordinate (default: 0)
            y (int): Starting Y coordinate (default: 0)
            direction (Direction): Starting direction (default: NORTH)
        """
        self.x = x
        self.y = y
        self.direction = direction

    def get_next_position(self, grid):
        """
        Get the next position the roomba would move to.

        Args:
            grid (Grid): The grid to check against

        Returns:
            Position: The next position, or None if next position is a wall
        """
        dx, dy = self.direction.get_vector()
        next_x = self.x + dx
        next_y = self.y + dy

        # Check if next position is valid
        if grid.is_within_bounds(next_x, next_y) and not grid.is_wall(next_x, next_y):
            return Position(next_x, next_y)
        return None

    def move_forward(self, grid):
        """
        Move the roomba forward if possible, otherwise turn right.

        Args:
            grid (Grid): The grid to check against

        Returns:
            bool: True if moved forward, False if turned right instead
        """
        next_pos = self.get_next_position(grid)
        
        if next_pos is not None:
            # Move forward
            self.x = next_pos.x
            self.y = next_pos.y
            return True
        else:
            # Turn right instead of moving
            self.turn_right()
            return False

    def turn_right(self):
        """Turn the roomba 90 degrees to the right."""
        self.direction = self.direction.turn_right()

    def get_position(self):
        """Get the current position."""
        return Position(self.x, self.y)

    def to_dict(self):
        """Convert roomba to dictionary for serialization."""
        return {
            "x": self.x,
            "y": self.y,
            "direction": self.direction.to_string()
        }

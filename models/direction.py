from enum import Enum


class Direction(Enum):
    """Enumeration for roomba direction."""
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def turn_right(self):
        """Return the direction after turning right."""
        return Direction((self.value + 1) % 4)

    def to_string(self):
        """Convert direction to string representation."""
        return self.name

    @staticmethod
    def from_string(s):
        """Convert string to Direction."""
        return Direction[s.upper()]

    def get_vector(self):
        """
        Get the (dx, dy) vector for this direction.
        Returns tuple (dx, dy) where:
        - dx: change in x coordinate
        - dy: change in y coordinate (y increases downward in grid)
        """
        vectors = {
            Direction.NORTH: (0, -1),
            Direction.EAST: (1, 0),
            Direction.SOUTH: (0, 1),
            Direction.WEST: (-1, 0),
        }
        return vectors[self]

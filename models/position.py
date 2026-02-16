class Position:
    """Represents a position on the grid."""

    def __init__(self, x, y):
        """
        Initialize a position.

        Args:
            x (int): X coordinate
            y (int): Y coordinate
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Check equality with another position."""
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """String representation of position."""
        return f"Position({self.x}, {self.y})"

    def to_dict(self):
        """Convert position to dictionary."""
        return {"x": self.x, "y": self.y}

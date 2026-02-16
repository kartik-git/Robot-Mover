class Cell:
    """Represents a single cell in the grid."""

    def __init__(self, x, y, is_wall=False):
        """
        Initialize a cell.

        Args:
            x (int): X coordinate of the cell
            y (int): Y coordinate of the cell
            is_wall (bool): Whether this cell is a wall
        """
        self.x = x
        self.y = y
        self.is_wall = is_wall

    def to_dict(self):
        """Convert cell to dictionary."""
        return {"x": self.x, "y": self.y, "isWall": self.is_wall}


class Grid:
    """Represents the grid for the roomba to move on."""

    def __init__(self, width=10, height=10):
        """
        Initialize a grid with walls on the boundaries.

        Args:
            width (int): Width of the grid (default: 10)
            height (int): Height of the grid (default: 10)
        """
        self.width = width
        self.height = height
        self.cells = self._create_grid()

    def _create_grid(self):
        """Create a 2D grid of cells with walls on boundaries."""
        cells = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Mark cells on the boundary as walls
                is_wall = (x == 0 or x == self.width - 1 or 
                          y == 0 or y == self.height - 1)
                row.append(Cell(x, y, is_wall))
            cells.append(row)
        return cells

    def is_within_bounds(self, x, y):
        """
        Check if a position is within grid bounds.

        Args:
            x (int): X coordinate
            y (int): Y coordinate

        Returns:
            bool: True if within bounds, False otherwise
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def is_wall(self, x, y):
        """
        Check if a position contains a wall.

        Args:
            x (int): X coordinate
            y (int): Y coordinate

        Returns:
            bool: True if it's a wall, False otherwise
        """
        if not self.is_within_bounds(x, y):
            return True  # Treat out-of-bounds as walls
        return self.cells[y][x].is_wall

    def get_cell(self, x, y):
        """
        Get a cell at a specific position.

        Args:
            x (int): X coordinate
            y (int): Y coordinate

        Returns:
            Cell: The cell at the position, or None if out of bounds
        """
        if not self.is_within_bounds(x, y):
            return None
        return self.cells[y][x]

    def to_dict(self):
        """Convert grid to dictionary for serialization."""
        return {
            "width": self.width,
            "height": self.height,
            "cells": [[cell.to_dict() for cell in row] for row in self.cells]
        }

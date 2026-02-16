"""
Test suite for Robot Mover models
"""
import sys
sys.path.insert(0, '.')

from models import Direction, Position, Grid, Cell, Roomba
from controllers.app_controller import AppController


def test_direction():
    """Test Direction enum and rotation."""
    print("Testing Direction...")
    assert Direction.NORTH.turn_right() == Direction.EAST
    assert Direction.EAST.turn_right() == Direction.SOUTH
    assert Direction.SOUTH.turn_right() == Direction.WEST
    assert Direction.WEST.turn_right() == Direction.NORTH
    print("✓ Direction rotation works correctly")


def test_position():
    """Test Position class."""
    print("\nTesting Position...")
    pos1 = Position(5, 5)
    pos2 = Position(5, 5)
    pos3 = Position(6, 5)
    assert pos1 == pos2
    assert pos1 != pos3
    print("✓ Position equality works correctly")


def test_grid():
    """Test Grid class."""
    print("\nTesting Grid...")
    grid = Grid(10, 10)
    
    # Test boundaries are walls
    assert grid.is_wall(0, 0), "Top-left corner should be wall"
    assert grid.is_wall(9, 9), "Bottom-right corner should be wall"
    assert grid.is_wall(0, 5), "Left edge should be wall"
    assert grid.is_wall(9, 5), "Right edge should be wall"
    
    # Test center is not wall
    assert not grid.is_wall(5, 5), "Center should not be wall"
    
    # Test bounds checking
    assert grid.is_within_bounds(0, 0)
    assert grid.is_within_bounds(9, 9)
    assert not grid.is_within_bounds(-1, 5)
    assert not grid.is_within_bounds(10, 5)
    
    print("✓ Grid boundaries work correctly")


def test_roomba_movement():
    """Test Roomba movement."""
    print("\nTesting Roomba movement...")
    grid = Grid(10, 10)
    roomba = Roomba(5, 5, Direction.NORTH)
    
    # Move forward (should move north/up)
    assert roomba.move_forward(grid) == True
    assert roomba.x == 5 and roomba.y == 4, f"Expected (5, 4), got ({roomba.x}, {roomba.y})"
    
    # Turn right (should now face east)
    roomba.turn_right()
    assert roomba.direction == Direction.EAST
    
    # Move forward (should move east/right)
    assert roomba.move_forward(grid) == True
    assert roomba.x == 6 and roomba.y == 4
    
    print("✓ Roomba movement works correctly")


def test_roomba_wall_collision():
    """Test Roomba collision with walls."""
    print("\nTesting Roomba wall collision...")
    grid = Grid(10, 10)
    roomba = Roomba(1, 1, Direction.WEST)
    
    # Try to move into wall (should turn right instead)
    initial_pos = (roomba.x, roomba.y)
    assert roomba.move_forward(grid) == False  # Collision
    assert (roomba.x, roomba.y) == initial_pos, "Position should not change on collision"
    assert roomba.direction == Direction.NORTH, "Should turn right to face NORTH"
    
    print("✓ Roomba wall collision detection works correctly")


def test_roomba_edge_collision():
    """Test Roomba collision with grid edge."""
    print("\nTesting Roomba edge collision...")
    grid = Grid(10, 10)
    # Position at (5, 2) facing up, so only 2 cells until wall at y=0
    roomba = Roomba(5, 2, Direction.NORTH)
    
    # First move towards edge - should work (moving from 2 to 1)
    assert roomba.move_forward(grid) == True
    assert roomba.x == 5 and roomba.y == 1
    
    # Second move towards edge - should fail (can't move from 1 to 0 because 0 is wall)
    # This will turn right instead
    assert roomba.move_forward(grid) == False
    assert roomba.direction == Direction.EAST
    assert roomba.x == 5 and roomba.y == 1, "Position should not change on collision"
    
    print("✓ Roomba edge collision works correctly")


def test_app_controller():
    """Test AppController."""
    print("\nTesting AppController...")
    controller = AppController()
    
    # Initial state - should be at (1, 1) facing NORTH
    state = controller.get_state()
    assert state['roomba']['x'] == 1
    assert state['roomba']['y'] == 1
    assert state['roomba']['direction'] == 'NORTH'
    
    # Move forward from (1, 1) facing NORTH - position (1, 0) is a wall, so should turn right
    state = controller.move_forward()
    assert state['roomba']['direction'] == 'EAST'
    assert state['roomba']['x'] == 1 and state['roomba']['y'] == 1  # No movement
    
    # Now facing EAST, move forward should work (moving from (1,1) to (2,1))
    state = controller.move_forward()
    assert state['roomba']['x'] == 2  # Moved east
    assert state['roomba']['y'] == 1
    
    # Turn right to face SOUTH
    state = controller.turn_right()
    assert state['roomba']['direction'] == 'SOUTH'
    
    # Reset back to initial position
    state = controller.reset()
    assert state['roomba']['x'] == 1
    assert state['roomba']['y'] == 1
    assert state['roomba']['direction'] == 'NORTH'
    
    print("✓ AppController works correctly")


if __name__ == '__main__':
    print("=" * 50)
    print("Robot Mover Test Suite")
    print("=" * 50)
    
    test_direction()
    test_position()
    test_grid()
    test_roomba_movement()
    test_roomba_wall_collision()
    test_roomba_edge_collision()
    test_app_controller()
    
    print("\n" + "=" * 50)
    print("✓ All tests passed!")
    print("=" * 50)

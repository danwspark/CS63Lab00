########################################
# CS63: Artificial Intelligence, Lab 1
# Spring 2016, Swarthmore College
########################################

# Unicode characters used for displaying the Maze
EMPTY = u"\u25A1"; WALL = u"\u25A0"

class Maze:
    """Represents the state space of a maze search problem."""    
    def __init__(self, rows, cols, walls):
        """
        rows: integer number of rows in the maze
        cols: integer number of columns in the maze
        walls: list of (row, col) pairs indicating non-empty maze cells.
        """
        self.rows = rows
        self.cols = cols
        self.walls = set(map(tuple, walls)) #set gives O(1) lookup
        self.start = (0,0) #top-left corner
        self.goal = (rows - 1, cols - 1) #bottom-right corner

    def is_wall(self, state):
        """Returns True if the cell is a wall; False otherwise."""
        return state in self.walls

    def neighbors(self, state):
        """Gives a list of orthogonal neighbors within the maze boundaries.
        Returns a list of up to four (row, col) pairs.
        """
        row, col = state
        n = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
        return filter(lambda s: self._in_range(s), n)

    def _in_range(self, state):
        """Helper method for neighbors(). Checks that a cell is in the maze."""
        row, col = state
        if row < 0 or row >= self.rows:
            return False
        if col < 0 or col >= self.cols:
            return False
        return True

    def display(self):
        """Prints a unicode representation of the maze."""
        rep = u""
        for r in range(self.rows):
            for c in range(self.cols):
                rep += self._display_char((r,c)) + " "
            rep += "\n"
        print rep

    def _display_char(self, state):
        """Helper function for display()."""
        if self.is_wall(state):
            return WALL
        else:
            return EMPTY


#! /usr/bin/env python

########################################
# CS63: Artificial Intelligence, Lab 1
# Spring 2016, Swarthmore College
########################################
# full name: WanSeo "Daniel" Park
# username: wpark1
########################################

from MazeClass import Maze
from Queues import FIFO_Queue, LIFO_Queue, Random_Queue

#TODO: add aditional Python library imports here
import getopt
import sys

# Unicode characters used for displaying the SearchAgent
#EMPTY = u"\u25A1"; WALL = u"\u25A0"; UNKNOWN = " "; PATH = "*"
EMPTY = "E"; WALL = "W"; UNKNOWN = " "; PATH = "*"
#UP = u"\u25B5"; DOWN = u"\u25BF"; LEFT = u"\u25C3"; RIGHT = u"\u25B9"
UP = "U"; DOWN = "D" ; LEFT = "L"; RIGHT = "R"

def main(bread):
    maze, mode = read_input()
    print "maze:"
    maze.display()

    agent = SearchAgent(maze, mode)
    agent.search()

    path = agent.path_to(maze.goal)
    if len(path) == 0:
        print "no path found\n"
    else:
        print "path of length", len(path), "found:"
        agent.display_path()

    print len(agent.walls) + len(agent.free), "states visited:"
    agent.display_parents()


def read_input():
    """Checks for valid command line input.
    On invalid input, prints usage instructions.
    On valid input, reads the input file and initializes a Maze object.
    Returns:
        maze: a Maze object initialized according to the input file
        mode: the search method to be used
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h", ["help"])

    except getopt.GetoptError:
        print "Error: Flag undefined.\nExiting.."######################
        exit(1)

    if len(sys.argv) != 3:
        print "Error: Incorrect number of inputs. \
                \nusage: ./MazeSearch.py maze_file.txt {BFS,DFS,RND} \
                \nExiting.."
        exit(1)
    try:
        ofile = open(str(args[0]),"r")
                
    except IOError:
        print "Error: File name is no good. Cannot open: "+ args[0]
        print "Exiting..\n"
        exit(1)
        
    row = int(ofile.readline().strip())
    col = int(ofile.readline().strip())
    rl = ofile.readline()
    walls = []
    while rl != '':
        temp = rl.strip().split()
        walls.append((int(temp[0]),int(temp[1]))) #Talk about ugly...
        rl= ofile.readline()

    maze = Maze(row,col,walls)

    if args[1] not in ['BFS', 'DFS', 'RND']:
        print "Error: Search Mode not recognized.\
         \nusage: .MazeSearch.py maze_file.txt {BFS,DFS,RND} \
            \nExiting.."
        exit(1)
    return maze, args[1]


class SearchAgent:
    """Core class for this assignment.
    Stores a MazeClass.Maze instance and the results of searching that maze.
    After a SearchAgent is initialized, the search() method should be run to
    look for start-->goal paths in the maze. The display methods will then
    show information about the search results."""
    def __init__(self, maze, mode):
        """
        Inputs:
            maze: a MazeClass.Maze instance
            mode: one of "BFS", "DFS", or "RND"
        """
        self.mz = maze #just made a new, shorter name. 
        self.free = {}
        self.parents = {}
        self.walls = {}
        self.start = maze.start
        self.end = maze.goal

        if mode == "DFS":
            self.frontier = LIFO_Queue()

        elif mode == "BFS":
            self.frontier = FIFO_Queue()

        elif mode == "RND":
            self.frontier = Random_Queue()

    def search(self):
        """Searches from start until it reaches goal or proves that it can't.
        On return, all visited states will appear in self.walls or self.free,
        and self.parents will reflect how each visited state was reached. The
        type of queue used to store the frontier determines which states are
        visited in which order.
        search() takes no inputs and has no return value.
        """
        #thank you for the pseudocode!
        self.frontier.add(self.start)
        self.parents[self.start] = None

        while len(self.frontier) != 0:
            self.curr = self.frontier.get()
            if self.mz.is_wall(self.curr):
                self.walls[self.curr] = None

            else:
                self.free[self.curr] = None
                if self.curr == self.end:
                    return

                for i in self.mz.neighbors(self.curr):
                    if i not in self.parents:
                        self.parents[i] = self.curr
                        self.frontier.add(i)


    def path_to(self, state):
        """Returns a list of (row, col) pairs along a path from start-->state.
        Should only be called after search(). If state has not been reached,
        an empty list is returned.
        """
        ret = []
        if self.curr != self.end:
            return ret

        #follows trace from end to start, bc curr is at the end
        self.trace = self.curr
        while self.trace!= self.start:
            ret.append(self.trace)
            self.trace= self.parents[self.trace]
        ret.append(self.trace)            
        return ret


    def display_path(self):
        """Prints the maze with a path from start-->goal if one was found.
        Should only be called after search()."""
        rep = u""
        path = self.path_to(self.mz.goal)
        for r in range(self.mz.rows):
            for c in range(self.mz.cols):
                rep += self._path_char((r,c), path) + " "
            rep += "\n"
        print rep

    def _path_char(self, state, path):
        """Helper function for display_path()."""
        if state in path:
            return PATH
        return self.mz._display_char(self.curr)
        
    def display_parents(self):
        """Prints a representation of the agent's knowledge of the maze.
        Should be called after search(). Visited free cells are represented by
        an arrow pointing in the direction of their parent. Unvisited cells
        are displayed as blanks."""
        rep = u""
        for r in range(self.mz.rows):
            for c in range(self.mz.cols):
                rep += self._parent_char((r,c)) + " "
            rep += "\n"
        print rep

    def _parent_char(self, state):
        """Helper function for display_parents()."""
        if state == self.mz.start:
            return EMPTY
        if state in self.walls:
            return WALL
        if state in self.free:
            p = self.parents[state]
            if p[0] < state[0]:
                return UP
            if p[0] > state[0]:
                return DOWN
            if p[1] < state[1]:
                return LEFT
            if p[1] > state[1]:
                return RIGHT
        return UNKNOWN


if __name__ == "__main__":
    main(sys.argv[1:])

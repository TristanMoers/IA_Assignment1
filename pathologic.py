# -*-coding: utf-8 -*
'''NAMES OF THE AUTHOR(S): GaÃ«l Aglin <gael.aglin@uclouvain.be>, Francois Aubry <francois.aubry@uclouvain.be>'''
from search import *
import time


#################
# Problem class #
#################
class Pathologic(Problem):

    def successor(self, state):
        # We list all actions possibles for player (move up, down, left, right)
        actions = list()
        xplayer = state.x
        yplayer = state.y
        
        # Firstly we check if player is not on border of the grid to avoid array out exception
        # Secondly we check if case (below, above, to left, to right) is not a wall
        # It's mean that the case is walkable so we create a new grid with modified cases
        # Next we add this move with a new state keeping new player position and new grid
        # If at new position it was a circle the counter is incremented 

        #UP
        if yplayer > 0:
            if state.grid[yplayer - 1][xplayer] != '1' and state.grid[yplayer - 1][xplayer] != 'x':
                newgrid = [x[:] for x in state.grid]
                newgrid[yplayer - 1][xplayer] = '$'
                newgrid[yplayer][xplayer] = 'x'
                if state.grid[yplayer - 1][xplayer] == '_':
                    actions.append(('up', State(newgrid, xplayer, yplayer - 1, state.counter + 1)))
                else:
                    actions.append(('up', State(newgrid, xplayer, yplayer - 1, state.counter)))

        #LEFT
        if xplayer > 0:
            if state.grid[yplayer][xplayer - 1] != '1' and state.grid[yplayer][xplayer - 1] != 'x':
                newgrid = [x[:] for x in state.grid]
                newgrid[yplayer][xplayer - 1] = '$'
                newgrid[yplayer][xplayer] = 'x'
                if state.grid[yplayer][xplayer - 1] == '_':
                    actions.append(('left', State(newgrid, xplayer - 1, yplayer, state.counter + 1)))
                else:
                    actions.append(('left', State(newgrid, xplayer - 1, yplayer, state.counter)))

        #DOWN
        if yplayer < state.nbr - 1:
            if state.grid[yplayer + 1][xplayer] != '1' and state.grid[yplayer + 1][xplayer] != 'x':
                newgrid = [x[:] for x in state.grid]
                newgrid[yplayer + 1][xplayer] = '$'
                newgrid[yplayer][xplayer] = 'x'
                if state.grid[yplayer + 1][xplayer] == '_':
                    actions.append(('down', State(newgrid, xplayer, yplayer + 1, state.counter + 1)))
                else:
                    actions.append(('down', State(newgrid, xplayer, yplayer + 1, state.counter)))

        #RIGHT
        if xplayer < state.nbc - 1:
            if(state.grid[yplayer][xplayer + 1] != '1' and state.grid[yplayer][xplayer + 1] != 'x'):
                newgrid = [x[:] for x in state.grid]
                newgrid[yplayer][xplayer + 1] = '$'
                newgrid[yplayer][xplayer] = 'x'
                if state.grid[yplayer][xplayer + 1] == '_':
                    actions.append(('right', State(newgrid, xplayer + 1, yplayer, state.counter + 1)))
                else:
                    actions.append(('right', State(newgrid, xplayer + 1, yplayer, state.counter)))


        for a in actions:
            yield a


    # The goal is when the number of circle equals the counter of actual state
    # It's mean that all circle is taked
    def goal_test(self, state):
        return self.goal == state.counter



###############
# State class #
###############

# State has position of player (x,y) and counter whish is incremented each time
# When player take circle  
class State:
    def __init__(self, grid, x, y, counter):
        self.nbr = len(grid)
        self.nbc = len(grid[0])
        self.grid = grid
        self.x = x
        self.y = y
        self.counter = counter

    def __str__(self):
        s = ""
        for i in range(0, self.nbr):
            for j in range(0, self.nbc):
                s = s + str(self.grid[i][j]) + " "
            s = s.rstrip()
            if i < self.nbr - 1:
                s = s + '\n'
        return s



######################
# Auxiliary function #
######################
def readInstanceFile(filename):
    lines = [line.replace(" ","").rstrip('\n') for line in open(filename)]
    n = len(lines)
    m = len(lines[0])
    grid_init = [[lines[i][j] for j in range(0, m)] for i in range(0, n)]
    return grid_init


#####################
# Launch the search #
#####################

grid_init = readInstanceFile(sys.argv[1])


# ========== Search player position and goals in grid ==========

# We keep position of player and count the number of circle in grid
# To know the goal
xplayer = 0
yplayer = 0
goal = 0

for y in range(0, len(grid_init)):
    for x in range(0, len(grid_init[y])):
        if grid_init[y][x] == '$':
            xplayer = x
            yplayer = y
        if grid_init[y][x] == '_':
            goal = goal+1

# ============================================================


init_state = State(grid_init, xplayer, yplayer, 0)

problem = Pathologic(init_state)
problem.goal = goal

# example of bfs graph search
start_time = time.time()


# ================= Differents search =========================
# DFSg
node = depth_first_graph_search(problem)

# BFSg
#node = breadth_first_graph_search(problem)

# DFSt
#node = depth_first_tree_search(problem)

# BFSt
#node = breadth_first_tree_search(problem)

# ==============================================================


# example of print
path = node.path()
path.reverse()
end_time = time.time()



print('Number of moves: ' + str(node.depth))
for n in path:
    print(n.state)  # assuming that the __str__ function of state outputs the correct format
    print()

#print("Finished in %.2f seconds" % (end_time - start_time))
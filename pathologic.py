# -*-coding: utf-8 -*
'''NAMES OF THE AUTHOR(S): Gaël Aglin <gael.aglin@uclouvain.be>, Francois Aubry <francois.aubry@uclouvain.be>'''
from search import *
import time


#################
# Problem class #
#################
class Pathologic(Problem):

    def successor(self, state):
        actions = list()
        xb = state.x
        yb = state.y
        #newgrid = [x[:] for x in state.grid]

        ########
        #UP
        if(yb>0 and state.grid[yb-1][xb] != '1' and state.grid[yb-1][xb] != 'x'):
            newgrid = [x[:] for x in state.grid]
            newgrid[yb-1][xb] = '$'
            newgrid[yb][xb] = 'x'
            if state.grid[yb-1][xb] == '_':
                actions.append(('up', State(newgrid, xb, yb-1, state.counter+1)))
            else:
                actions.append(('up', State(newgrid, xb, yb-1, state.counter)))

        #DOWN
        if(yb<state.nbc-1 and state.grid[yb+1][xb] != '1' and state.grid[yb+1][xb] != 'x'):
            newgrid = [x[:] for x in state.grid]
            newgrid[yb+1][xb] = '$'
            newgrid[yb][xb] = 'x'
            if state.grid[yb+1][xb] == '_':
                actions.append(('down', State(newgrid, xb, yb+1, state.counter+1)))
            else:
                actions.append(('down', State(newgrid, xb, yb+1, state.counter)))

        #LEFT
        if(xb>0 and state.grid[yb][xb-1] != '1' and state.grid[yb][xb-1] != 'x'):
            newgrid = [x[:] for x in state.grid]
            newgrid[yb][xb-1] = '$'
            newgrid[yb][xb] = 'x'
            if state.grid[yb][xb-1] == '_':
                actions.append(('left', State(newgrid, xb-1, yb, state.counter+1)))
            else:
                actions.append(('left', State(newgrid, xb-1, yb, state.counter)))

        #RIGHT
        if(xb<state.nbr-1 and state.grid[yb][xb+1] != '1' and state.grid[yb][xb+1] != 'x'):
            newgrid = [x[:] for x in state.grid]
            newgrid[yb][xb+1] = '$'
            newgrid[yb][xb] = 'x'
            if state.grid[yb][xb+1] == '_':
                actions.append(('right', State(newgrid, xb+1, yb, state.counter+1)))
            else:
                actions.append(('right', State(newgrid, xb+1, yb, state.counter)))


        for a in actions:
            yield a


    def goal_test(self, state):
        return self.goal == state.counter



###############
# State class #
###############

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

# ========== Search $ in grid ==========
xb = 0
yb = 0
goal = 0

for y in range(0, len(grid_init)):
    for x in range(0, len(grid_init[y])):
        if grid_init[y][x] == '$':
            xb = x
            yb = y
        if grid_init[y][x] == '_':
            goal = goal+1

# ======================================

init_state = State(grid_init, xb, yb, 0)

problem = Pathologic(init_state)
problem.goal = goal

# example of bfs graph search
start_time = time.time()
node = breadth_first_graph_search(problem)

# example of print
path = node.path()
path.reverse()
end_time = time.time()



print('Number of moves: ' + str(node.depth))
for n in path:
    print(n.state)  # assuming that the __str__ function of state outputs the correct format
    print()

print("Finished in %.2f seconds" % (end_time - start_time))
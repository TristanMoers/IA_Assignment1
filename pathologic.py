# -*-coding: utf-8 -*
'''NAMES OF THE AUTHOR(S): Gaël Aglin <gael.aglin@uclouvain.be>, Francois Aubry <francois.aubry@uclouvain.be>'''
from search import *


#################
# Problem class #
#################
class Pathologic(Problem):

    def successor(self, state):
        actions = list()
        xb = state.x
        yb = state.y

        ########

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

for x in range(0, len(grid_init)):
    for y in range(0, len(grid_init[x])):
        if grid_init[x][y] == '$':
            xb = x
            yb = y
        if grid_init[x][y] == '_':
            goal = goal+1

# ======================================

init_state = State(grid_init, xb, yb, 0)

problem = Pathologic(init_state)
problem.goal = goal

# example of bfs graph search
node = breadth_first_graph_search(problem)

# example of print
path = node.path()
path.reverse()



print('Number of moves: ' + str(node.depth))
for n in path:
    print(n.state)  # assuming that the __str__ function of state outputs the correct format
    print()
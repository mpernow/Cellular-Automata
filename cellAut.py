import numpy as np
import matplotlib.pyplot as plt

class CellAut():
    """
    Cellular automaton class
    """
    def __init__(self, neighbours=3, size=15):
        """
        Initialises the cellular automaton class.
        neighbours is the total number of cells checked at each update.
        size is the number of cells in each iteration.
        """
        if neighbours%2 != 1:
            raise ValueError("Only odd length allowed")
        self.neighbours = neighbours
        self.rule = np.random.choice([0,1], 2**self.neighbours).astype(int)
        self.size = 15
        self.pattern = []

    def set_rule(self, rule):
        """
        Sets the update rule to a given array.
        Should be a list of zeroes and ones of length 2**neighbours.
        Use convention of Wolfram.
        """
        if len(rule) != 2**self.neighbours:
            raise ValueError("Rule must be of length 2**neighbours")
        if not all(x == 0 or x == 1 for x in rule):
            raise ValueError("Rule must contain only 0s or 1s")
        self.rule = rule

    def set_size(self, size):
        """
        Sets the number of cells in each iteration.
        """
        self.size = size

    def run(self, num=None, init=None):
        """
        Runs the cellular automaton for num iterations.
        """
        if num == None:
            num = self.size
        self.pattern = np.zeros((num,self.size)).astype(int)
        if init == None:
            self.pattern[0] = np.random.choice([0,1], self.size).astype(int)
        else:
            if len(init) != self.size:
                raise ValueError("Initial generation of incorrect size")
            self.pattern[0] = init
        for age in range(num-1):
            for cell in range(self.size):
                this_gen = self.pattern[age]
                indices = [cell - int((self.neighbours-1)/2) + i for i in range(self.neighbours)]
                for i in range(len(indices)):
                    if indices[i] >= self.size:
                        indices[i] = indices[i] - self.size
                neighbour_vals = [this_gen[ind] for ind in indices]
                current = ''.join(str(e) for e in neighbour_vals)
                rule_ind = 2**self.neighbours - 1 - int(current, 2) # Wolfram convention for rule
                self.pattern[age+1][cell] = self.rule[rule_ind]

    def disp(self):
        """
        Plot the cellular automaton.
        """
        fig = plt.imshow(self.pattern, cmap='Greys',  interpolation='nearest')
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        return fig

    def __str__(self):
        """
        For printing.
        """
        if len(self.pattern) == 0:
            return "Cellular automaton has not run yet."
        else:
            return np.array_str(self.pattern)

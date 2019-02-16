import numpy as np
import cellAut as ca
import matplotlib.pyplot as plt

plt.close("all")

#Wolfram's rule30
rule30 = [0, 0, 0, 1, 1, 1, 1, 0]
rule110 = [0, 1, 1, 1, 1, 0, 0, 0]
rule = np.random.choice([0,1],8).astype(int)

my_ca = ca.CellAut(3)
my_ca.set_rule(rule30)

size = 200
init_arr = np.zeros(size)
init_arr[int(size/2)]=1
#init_arr[int(size/4)]=1
#init_arr[int(3*size/4)]=1
my_ca.set_size(size)
my_ca.run(num=200)
#my_ca.run(num=200,init=list(init_arr))
myplot = my_ca.disp()

plt.show(myplot)

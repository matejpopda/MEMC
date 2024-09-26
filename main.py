import util
import generators
import numpy as np
import matplotlib.pyplot as plot



a = generators.congruent_period(1,2**16,75)

for i in range(10):
    print(a.get_float())




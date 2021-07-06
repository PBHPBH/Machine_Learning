from numpy import arange
from scipy.optimize import curve_fit
from matplotlib import pyplot
import random

a = random.randint(1, 6)

# define the true objective function
def objective(x, a, b, c):
    return a * x ** 2 + b * x + c

# x,y 값 지정
xy = [[-2.9,35.4],[-2.1,19.7],[-0.9,5.7],[1.1,2.1],[0.1,1.2],[1.9,8.7],[3.1,25.7],[4.0,41.5]]

xy_1 = random.sample(xy, 6)
xy_2 = random.sample(xy, 6)

x= [xy_1[0][0],xy_1[1][0],xy_1[2][0],xy_1[3][0],xy_1[4][0],xy_1[5][0]]
y= [xy_1[0][1],xy_1[1][1],xy_1[2][1],xy_1[3][1],xy_1[4][1],xy_1[5][1]]

x2= [xy_2[0][0],xy_2[1][0],xy_2[2][0],xy_2[3][0],xy_2[4][0],xy_2[5][0]]
y2= [xy_2[0][1],xy_2[1][1],xy_2[2][1],xy_2[3][1],xy_2[4][1],xy_2[5][1]]

popt, _ = curve_fit(objective, x, y)
popt2,ty = curve_fit(objective, x2, y2)
# summarize the parameter values
a, b, c = popt
a1, b1, c1 = popt2
print('y = %f * x^2 + %f * x+ %f' % (a, b, c))
print('y = %f * x^2 + %f * x+ %f' % (a1, b1, c1))


# graph plotting
pyplot.scatter(x, y)
pyplot.scatter(x2, y2)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(-3, 4, 1)

# calculate the output for the range
y_line = objective(x_line, a, b, c)
y2_line = objective(x_line, a1, b1, c1)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '-', color='red')
pyplot.plot(x_line, y2_line, '-', color='blue')

pyplot.show()
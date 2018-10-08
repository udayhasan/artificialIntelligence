from csv import reader
import matplotlib.pyplot as plt
import numpy as np
from numpy import array

alpha   = 1

t0_prev = 10
t1_prev = 10
J_prev  = 100

t0      = 0
t1      = 0
J       = 0

t0_err  = 0.001
t1_err  = 0.001
J_err   = 0.01

with open('regression_dataset.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    x=[]
    y=[]
    i=0
    for row in csv_reader:
        if(i!=0):
            x.append(int(row[0]))
            y.append(float(row[1]))
        else:
            plt.xlabel(row[0])
            plt.ylabel(row[1])
        i+=1
    plt.plot(x,y,'r^')
    plt.axis([0,max(x)+1, 0,max(y)+1])


def line_maker(t0_plot, t1_plot, color):
    y_final = []
    for i in range(len(x)):
        y_final.append(t0_plot + t1_plot*x[i])

    plt.plot(x,y_final, color)

"""def cost_function(t0_cur, t1_cur):
    J_cur  = (0.5 * sum([(t0_cur+t1_cur*x[j]-y[j])**2 for j in range(len(x))]))/len(x)
    t0_cur = t0_cur - alpha*((J - J_prev)/(t0_cur - t0_prev))
    t1_cur = t1_cur - alpha*((J - J_prev)/(t1_cur - t1_prev))
    
    t0_prev = t0_cur
    t1_prev = t1_cur
    J_prev  = J_cur

    return t0_cur, t1_cur, J_cur"""

i=0
while(abs(J-J_prev) > J_err):
    #t0, t1, J = cost_function(t0, t1)
    J_prev  = J
    J  = (0.5 * sum([(t0+t1*x[j]-y[j])**2 for j in range(len(x))]))/len(x)
    print(J)
    #t0 = t0 - alpha*((J - J_prev)/(t0 - t0_prev))
    #t1 = t1 - alpha*((J - J_prev)/(t1 - t1_prev))
    
    t0_prev = t0
    t1_prev = t1
    
    i += 1
print(i)
line_maker(t0, t1, 'r')
plt.show()

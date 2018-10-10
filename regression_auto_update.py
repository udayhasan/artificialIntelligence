from csv import reader
import matplotlib.pyplot as plt
import numpy as np
from numpy import array

alpha   = 0.004
max_run = 1000
J       = 10
J_prev  = 20
J_err   = 0.0001

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
    #plt.subplot(211)
    plt.axis([0,max(x)+1, 0,max(y)+1])
    plt.plot(x, y, 'r*')


t0_prev = y[1]
t1_prev = (y[1]-y[0])/(x[1]-x[0])

t0      = y[2]
t1      = (y[2]-y[1])/(x[2]-x[1])

def line_maker(t0_plot, t1_plot, color):
    y_final = []
    for i in range(len(x)):
        y_final.append(t0_plot + t1_plot*x[i])
    #plt.subplot(212)
    #plt.axis([0,max(x)+1, min(y_final), max(y_final)])
    plt.plot(x,y_final, color)

i = 0
while(abs(J-J_prev) > J_err and i < max_run):
    J_prev  = J
    J       = (0.5 * sum([(t0 + t1*x[j]-y[j])**2 for j in range(len(x))]))/len(x)
    t0_temp = t0 - alpha*((J - J_prev)/(t0 - t0_prev))
    t1_temp = t1 - alpha*((J - J_prev)/(t1 - t1_prev))

    print(t0, t1, J)

    t0_prev = t0
    t1_prev = t1

    t0      = t0_temp
    t1      = t1_temp
        
    i += 1
    
line_maker(t0, t1, 'b')
plt.show()


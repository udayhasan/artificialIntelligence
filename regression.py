from csv import reader
import matplotlib.pyplot as plt
import numpy as np
from numpy import array

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

theta0_final = []
theta1_final = []
J_final = []

def plotter(t0, t1, color):
    y_final = []
    for i in range(len(x)):
        y_final.append(t0 + t1*x[i])

    plt.plot(x,y_final, color)

for k in np.linspace(int(min(y)), int(max(y)), len(y)):
    J = []
    theta1 = []
    for i in np.linspace(0,1,len(x)):
        theta1.append(i)
        s = 0
        for j in range(len(x)):
            h=k+i*x[j]
            s += (h-y[j])**2
        J.append(1/(2*len(x))*s)
        
        J_final.append(J[J.index(min(J))])
        theta1_final.append(theta1[J.index(min(J))])
        theta0_final.append(k)
        
    plotter(k,theta1[J.index(min(J))], 'bo')

plotter(theta0_final[J_final.index(min(J_final))],theta1_final[J_final.index(min(J_final))], 'g')

plt.plot(x,y,'r^')
plt.axis([0,max(x)+1, 0,max(y)+1])

plt.show()

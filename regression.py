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

theta0_no = 100
theta1_min = -10
theta1_max = 10
theta1_no = 100

theta0_final = []
theta1_final = []
J_final = []

def line_maker(t0, t1, color):
    y_final = []
    for i in range(len(x)):
        y_final.append(t0 + t1*x[i])

    plt.plot(x,y_final, color)

def rectifier(theta0_temp1, theta1_temp1, J_temp1):
    theta0_final.append(theta0_temp1)
    theta1_final.append(theta1_temp1)
    J_final.append(J_temp1)

def cost_function():
    theta0_temp = []
    theta1_temp = []
    J_temp = []
    for k in np.linspace(int(min(y))-10, int(max(y))+10, theta0_no):
        J = []
        theta1 = []
        
        for i in np.linspace(theta1_min, theta1_max, theta1_no):
            e = sum([(k+i*x[j]-y[j])**2 for j in range(len(x))])
            J.append(0.5*e/len(x))
            theta1.append(i)

        J_temp.append(min(J))
        theta1_temp.append(theta1[J.index(min(J))])
        theta0_temp.append(k)

    rectifier(theta0_temp,theta1_temp,J_temp)
            

#Making the cost function (J)
cost_function()
print(min(theta1_final))

#ploting J vs theta1 graph
plt.plot(theta1_final, J_final, 'b--o')
plt.axis([0,max(theta1_final)+1, 0,max(J_final)+1])

#Regression Straight Line
#line_maker(theta0_final[J_final.index(min(J_final))],theta1_final[J_final.index(min(J_final))], 'g')

#Plotting original values
#plt.plot(x,y,'r^')
#plt.axis([0,max(x)+1, 0,max(y)+1])

plt.show()

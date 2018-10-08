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
        #else:
            #plt.xlabel(row[0])
            #plt.ylabel(row[1])
        i+=1
        
theta0_min = min(y)-13.5
theta0_max = max(y)+10
theta0_no = 100

theta1_min = -10
theta1_max = 100
theta1_no = 1000

theta0_final = []
theta1_final = []
J_final = []

def line_maker(t0, t1, color):
    y_final = []
    for i in range(len(x)):
        y_final.append(t0 + t1*x[i])

    plt.plot(x,y_final, color)

def rectifier(theta0_temp1, theta1_temp1, J_temp1):
    for i in range(0, len(theta1_temp1)):
        if(theta1_temp1[i] not in theta1_final):
            theta0_final.append(theta0_temp1[i])
            theta1_final.append(theta1_temp1[i])
            J_final.append(J_temp1[i])

def cost_function():
    theta0_temp = []
    theta1_temp = []
    J_temp = []
    for k in np.linspace(theta0_min, theta0_max, theta0_no):
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
print(min(J_final))

#ploting J vs theta1 graph
plt.plot(theta1_final, J_final, 'b--o')
plt.axis([min(theta1_final)-1,max(theta1_final)+1, 0,max(J_final)+1])
plt.xlabel('Theta1')
plt.ylabel('Cost Function (J)')

#Regression Straight Line
#line_maker(theta0_final[J_final.index(min(J_final))],theta1_final[J_final.index(min(J_final))], 'g')

#Plotting original values
#plt.plot(x,y,'r^')
#plt.axis([0,max(x)+1, 0,max(y)+1])

plt.show()
plt.show()


from csv import reader
import matplotlib.pyplot as plt
from numpy import array

with open('regression_dataset.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    x=[]
    y=[]
    for row in csv_reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
    plt.plot(x,y,'r^')
    plt.axis([0,max(x)+1, 0,max(y)+1])
    plt.show()

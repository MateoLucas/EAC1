import matplotlib.pyplot as plt
import numpy as np

#Develve una matriz de numpy donde la primera colmna es el valor de clientes(int)
#y la segunda columna es la fecha(string) en el orden en el que vienen del 
#.txt (cronologico). Input es una matriz con las tres columnas con los tres 
#valores en formato int. No lo devuelve.
def entrada():
    input = np.loadtxt("cinearnuevosusuarios.txt", dtype='i')
    data = np.zeros((len(input),2),dtype=object)
    for i in range(0,len(input)):     
        data[i][0] = input[i][2]
        data[i][1] = str(input[i][0]) + '/' +  str(input[i][1])
    return data
    
def item_a(data):
    y = np.array(data[:,0])
    x = np.array(data[:,1])
    plt.figure(figsize=(20,5))
    plt.bar(x,y,width = 0.8)
    plt.xticks(rotation = 'vertical')
    plt.show()
    


        
def main(): 
    data =entrada()
    item_a(data)
main()


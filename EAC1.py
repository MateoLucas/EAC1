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

def test_data():
    #data para probar el correto funcionamiento del programa
    #no apto pra
    test_data = np.matrix([[1067, 'a'],
                 [919, 'b'],
                 [1196,'c'],
                 [785,'d'],
                 [1126,'e'],
                 [936,'f'],
                 [918,'g'],
                 [1156,'h'],
                 [920,'i'],
                 [948,'j']],dtype=object)
    return test_data

'''Item a) Debieron haber una gran cantidad de nuevos suscriptores en el primer mes
porque es el primer mes de opeación de la plataforma. Toda a quellas personas que
estaban esperando para usarla, y todas las personas que mas interesadas podrian estar
se debieron subscribir apenas se enteraron que estaba habilitado. Luego mes a mes
las personas menos atentas o que no estaban aun convencidas se fueron anotando
a un ritmo mas distribuido.''' 
def item_a(data):
    y = np.array(data[:,0])
    x = np.array(data[:,1])
    plt.figure(figsize=(20,5))
    plt.bar(x,y,width = 0.8)
    plt.xticks(rotation = 'vertical')
    plt.show()
    

def item_b(data):
    #mediana
    med_arr = np.array(data[:,0])
    med_arr = np.sort(med_arr,axis = None)
    if(len(med_arr)%2 == 0):
        #caso de que haya una cantidad par de elementos
        mediana = (med_arr[int(len(med_arr)/2)]+med_arr[(int(len(med_arr)/2)-1)])/2
    elif(len(med_arr)%2 == 1):
        #caso de que haya una cantidad impar de elementos
        mediana = med_arr[(int((len(med_arr)-1)/2))]
    else:
        print("Error al calcular mediana.")
    print("Mediana: " + str(mediana))
    #promedio
    prom_arr = np.array(data[:,0])
    promedio = 0
    for i in range(0,len(prom_arr)):
        promedio += prom_arr[i]
    promedio = promedio/len(prom_arr)
    print("Proemdio: " + str(promedio))
    #desviacioin estandard
    desv_arr = np.array(data[:,0])
    desv = 0
    for i in range(0,len(desv_arr)):
        desv += abs(promedio - desv_arr[i])
    desv = desv/len(desv_arr)
    print("Desvio estandard: " + str(desv))
        
def main(): 
    #data =entrada()
    data =test_data() #no apta para item a
    #item_a(data)
    item_b(data)
main()


import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) # Here you put the input data
saidas = np.array([0,0,0,1]) # This is the data you expect to output
pesos = np.array([0.0, 0.0]) # Here are the data weights, you can set an initial value
taxaAprendizagem = 0.1 # Here is the learning rate of the neuron, you can also change

def stepFunction(soma): # For the data output I chose, I defined the step function
    if (soma >=1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
                print('Total de erros: ' + str(erroTotal))
                
treinar()
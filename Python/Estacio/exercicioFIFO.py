#PT: Este exercicio será um exemplo de estrutura de dados FIFO com lista
#EN: This exercise will be an example of data structure FIFO using arrays

from time import sleep

fifo = [] #FIFO array

for i in range (10): # loop method
    fifo.insert(0, i) # enqueuing
    print('entrada ->', fifo)
    sleep(0.5)

for i in range (9, 0, -1): # loop method
    print(fifo, '-> saída') # Showing the queue before doing anything
    fifo.pop() # dequeuing
    sleep(0.5)

print(fifo, '-> saída') # showing the last iten enqueued
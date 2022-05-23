#PT: Este exercicio será um exemplo de estrutura de dados FIFO em POO
#EN: This exercise will be an example of data structure FIFO using OOP

from time import sleep

class Fifo: # 
    def __init__(self): # method thats gonna make the array object
        self.dados = [] 
    
    def inserir(self, elemento): # method to insert itens into the array
        self.dados.insert(0, elemento) # the insert method from python to make an insert method. lol

    def remover(self): # method to remove the last iten from the array
        self.dados.pop() # the remove method from pythons library to make a remove method. agaain -.-

    def vazio(self): # method to test if the array is empty
        return len(self.dados) == 0 # the same as the other methods
    
fifo = Fifo() # instantiating the array object

print('lista vazia? ->', fifo.vazio()) # verifying if the array is empty
sleep(1)

# FROM NOW ON IS THE SAME AS THE OTHER DATA STRUCTURE EXERCISES. PICK ONE AND HAVE FUN :)
for count in range(10):
    fifo.inserir(count)
    print('entrada ->', fifo.dados)
    sleep(0.5)

print('lista vazia? ->', fifo.vazio())
sleep(1)
print('Agora veja que os itens serão desinfileirados a partir do 1º item adicionado (o numero 0)')
sleep(5)

for count in range(9, 0, -1):
    print(fifo.dados, '-> saída')
    fifo.remover()
    sleep(0.5)

print(fifo.dados, '-> saída')
fifo.remover()
sleep(1)
print('lista vazia? ->', fifo.vazio())

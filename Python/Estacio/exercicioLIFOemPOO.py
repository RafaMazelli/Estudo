#PT: Este exercicio será um exemplo de estrutura de dados LIFO em POO
#EN: This exercise will be an example of data structure LIFO using OOP

from time import sleep

class Lifo: # class that will be used to make a LIFO array
    def __init__(self): 
        self.dados = [] # telling the class that we're gonna create an array

    def inserir(self, elemento): # method that inserts itens to the array
        self.dados.insert(0, elemento) #using the insert method to make another insert method. lol

    def remover(self): # the removing method
        self.dados.pop(0) # also using a removing method to make another removing method

    def vazio(self):
        return len(self.dados) == 0

teste = Lifo() # creating an array object

#From now on is all the same as the last exercise: LIFO with arrays. Not gonna write all over again. sorry :/

print('Lista vazia? -> ', teste.vazio())
sleep(2)

for i in range(10):
    teste.inserir(i)
    print('Entrada ->', teste.dados)
    sleep(0.5)

sleep(1)

print('Agora repare que o último item (o numero 9) a entrar na pilha será o primeiro a sair.')
sleep(4)

for count in range(9, 0, -1):
    print('Saída <-', teste.dados)
    teste.remover()
    sleep(0.5)

print('Saída <-', teste.dados)
print('Lista vazia? -> ', teste.vazio())
sleep(5)

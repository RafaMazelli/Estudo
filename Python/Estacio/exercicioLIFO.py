#PT: Este exercicio será um exemplo de estrutura de dados LIFO usando um array
#EN: This exercise will be an example of data structure LIFO using array

from time import sleep

lifo = [] # the array that will be used for the exercise

for count in range(10): #making a counting loop
    lifo.append(count) # adding something to the array. I took advantage from the counting to do so
    print(lifo) #printing the array
    sleep(0.5) #taking a breath xD

sleep(1) 
print ('Agora perceba que o ultimo item será o primeiro a sair.')
sleep(2)

for count in range(9, 0, -1): #Making a reverse counting loop
    print(lifo) #here i had to print before removing anything
    lifo.pop(count) #removing the iten. also took advantage from the counting loop to do so
    sleep(0.5)

print(lifo) #had to show one last time because the for looping checks the parameters before executing the code. I could also use the do while loop, but im at the crazy life style. lol
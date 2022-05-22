produto = int(input('\33[32mQual o preço do produto?\33[m\n'))
print('-='*50)
print(f'\33[32mO valor do produto com 5% de desconto é de \33[36mR${produto-(5/100*produto):.2f}')

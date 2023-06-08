def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    if number % 2 != 0:
        print(3*number+1)
        return 3*number+1
# Conjectura de collatz
try:
    op = int(input("Digite um número\n"))
    while op != 1:
        op = collatz(op)  
except ValueError:
    print('Forneça um número inteiro!')
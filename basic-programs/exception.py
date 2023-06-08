def spam(divideBy):
    return 42 / divideBy

try:    
    print(spam(2))
    print(spam(12))
    print(spam(0)) # Erro
    print(spam(1))
except:
    print('Error: Invalid argument.')

# Os erros podem ser tratados com instruções try e except. O código que pode
# conter um erro em potencial é inserido em uma cláusula try. A execução do
# programa segue para o início da cláusula except seguinte caso um erro ocorra.
# Podemos colocar o código anterior de divisão por zero em uma cláusula try
# e fazer com que uma cláusula except contenha um código para lidar com o
# que acontece quando esse erro ocorrer.

# Quando um código em uma cláusula try provocar um erro, a execução do
# programa será transferida imediatamente para o código na cláusula except.
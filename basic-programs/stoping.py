import sys

# O programa contém um loop infinito sem uma instrução break. A única maneira desse
# programa terminar será o usuário digitar Sair, fazendo sys.exit() ser chamado.

while True:
    response = input ("Digite \"Sair\" para sair.\n")
    if response == "Sair":
        sys.exit()
    print("\nVocê digitou \""+response+"\"\n")
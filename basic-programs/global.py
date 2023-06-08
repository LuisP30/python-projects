# INSTRUÇÃO GLOBAL

def spam():
    global eggs
    eggs = "spam"

eggs = "global"
spam()
# Quando spam() é chamada o valor da variável global eggs se torna "spam"
print(eggs)

# Como eggs é declarada como global no início de spam(), 
# quando eggs é definida com 'spam', essa atribuição	
# é	feita ao eggs do escopo global. Nenhuma	variável local eggs será criada.
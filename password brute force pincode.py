import time

# Fazer como um array para facilitar

print('Escolha uma senha de 9 digitos númericos com todos diferentes entre si')

password = int(input())

while (password < 123456789 | password > 987654321):
    aux = str(password)
    def split(word):
        return [char for char in word]
    x = split(aux)
    print(type(x))
    if len(x) > len(set(x)):
        pass
    else:
        print('Escolha uma senha de 9 digitos númericos com todos diferentes entre si')
        password = int(input())

print('Tentaremos obter sua senha com FORÇA BRUTA e verificaremos se ela é forte (concluiremos que não)')

def bruteforce():
    n = 0
    while n != password:
       n += 1
    return n

start = time.time()
senha = bruteforce()
end = time.time()
print('A senha do usuario é ' + str(senha))
tempo = (end-start)
print('O tempo demorado para obter foi '+ str(tempo) + 's')
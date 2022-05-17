import time
import numpy as np

print('Escolha uma senha de 4 a 9 digitos númericos com todos diferentes entre si')

password = int(input())
nonDuplicate = False

while (password < 1234 or nonDuplicate == False):
    aux = str(password)
    def split(word):
        return [char for char in word]
    x = split(aux)
    y = np.array(x)
    z = []
    for i in y:
        if i not in z:
            z.append(i)

    if len(z) == len(y):
        nonDuplicate = True
    else:
        print('Senha não adequada. Escolha uma senha de 9 digitos númericos com todos diferentes entre si')
        password = int(input()) 
    if (password < 1234 and nonDuplicate == True):
        print('Senha não adequada. Escolha uma senha de 9 digitos númericos com todos diferentes entre si')
        password = int(input())

print('Tentaremos obter sua senha com FORÇA BRUTA e verificaremos se ela é forte (concluiremos que não)')

def bruteforce():
    n = 1234
    while n != password:
       n += 1
    return n

start = time.time()
senha = bruteforce()
end = time.time()
print('A senha do usuario é ' + str(senha))
tempo = (end-start)
print('O tempo demorado para obter foi '+ str(tempo) + 's')
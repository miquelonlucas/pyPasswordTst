import time

password = -1

print('Escolha uma senha de seis dígitos NUMÉRICA: ')
password = int(input())

while (password < 0 | password > 999999):
    print('Escolha uma senha de quatro dígitos NUMÉRICA: ')
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
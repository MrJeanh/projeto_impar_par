import funcoes as f
"""
Este programa solicita números do usuário,
e verifica se o número digitado é ímpar ou par.
Exemplo: 5 = 5 é Ímpar.
"""

def main():
    numero = int(input('Digite um número: '))
    print(f.impar_par(numero))
main()
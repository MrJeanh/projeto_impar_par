def impar_par(numero: int) -> str:
    '''Verifica se um número é par ou ímpar.'''
    if numero % 2 == 0:
        return f'{numero} é Par'
    else:
        return f'{numero} é Ímpar'

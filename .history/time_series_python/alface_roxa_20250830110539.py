"""
==================================================
Script Name : alface_roxa.py.py
Author      : Alessandra
Date        : 2025-08-30
Description : Funções com decorators e wrappers
Usage       : 
Dependencies: 
Python ver. : 3
==================================================
"""

####### Sobre Decorators...
# segue exercício: 

# oque é um python decorator?
#uma função que muda o comportamento de outra função, sem modificar a mesma.

# Crie um decorator com parâmetro: @repete(n) 
# Requisitos:
# - Executa a função "n" vezes
# - Retorna o resultado da última execução
# - Use @wraps na função interna

from functools import wraps

def repete(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resultado = 0
            for _ in range(n):
                i = func(*args, **kwargs)                
                return i
                return wrapper
            return decorator
        
        @repete(3)
        def diga_oi(nome):
            print(f'oi: {nome}')
            return f'oi: {nome}'
        
        i = diga_oi('Ana')
        print(i)

    raise NotImplementedError

# Crie um decorator simples de tempo de execução
# Requisitos:
# - Use @wraps para preservar __name__ e __doc__
# - Meça o tempo com time.perf_counter()
# - Printee: "func <nome> levou <segundos:.3f>s"
import time
from functools import wraps

def tempo_execucao():
        @wraps(func)
        def wrapper(*args, **kwargs):
             inicio = time.perf_counter()
             r = func(*args, **kwars)
             fim = time.perf_counter()

             print(f'func{time.perf_counter()}')
             return r
        return wrapper
        
        
    raise NotImplementedError


#  Funções-alvo para decorar 
def soma_lenta(a, b):
    """Soma após meio segundo"""
    time.sleep(0.5)
    return a + b

def diga_oi(nome):
    return f"Oi, {nome}!"


#  Aplique seus decorators (após implementar)
# Ex.: @tempo_execucao
#      def soma_lenta(...):
#          ...

# Ex.: @repete(3)
#      def diga_oi(...):
#          ...

"""
==================================================
Script Name : alface_roxa.py.py
Author      : Alessandra
Date        : 2025-08-30
Description : Funções com decorators e wrappers
Usage       : Decorators: Usados para mudar o comportamento de uma função sem alterar a mesma.
Usados nos exercicios para 
Dependencies: 
Python ver. : 3
==================================================
"""

# Sobre Decorators...

# oque é um python decorator?
#uma função que muda o comportamento de outra função, sem modificar a mesma.

# Crie um decorator com parâmetro: @repete(n) 
# Requisitos:
# - Executa a função "n" vezes
# - Retorna o resultado da última execução
# - Use @wraps na função interna

from functools import wraps
import time

def repete(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs): #args: valor ex 1, kwargs: chave-valor ex nome:Ana
            i = None
            for _ in range(n):
                i = func(*args, **kwargs)                
            return i
        return wrapper
    return decorator

# Crie um decorator simples de tempo de execução
# Requisitos:
# - Use @wraps para preservar __name__ e __doc__
# - Meça o tempo com time.perf_counter()
# - Printee: "func <nome> levou <segundos:.3f>s"

def tempo_execucao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
             inicio = time.perf_counter()
             r = func(*args, **kwargs)
             fim = time.perf_counter()
             print(f'func{func.__name__} levou {fim - inicio:.3f}s')
             return r
    return wrapper
        
#  Funções-alvo para decorar 
@tempo_execucao
def soma_lenta(a, b):
     """Soma após meio segundo"""
     time.sleep(0.5)
     return a + b

@repete(3)
def diga_oi(nome):
    return f"Oi, {nome}!"

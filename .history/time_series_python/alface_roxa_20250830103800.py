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
def repete(n):
    def original(func):
        def wrapper():
            i = n
            for in range(1, 6):
                print(i = i.length)

def

    raise NotImplementedError

# Crie um decorator simples de tempo de execução
# Requisitos:
# - Use @wraps para preservar __name__ e __doc__
# - Meça o tempo com time.perf_counter()
# - Printee: "func <nome> levou <segundos:.3f>s"
def tempo_execucao(func):
    # implementar
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

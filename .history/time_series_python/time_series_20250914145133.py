def media_movel_ultima_serie(serie, janela=3):
    """
    Recebe uma lista de floats `serie` e retorna a previsão do próximo valor
    usando a média móvel dos últimos `janela` elementos.
    """
    if len(serie) < janela:
        # Se a série for menor que a janela, usa a média de tudo
        return sum(serie) / len(serie)
    else:
        return sum(serie[-janela:]) / janela

serie = [3.0, 5.0, 7.0, 6.0, 8.0]
previsao = media_movel_ultima_serie(serie, janela=3)
print(f"Próximo valor previsto: {previsao}")

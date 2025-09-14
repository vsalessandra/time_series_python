def media_movel_ultima_serie(serie, janela=3):
do a média móvel dos últimos `janela` elementos.
    """
    if len(serie) < janela:
        return sum(serie) / len(serie)
    else:
        return sum(serie[-janela:]) / janela

serie = [3.0, 5.0, 7.0, 6.0, 8.0]
previsao = media_movel_ultima_serie(serie, janela=3)
print(f"Próximo valor previsto: {previsao}")

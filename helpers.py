import requests
from config import URL_BASE_TOP_HEADLINES, URL_BASE_EVERYTHING, CHAVE_API

def top_noticias(pais, fonte=None, categoria=None, pesquisa=None):
    """
    Retorna as top noticias do site newsapi.org
    :param pais: requerido - ex: br
    :param fonte: opcional - ex: globo
    :param categoria: opcional - ex: 'technology'
    :param pesquisa: opcional - ex: bolsonaro
    :return: lista de top notícias
    """

    if fonte:
        url = f"{URL_BASE_TOP_HEADLINES}sources={fonte}&apiKey={CHAVE_API}"
    elif categoria:
        url = f"{URL_BASE_TOP_HEADLINES}country={pais}&category={categoria}&apiKey={CHAVE_API}"
    elif pesquisa:
        url = f"{URL_BASE_TOP_HEADLINES}country={pais}&q={pesquisa}&apiKey={CHAVE_API}"
    else:
        url = f"{URL_BASE_TOP_HEADLINES}country={pais}&apiKey={CHAVE_API}"

    #coleta os dados informados em json
    resposta = requests.get(url).json()

    #pegando todos os artigos
    artigos = resposta['articles']
    
    # lista vazia para preencher com os dados
    top_noticias = []

    for artigo in artigos:
        top_noticias.append(f"Autor: {artigo['author']}, "
                                  f"Titulo: {artigo['title']}, "
                                  f"Descrição: {artigo['description']}, "
                                  f"URL: {artigo['url']}, "
                                  f"URLTOIMAGE: {artigo['urlToImage']}, "
                                  f"publicado em: {artigo['publishedAt']}, "
                                  f"conteudo: {artigo['content']}")

    return top_noticias
    #print(resposta)

def todas_noticias(pesquisa, lingua=None, fr=None, to=None):
    """
    retorna todas as noticias do site newsapi
    """
    todas_noticias = []

    if pesquisa:
        if lingua and fr == '' or to == '':
            url = f"{URL_BASE_EVERYTHING}q={pesquisa}&language={lingua}&apiKey={CHAVE_API}"
        elif fr or to and lingua:
            url = f"{URL_BASE_EVERYTHING}q={pesquisa}&language={lingua}&from={fr}&to={to}&apiKey={CHAVE_API}"
        else:
            url = f"{URL_BASE_EVERYTHING}q={pesquisa}&apiKey={CHAVE_API}"

    #coletando em formato json
    resposta = requests.get(url).json()
    artigos = resposta['articles']

    for artigo in artigos:
        todas_noticias.append(f"Autor: {artigo['author']}, "
                                    f"Titulo: {artigo['title']}, "
                                    f"Descrição: {artigo['description']}, "
                                    f"URL: {artigo['url']}, "
                                    f"URLTOIMAGE: {artigo['urlToImage']}, "
                                    f"publicado em: {artigo['publishedAt']}, "
                                    f"conteudo: {artigo['content']}")

    return todas_noticias
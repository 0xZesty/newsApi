from helpers import top_noticias, todas_noticias
print("===COLETOR NOTÍCIAS VIA API - NEWSAPI.ORG===\n")
print("Favor, insira as informações solicitadas abaixo")
pais = input("Insira o país da notícia (br, us, de, etc): ")
pesquisa = input("Insira o que pesquisar (palavra ou frase): ")
fonte = input("Insira a fonte (globo, blasting-news-br, google-news-br): ")
categoria = input("Insira a categoria (business, entertainment, general, health, science, sports, technology): ")
lingua = input('insira o idioma da pesquisa (pt, en): ')
fro = input('insira a data da pesquisa pesquisa inicial (2020-10-11): ')
to = input('insira a data da pesquisa final (2020-10-11): ')

noticias = top_noticias(pais, pesquisa=pesquisa, fonte=fonte, categoria=categoria)

print(f" **** Listando as Top Notícias do País - {pais.upper()} ****")
if noticias:
    for numero in range(len(noticias)):
        print(f"{numero + 1} - {noticias[numero]}")
else:
    print("Não encontrei notícias com as opções informadas!")


print('\n')
print('\n')

todas_not = todas_noticias(pesquisa, lingua=lingua, fr=fro, to=to)

print(f" **** Listando Todas As Notícias sobre - {pesquisa.upper()} ****")
if todas_not:
    for numero in range(len(todas_not)):
        print(f"{numero + 1} - {todas_not[numero]}")
else:
    print("Não encontrei notícias com as opções informadas!")
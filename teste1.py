import os

PASTA_DADOS = os.path.join(os.path.dirname(__file__), "dados")
ARQUIVO = os.path.join(PASTA_DADOS, "dados_teste.txt")

print("=" * 80)
print("Teste com arquivos de dados")

print("__file__ = {}".format(__file__))
print("os.getcwd() = {}".format(os.getcwd()))
print("Nome completo do arquivo: {}".format(ARQUIVO))
 
with open(ARQUIVO) as f:
    # # Forma 1 - readline - 1 linha por vez
    # texto = None
    # while texto != '':
    #     texto = f.readline() 
    #     print("texto lido = '{}'".format("".join(texto)))

    # # Forma 2 - read() - le o arquivo inteiro para 1 string
    # print("texto lido = '{}'".format(f.read()))

    # Forma 3 - list - retorna uma lista com 1 linha por elemento da lista
    lines = f.readlines()
    header = lines[0]
    print("header = {}".format(header))
    for line in lines[1:]:
        print("line = {}".format(line))
        ativo = line[13:24]
        preco_medio = line[96:108]
        print("ativo = {} preco_medio = {}".format(ativo, preco_medio))


print("*" * 80)

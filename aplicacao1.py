
import argparse
import os 
from carregador_dados import le_arquivo 

def main(args):
    print("=" * 80)
    print("Teste com arquivos de dados")

    print("Nome completo do arquivo: {}".format(args.input_file))

    gerador_arquivo = le_arquivo(args.input_file)
    print("header = {}".format(next(gerador_arquivo)))
    print("-" * 80)

    for data_pregao, ativo, preco_medio in gerador_arquivo:
        print("data_pregao = {} ativo = {} preco_medio = {}".format(
            data_pregao, ativo, preco_medio))

    print("*" * 80)


def parse_args():
    # Exemplo de uso 
    # python3 teste2.py --input-file dados/COTAHIST_A2020.TXT  
    PASTA_DADOS = os.path.join(os.path.dirname(__file__), "dados")
    ARQUIVO_DEFAULT = os.path.join(PASTA_DADOS, "dados_teste.txt")
    parser = argparse.ArgumentParser(description='Carregador de dados')
    parser.add_argument('-i', '--input-file', type=str,
                        default=ARQUIVO_DEFAULT)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)


import argparse
import os 
from carregador_dados import le_arquivo 
import numpy as np

def main(args): 
    gerador_arquivo = le_arquivo(args.input_file, pula_header=True) 

    dados = np.array(list(gerador_arquivo))
    precos_medios = dados[:, 2] # seleciona todas as linhas, coluna 2 (preco_medio)
    
    print("media de precos = {} desvio padrao = {} variancia = {}".format(
        np.mean(precos_medios), np.std(precos_medios), np.var(precos_medios)))


def parse_args():
    # Exemplo de uso 
    # python3 teste2.py --input-file dados/COTAHIST_A2020.TXT  
    PASTA_DADOS = os.path.join(os.path.dirname(__file__), "dados")
    ARQUIVO_DEFAULT = os.path.join(PASTA_DADOS, "dados_teste.txt")
    parser = argparse.ArgumentParser(description='Carregador de dados')
    parser.add_argument('-i', '--input-file', type=str,
                        default=ARQUIVO_DEFAULT)
    parser.add_argument('--ativo', type=str,
                        default='ALPA4', help="filtra pelo ativo informado")                    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)


import argparse
import os 
from carregador_dados import le_arquivo 

def main(args): 
    gerador_arquivo = le_arquivo(args.input_file, pula_header=True) 

    n_vezes = 0
    total = 0
    for _, ativo, preco_medio in gerador_arquivo:
        if ativo == args.ativo:
            n_vezes += 1
            total += preco_medio

    print("O ativo {} apareceu {} vezes e a media eh {}".format(
        args.ativo, n_vezes, total / n_vezes)) 


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

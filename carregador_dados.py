from datetime import datetime


def le_arquivo(path_arquivo, pula_header=False):
    with open(path_arquivo) as f:
        header = f.readline().strip()
        if not pula_header:
            yield header
        while True:
            line = f.readline()
            if line == '' or line == '\n' or line.startswith("99COTAHIST"):
                break
            data_pregao = datetime.strptime(line[2:10], "%Y%m%d").date()
            ativo = line[12:24].strip()
            preco_medio = float("{}.{}".format(line[95:106], line[106:108]))
            yield data_pregao, ativo, preco_medio

import pdfplumber
import text
import nome_arquivo

def Mercado_Vista(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_Texto(num_page)
        
        vista_acoes = row[9].split()
        vista_ouro = row[10].split()
        vista_outro = row[11].split()
        mercado_vista = {
            "Mercado à vista": {
                "Operações comuns": vista_acoes[-2],
                "Day-Trade": vista_acoes[-1]
            },
            "Mercado à vista - ouro": {
                "Operações comuns": vista_ouro[-2],
                "Day-Trade": vista_ouro[-1]
            },
            "Mercado à vista - outro at. fin. fora bolsa": {
                "Operações comuns": vista_outro[-2],
                "Day-Trade": vista_outro[-1]
            }
        }
        return mercado_vista

def Mercado_Opcoes(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_Texto(num_page)
        
        opcoes_acoes = row[13].split()
        opcoes_ouro = row[14].split()
        opcoes_fora_bolsa = row[15].split()
        opcoes_outros = row[16].split()
        mercado_opcoes = {
            "Mercado opções - ações": {
                "Operações comuns": opcoes_acoes[-2],
                "Day-Trade": opcoes_acoes[-1]
            },
            "Mercado opções - ouro": {
                "Operações comuns": opcoes_ouro[-2],
                "Day-Trade": opcoes_ouro[-1]
            },
            "Mercado opções - fora bolsa": {
                "Operações comuns": opcoes_fora_bolsa[-2],
                "Day-Trade": opcoes_fora_bolsa[-1]
            },
            "Mercado opções - outros": {
                "Operações comuns": opcoes_outros[-2],
                "Day-Trade": opcoes_outros[-1]
            }
        }
        return mercado_opcoes
    
def Mercado_Futuro(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_Texto(num_page)
        
        futuro_dolar = row[18].split()
        futuro_indices = row[19].split()
        futuro_juros = row[20].split()
        futuro_outros = row[21].split()
        mercado_futuro = {
            "Mercado à vista - dólar dos EUA": {
                "Operações comuns": futuro_dolar[-2],
                "Day-Trade": futuro_dolar[-1]
            },
            "Mercado à vista - índices": {
                "Operações comuns": futuro_indices[-2],
                "Day-Trade": futuro_indices[-1]
            },
            "Mercado à vista - juros": {
                "Operações comuns": futuro_juros[-2],
                "Day-Trade": futuro_juros[-1]
            },
            "Mercado à vista - outros": {
                "Operações comuns": futuro_outros[-2],
                "Day-Trade": futuro_outros[-1]
            }
        }
        return mercado_futuro
    
import pdfplumber
import nome_arquivo

def Resumo_Financeiro():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_financeira = page.crop((307, 400, page.width, 660))
    
        financeiro = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [308, 500, 564, 574],
            "explicit_horizontal_lines": [
                440, 450, 460, 470, 478, 486, 496, 506, 516, 524, 532,
                542, 552, 560, 570, 580, #alterações aqui
                598, 608, 615, 625, 635
            ]
        }
        Resumo_financeiro = coluna_financeira.extract_table(financeiro) 
        
        obj_bolsa = {
            "titulo": Resumo_financeiro[5][0],
            Resumo_financeiro[6][0]: {
                "Valor": Resumo_financeiro[6][2],
                "DC": Resumo_financeiro[6][3]
            },
            Resumo_financeiro[7][0]: {
                "Valor": Resumo_financeiro[7][2],
                "DC": Resumo_financeiro[7][3]
            },
            Resumo_financeiro[8][0]: {
                "Valor": Resumo_financeiro[8][2],
                "DC": Resumo_financeiro[8][3]
            },
            "Total_Bovespa_Soma": {
                "Valor": Resumo_financeiro[9][2],
                "DC": Resumo_financeiro[9][3]
            }
        }
        
        obj_Corretagem = {
            "Titulo": Resumo_financeiro[10][0],
            "Corretagem": {
                "Valor": Resumo_financeiro[12][2],
                "DC": Resumo_financeiro[12][3]
            },
            "ISS": {
                "Valor": Resumo_financeiro[13][2],
                "DC": Resumo_financeiro[13][3]
            },
            Resumo_financeiro[14][0]: {
                "Valor": Resumo_financeiro[14][2],
                "DC": Resumo_financeiro[14][3]
            },
            "Outras": {
                "Valor": Resumo_financeiro[16][2],
                "DC": Resumo_financeiro[16][3]
            },
            "Total_corretagem_Despesas": {
                "Valor": Resumo_financeiro[17][2],
                "DC": Resumo_financeiro[17][3]
            },
            Resumo_financeiro[18][0]: {
                "Valor": Resumo_financeiro[18][2],
                "DC": Resumo_financeiro[18][3]
            },
            "Observacao": Resumo_financeiro[19][0]
        }
        
        obj_resumo_financeiro = {
            "titulo": Resumo_financeiro[0][0],
            "Valor_liquido_das_operacoes": {
                "Valor": Resumo_financeiro[1][2],
                "DC": Resumo_financeiro[1][3],
            },
            
            "Taxa_de_liquidacao": {
                "Valor": Resumo_financeiro[2][2],
                "DC": Resumo_financeiro[2][3]
            },
            
            "Taxa_de_registro": {
                "Valor": Resumo_financeiro[3][2],
                "DC": Resumo_financeiro[3][3]
            },
            
            "Total_CBLC": {
                "Valor": Resumo_financeiro[4][2],
                "DC": Resumo_financeiro[4][3]
            },
            
            "Bolsa": obj_bolsa,
            "Corretagem": obj_Corretagem
        }
        return obj_resumo_financeiro
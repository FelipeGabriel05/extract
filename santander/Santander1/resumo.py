import pdfplumber
import nome_arquivo

def Resumo():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        coluna_resumo = page.crop((296, 70, page.width, 360))
        resumo_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [301, 500, 550, 560]
        }
        table_resumo = coluna_resumo.extract_table(resumo_settings)
        
        resumo_financeiro = {
            "CBLC": {
                "Valor": table_resumo[1][-2],
                "DC": table_resumo[1][-1]
            },
            "Valor Líquido das Operacões": {
                "Valor": table_resumo[2][-2],
                "DC": table_resumo[2][-1]
            },
            "Taxa de Liquidação": {
                "Valor": table_resumo[3][-2],
                "DC": table_resumo[3][-1]
            },
            "Taxa de Registro": {
                "Valor": table_resumo[4][-2],
                "DC": table_resumo[4][-1]
            },
            "Total CBLC": {
                "Valor": table_resumo[5][-2],
                "DC": table_resumo[5][-1]
            }
        }
        
        obj_bovespa = {
            "Taxa de Termo_Opções": {
                "Valor": table_resumo[8][-2],
                "DC": table_resumo[8][-1]
            },
            "Taxa_ANA": {
                "Valor": table_resumo[9][-2],
                "DC": table_resumo[9][-1]
            },
            "Emolumentos": {
                "Valor": table_resumo[10][-2],
                "DC": table_resumo[10][-1]
            },
            "Total_Bovespa_Soma": {
                "Valor": table_resumo[11][-2],
                "DC": table_resumo[11][-1]
            }
        }

        obj_despesas = {
            table_resumo[14][0]: {
                "Valor": table_resumo[14][-2],
                "DC": table_resumo[14][-1]
            },
            table_resumo[15][0]: {
                "Valor": f"{table_resumo[15][-2]} {table_resumo[15][-1]}",
                "DC": ''
            },
            table_resumo[16][0]: {
                "Valor": f"{table_resumo[16][-2]}{table_resumo[16][-1]}",
                "DC": ''
            },
            table_resumo[17][0]: {
                "Valor": table_resumo[17][-2],
                "DC": table_resumo[17][-1]
            },
            table_resumo[18][0]: {
                "Valor": table_resumo[18][-2],
                "DC": table_resumo[18][-1]
            },
            table_resumo[19][0]: {
                "Valor": table_resumo[19][-2],
                "DC": table_resumo[19][-1]
            }
        }
        
        obj_resumos = {
            "Resumo Financeiro": resumo_financeiro,
            "BOVESPA_SOMA": obj_bovespa,
            "CORRETAGEM_Despesas": obj_despesas
        }
        return obj_resumos
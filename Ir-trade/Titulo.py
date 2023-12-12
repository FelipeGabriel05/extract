import pdfplumber
import nome_arquivo
import text

def Titulo(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_Texto(num_page)
   
        cpf_cnpj = row[4].split('CPF/CNPJ: ')
        nome = row[3].split('Nome:')
        dado_inferior = row[-1].split()
        titulo = {
            "Calendario": row[0],
            "Informe_de_rendimentos": f"{row[1]} {row[2]}",
            "Nome_Cliente": nome[-1],
            "CPF_CNPJ": cpf_cnpj[-1],
            "Internet": dado_inferior[0],
            "Numero_da_pagina": dado_inferior[-1]
        }
        return titulo
    
def Rendimentos():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        row = text.Pegar_Texto(1)
        
        coluna_table = page.crop((20, 190, page.width, 415))
        table_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [105, 310, 410, 498],
            "explicit_horizontal_lines": [190, 204, 215, 230, 245, 260, 275, 290, 305, 320, 335, 350,
        365, 380, 395, 406]
        }
        tabela_meses = coluna_table.extract_table(table_settings)
        
        i = 3
        meses_lista = []
        while i <= len(tabela_meses) - 2:
            mes = {
                "Mes": tabela_meses[i][0],
                "Total_no_mes": tabela_meses[i][2]
            }
            meses_lista.append(mes) 
            i += 1
        
        obj_vendas_isentas = {
            "Titulo_pagina": Titulo(1),
            "Nome_Nota": f"{row[5]} {row[6]}",
            "titulo_vendas": tabela_meses[0][0],
            "Cod_Lancamento": tabela_meses[1][1],
            "Total": tabela_meses[1][2],
            "total_mes" : {
                "mes1": meses_lista[0],
                "mes2": meses_lista[1],
                "mes3": meses_lista[2],
                "mes4": meses_lista[3],
                "mes5": meses_lista[4],
                "mes6": meses_lista[5],
                "mes7": meses_lista[6],
                "mes8": meses_lista[7],
                "mes9": meses_lista[8],
                "mes10": meses_lista[9],
                "mes11": meses_lista[10],
                "mes12": meses_lista[11]
            },
            row[-6]: f"{row[-4]} {row[-3]} {row[-2]}"
        }
        return obj_vendas_isentas
import pdfplumber
import nome_arquivo

def Negocios():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page1 =  pdf.pages[0]
        page2 = pdf.pages[1]
        all_text = ''
        text = page2.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        coluna_negocios = page1.crop((20, 310, page1.width, 810))
        negocios_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [33, 50, 110, 140, 210, 340, 410, 440, 470, 537, 562]
        }
        table_negocios = coluna_negocios.extract_table(negocios_settings)
        
        quantidades = row[2].split()
        num_negocio = 0
        numero_repeticao = 1
        total_negocios = {}
        
        while num_negocio <= len(table_negocios) -1:
            medio = num_negocio + 1
            
            if num_negocio == len(table_negocios) -1:
                negocio = {
                    "Q": table_negocios[num_negocio][0],
                    "Negociacao": table_negocios[num_negocio][1],
                    "CV": table_negocios[num_negocio][2],
                    "Tipo_de_mercado": table_negocios[num_negocio][3],
                    "Especificação_do_titulo": table_negocios[num_negocio][4],
                    "Quantidade": table_negocios[num_negocio][5],
                    "Preço_Ajuste": table_negocios[num_negocio][7],
                    "Valor_Ajuste": table_negocios[num_negocio][8],
                    "DC": table_negocios[num_negocio][9],
                    "Total": {
                        "Quantidade Total": quantidades[2],
                        "Preço Médio": quantidades[5]
                    }
                }
            else:
                negocio = {
                    "Q": table_negocios[num_negocio][0],
                    "Negociacao": table_negocios[num_negocio][1],
                    "CV": table_negocios[num_negocio][2],
                    "Tipo_de_mercado": table_negocios[num_negocio][3],
                    "Especificação_do_titulo": table_negocios[num_negocio][4],
                    "Quantidade": table_negocios[num_negocio][5],
                    "Preço_Ajuste": table_negocios[num_negocio][7],
                    "Valor_Ajuste": table_negocios[num_negocio][8],
                    "DC": table_negocios[num_negocio][9],
                    "Total": {
                        "Especificação_do_Titulo": table_negocios[medio][4],
                        "Quantidade Total": table_negocios[medio][6],
                        "Preço Médio": table_negocios[medio][9]
                    }
                }
        
            total_negocios[f"negocio_{numero_repeticao}"] = negocio
            num_negocio += 2
            numero_repeticao += 1
        
        return total_negocios
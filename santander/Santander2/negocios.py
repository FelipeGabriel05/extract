import pdfplumber
import nome_arquivo

def Negocio2():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        coluna_negocios = page.crop((20, 50, page.width, 75))
        negocios_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [58, 114, 135, 214, 320, 332, 390, 453, 520, 535]
        }
        table_negocios = coluna_negocios.extract_table(negocios_settings)
        obj = {
            "Negociacao": table_negocios[0][0],
            "C_V": table_negocios[0][1],
            "Tipo_de_Mercado": table_negocios[0][2],
            "Especificacao_do_Titulo": table_negocios[0][3],
            "obs_asterisco": table_negocios[0][4],
            "Quantidade": table_negocios[0][5],
            "Preco_Ajuste": table_negocios[0][6],
            "Valor_Ajuste": table_negocios[0][7],
            "D_C": table_negocios[0][8]
        }
        return obj

def Negocio():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_negocios = page.crop((20, 330, page.width, 830))
        negocios_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [58, 114, 135, 214, 320, 332, 390, 453, 520, 535]
        }
        table_negocios = coluna_negocios.extract_table(negocios_settings)
        
        num_negociacao = 0
        total_negocios = {}
        while num_negociacao <= len(table_negocios) -2:
            negocio_num = num_negociacao + 1
            negocio = {
                "Negociacao": table_negocios[num_negociacao][0],
                "C_V": table_negocios[num_negociacao][1],
                "Tipo_de_Mercado": table_negocios[num_negociacao][2],
                "Especificacao_do_Titulo": table_negocios[num_negociacao][3],
                "obs_asterisco": table_negocios[num_negociacao][4],
                "Quantidade": table_negocios[num_negociacao][5],
                "Preco_Ajuste": table_negocios[num_negociacao][6],
                "Valor_Ajuste": table_negocios[num_negociacao][7],
                "D_C": table_negocios[num_negociacao][8]
            }
            total_negocios[f"Negocio_{negocio_num}"] = negocio
            num_negociacao += 1
        
        num_negociacao += 1
        total_negocios[f"Negocio_{num_negociacao}"] = Negocio2()
        return total_negocios
        
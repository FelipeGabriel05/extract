import pdfplumber
import nome_arquivo

def Negocios():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_negocios = page.crop((20, 245, page.width, 290))
        negocios_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [30, 50, 102, 165, 220, 280, 360, 460, 480, 555],
            "explicit_horizontal_lines": [245, 285]
        }
        table_negocios = coluna_negocios.extract_table(negocios_settings)
        total_negocios = {}
        i = 0
        num_negocio = 1
        while i <= len(table_negocios) - 1: 
            negocio = {
                "CV": table_negocios[i][0],
                "Mercadoria": table_negocios[i][1],
                "Vencimento": table_negocios[i][2],
                "Quantidade": table_negocios[i][3],
                "Preco_Ajuste": table_negocios[i][4],
                "Tipo_Do_Negocio": table_negocios[i][5],
                "Vlr_de_Operacao_Ajuste_DC": table_negocios[i][6],
                "Taxa_Operacional": table_negocios[i][7]
            }
            total_negocios[f"negocio{num_negocio}"] = negocio
            num_negocio += 1
            i += 1
        return total_negocios
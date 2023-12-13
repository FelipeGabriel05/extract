import pdfplumber
import text
import nome_arquivo

def Negocios(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[num_page]
        row = text.Pegar_texto(num_page)
        coluna_negocios = page.crop((20, 185, page.width, 418))
        
        banco = row[11].split()
        negocios_settings = {
            "vertical_strategy": "explicit",
            "explicit_vertical_lines": [44, 88, 102, 160, 265, 298, 358, 458, 540, 552]
        }
        table_negocios = coluna_negocios.extract_table(negocios_settings)
        
        if table_negocios[0][0] == banco[0]:
            i = 3
            total = len(table_negocios) - 2
        else: 
            i = 0
            total = len(table_negocios) - 2
            
        total_negocios = {}
        num_negocio = 1
        while i <= total:
            negocio = {
                "Praca": table_negocios[i][0],
                "C_V": table_negocios[i][1],
                "Tipo_Mercado": table_negocios[i][2],
                "Especificacao_de_titulos": table_negocios[i][3],
                "OBS": table_negocios[i][4],
                "Quantidade": table_negocios[i][5],
                "Preco_liquidacao": table_negocios[i][6],
                "Compra_Venda": table_negocios[i][7],
                "D_C": table_negocios[i][8],
            }
            total_negocios[f"negocio_{num_negocio}"] = negocio
            num_negocio += 1
            i += 1
        return total_negocios
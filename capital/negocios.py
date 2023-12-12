import pdfplumber
import nome_arquivo
import text

def Negocios(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[num_page]
        coluna_negocios = page.crop((10, 190, page.width, 628))
    
        negocios_settings = {
            "vertical_strategy": "explicit",
            "explicit_vertical_lines": [18, 30, 125, 220, 240, 315, 430, 510, 595]
        }
        negocios = coluna_negocios.extract_table(negocios_settings)
        i = 0
        total_negocios = {}
        num_negocio = 1
        while i <= len(negocios) - 1:
            obj_negocios = {
                "C_V": negocios[i][0],
                "Mercadoria": negocios[i][1],
                "Vencimento": negocios[i][2],
                "Quantidade": negocios[i][3],
                "Preco_Ajuste": negocios[i][4],
                "Tipo_do_negocio": negocios[i][5],
                "Vlr_de_operacao_ajuste_DC": negocios[i][6],
                "Taxa_operacional": negocios[i][7]
            }
            total_negocios[f"negocio_{num_negocio}"] = obj_negocios
            num_negocio += 1
            i += 1
        return total_negocios

def Observacoes(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_texto(num_page)
        informacoes_corretagem = {
            "info1": row[-10],
            "info2": row[-9],
            "info3": row[-8],
            "info4": row[-7],
            "info5": row[-6],
            "info6": f"{row[-5]} {row[-4]} {row[-3]}",
            "info7": f"{row[-2]} {row[-1]}"
        }
        return informacoes_corretagem
import pdfplumber
import nome_arquivo

def Negocios():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_negocios = page.crop((20, 212, page.width, 427))
        negocios_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "text",
            "explicit_vertical_lines": [40, 47, 90, 102, 180, 207, 340, 
                                            370, 430, 490, 560, 575]
        }
        tabela_negocios = coluna_negocios.extract_table(negocios_settings)
        
        i = 0
        total_negocios = {}
        num_negocio = 1
        while i <= len(tabela_negocios) - 1:
            negocio = {
                "Q": tabela_negocios[i][0],
                "Negociacao": tabela_negocios[i][1],
                "C_V": tabela_negocios[i][2],
                "Tipo_Mercado": tabela_negocios[i][3],
                "Prazo": tabela_negocios[i][4],
                "Especificacao_de_titulo": tabela_negocios[i][5],
                "OBS": tabela_negocios[i][6],
                "Quantidade": tabela_negocios[i][7],
                "Preco_Ajuste": tabela_negocios[i][8],
                "Valor_Operacao_Ajuste": tabela_negocios[i][9],
                "DC": tabela_negocios[i][10],
            }
            total_negocios[f"negocio_{num_negocio}"] = negocio
            num_negocio += 1
            i += 1
        return total_negocios
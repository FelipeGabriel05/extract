import pdfplumber
import nome_arquivo
import titulo 
import text

def Negocios():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[2]
        row = text.Pegar_Texto(2)
        coluna_bovespa = page.crop((20, 250, page.width, 320))
        bovespa_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [40, 130, 160, 200, 250, 390, 480, 540, 610, 638, 730, 800],
            "explicit_horizontal_lines": [258, 268, 285, 305, 315]
        }
        tabela_bovespa = coluna_bovespa.extract_table(bovespa_settings)
        
        total_negocios = {}
        total_increment = 0
        num_negocio = 1
        while total_increment <= len(tabela_bovespa) - 2:
            negocio = {
                "Corretora": tabela_bovespa[total_increment][0],
                "CV": tabela_bovespa[total_increment][1],
                "Grupo": tabela_bovespa[total_increment][2],
                "Codigo": tabela_bovespa[total_increment][3],
                "Empresa": tabela_bovespa[total_increment][4],
                "CNPJ": tabela_bovespa[total_increment][5],
                "Ativo": tabela_bovespa[total_increment][6],
                "Vencimento": tabela_bovespa[total_increment][7],
                "Qtd": tabela_bovespa[total_increment][8],
                "Custo_medio": tabela_bovespa[total_increment][9],
                "Total_cTaxas": tabela_bovespa[total_increment][10],
            }
            total_negocios[f"negocio_{num_negocio}"] = negocio
            num_negocio += 1
            total_increment += 1
        
        obj_bovespa = {
            "Titulo_Pagina": titulo.Titulo(2),
            "Nome_Nota": f"{row[5]} {row[6]}",
            "Sugestão de lançamento no campo Discriminação": row[8],
            "Total_negocios": total_negocios,
            "Total_de_posicao": tabela_bovespa[-1][-1]
        }
        return obj_bovespa
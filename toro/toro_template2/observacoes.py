import pdfplumber
import nome_arquivo

def Legenda():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        
        coluna_legenda = page.crop((20, 496, page.width, 650))
        legenda_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [30, 220, 450],
            "explicit_horizontal_lines": [500, 515, 525, 535, 545, 555, 565, 575, 585]
        }
        tabela_legenda = coluna_legenda.extract_table(legenda_settings)
        
        obs = {
            "dados_2": tabela_legenda[0][0],
            "dados_P": tabela_legenda[0][1],
            "dados_negocio": tabela_legenda[1][0],
            "dados_H": tabela_legenda[1][1],
            "dados_8": tabela_legenda[2][0],
            "dados_X": tabela_legenda[2][1],
            "dados_D": tabela_legenda[3][0],
            "dados_Y": tabela_legenda[3][1],
            "dados_F": tabela_legenda[4][0],
            "dados_L": tabela_legenda[4][1],
            "dados_B": tabela_legenda[5][0],
            "dados_T": tabela_legenda[5][1],
            "dados_A": tabela_legenda[6][0],
            "dados_I": tabela_legenda[6][1],
            "dados_C": tabela_legenda[7][0]
        }
        return obs
    
def Adicional():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        linha_dt = row[-11].split()
        dt_obs = row[-11].split('Especificações diversas: IRRF Day Trade: Base R$0,00 Projeção R$0,00')
        linha_oc = row[-10].split()
        obj = {
            "Especificações diversas": {
                "IRRF_Day_Trade": {
                    "Base": linha_dt[6],
                    "Projeção": linha_dt[8],
                    "obs": dt_obs[-1]
                },
                "IRRF_Operação_Comum": {
                    "Base": linha_oc[4],
                    "Projeção": linha_oc[6],
                    "obs": row[-9]
                },
                "informação_adicional": f"{row[-8]} {row[-7]} {row[-6]} {row[-5]} {row[-4]} {row[-3]} {row[-2]}"
            }
        }
        return obj
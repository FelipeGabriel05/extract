import nome_arquivo
import pdfplumber

def Num_page():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        info = row[0].split()
        info2 = row[0].split('S4')
        obj = {
            "Folha": info[0],
            "Página": info2[-1]
        }
        return obj
    
def Negociacao():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        coluna_negociacao = page.crop((20, 80, 300, 250))
        negociacao_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [55, 249, 293]
        }
        table_negociacao = coluna_negociacao.extract_table(negociacao_settings)
        especificacao = row[-14].split()
        irrf = ''
        num_caractere = 6
        while num_caractere <= len(especificacao[2]) - 1:
            irrf += f"{especificacao[2][num_caractere]}"
            num_caractere += 1
        
        negociacao = {
            "Vendas a vista": table_negociacao[1][1],
            "Compras a vista": table_negociacao[2][1],
            "Opcoes_Compra": table_negociacao[3][1],
            "Opcoes_Vendas": table_negociacao[4][1],
            "Operacoes a Termo": table_negociacao[5][1],
            "Valor das Operacoes com Titulos Publicos V_Nom": table_negociacao[6][1],
            "Valor das Operacoes": table_negociacao[7][1],
            "Especificações Diversas": {
                "IRRF_Day_Trade": irrf,
                "Projeção": especificacao[-1]
            }
        }
        return negociacao
    
def Observacao():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        coluna_obs = page.crop((20, 255, 298, 357))
        obs_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [55, 183, 293],
            "explicit_horizontal_lines": [256, 266, 280, 300, 310, 330, 340, 354]
        }
        table_obs = coluna_obs.extract_table(obs_settings)
        obs = {
            "Dados8":  table_obs[1][0],
            "Dados_D": table_obs[1][1],
            "Dados_F": table_obs[2][0],
            "Dados_B": table_obs[2][1],
            "Dados_C": table_obs[3][0],
            "Dados_A": table_obs[3][1], 
            "Dados_H": table_obs[4][0],
            "Dados_X": table_obs[4][1],
            "Dados_P": table_obs[5][0],
            "Dados_Y": table_obs[5][1],
            "Dados_L": table_obs[6][0],
            "Dados_T": table_obs[6][1],
            "obs_Operacões": f"{row[-4]} {row[-3]}"
        }
        return obs
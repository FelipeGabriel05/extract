import pdfplumber
import nome_arquivo

def extract_page():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        return row[0]

def Negociacao():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        coluna_negociacao = page.crop((20, 70, 295, 200))
        negociacao_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [35, 250, 288]
        }
        table_negociacao = coluna_negociacao.extract_table(negociacao_settings)
        obj_negociacao = {
            "Data de extração": extract_page(),
            table_negociacao[1][0]: table_negociacao[1][1],
            table_negociacao[2][0]: table_negociacao[2][1],
            table_negociacao[3][0]: table_negociacao[3][1],
            table_negociacao[4][0]: table_negociacao[4][1],
            table_negociacao[5][0]: table_negociacao[5][1],
            table_negociacao[6][0]: table_negociacao[6][1],
            table_negociacao[7][0]: table_negociacao[7][1]
        }
        return obj_negociacao
    
def Observacoes():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[1]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        coluna_obs = page.crop((20, 255, 298, 350))
        obs_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "text",
            "explicit_vertical_lines": [30, 200, 290]
        }
        table_obs = coluna_obs.extract_table(obs_settings)
        
        especificacao = row[16].split()
        day_info = row[-6].split('As operações a termo não são computadas no líquido da')
        info2 = row[-6].split('DayTrade-IR 1% na Fonte')
        observacoes_finais = {
            "Especificações Diversas": {
                "IRRF_Day_Trade": especificacao[3],
                "Projeção": especificacao[-1]
            },
            "Informações Adicionais": {
                "info1": day_info[1],
                "info2": f"{info2[0]} {row[-5]}",
                "info3": f"{row[-4]} {row[-3]} {row[-2]}",
                "Site": row[-1]
            }
        }
        
        obj_obs = {
            "Dados2": f"{table_obs[0][0]} {table_obs[1][0]}",
            "Dados_Negocios": table_obs[0][1],
            "Dados8": table_obs[3][0],
            "Dados_D": table_obs[3][1],
            "Dados_F": table_obs[5][0],
            "Dados_B": table_obs[5][1],
            "Dados_C": table_obs[7][0],
            "Dados_A": table_obs[7][1],
            "Dados_H": table_obs[9][0],
            "Dados_X": table_obs[9][1],
            "Dados_P": table_obs[11][0],
            "Dados_Y": table_obs[11][1],
            "Dados_L": table_obs[13][0],
            "Dados_T": f"{table_obs[13][1]} {table_obs[14][-1]}",
            "Observações Finais": observacoes_finais
        }
        return obj_obs
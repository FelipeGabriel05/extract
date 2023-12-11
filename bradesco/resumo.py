import pdfplumber
import nome_arquivo

def Resumo():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_resumo = page.crop((20, 400, 308, 600))
    
        resumo_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [38, 200, 307],
            "explicit_horizontal_lines": [ 440, 450, 460, 469, 479, 489, 499, 509, 519,
                                            532, 542, 562]
        }
        
        resumo_negocios = coluna_resumo.extract_table(resumo_settings)
        obj_resumo_negocios = {
            "Debentures": resumo_negocios[0][1],
            "Vendas_a_vista": resumo_negocios[1][1],
            "Compras_a_vista": resumo_negocios[2][1],
            "Opcoes_compras": resumo_negocios[3][1],
            "Opcoes_vendas": resumo_negocios[4][1],
            "Operacoes_a_termo": resumo_negocios[5][1],
            "Valor_das_operacoes_cTitulo_Vnom": resumo_negocios[6][1],
            "Valor_das_Operacoes": resumo_negocios[7][1],
            "Especificacoes_diversas": resumo_negocios[10][0],
        }
        return obj_resumo_negocios
    
def Observacao():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        coluna_obs = page.crop((20, 616, 308, 690))
        obs_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "explicit",
            "explicit_vertical_lines": [38, 152, 220, 307],
            "explicit_horizontal_lines": [616,626, 636, 646, 656, 666, 676, 686]
        }
        table_obs = coluna_obs.extract_table(obs_settings)
        obj_obs = {
            "Tipo_observacao": table_obs[0][0],
            "DadosA": table_obs[0][1],
            "DadosT": table_obs[0][2],
            "Dados2": table_obs[1][0],
            "DadosC": table_obs[1][1],
            "DadosI": table_obs[1][2],
            "DadosNegocio": table_obs[2][0],
            "DadosP": table_obs[2][1],
            "Dados8": table_obs[3][0],
            "DadosH": table_obs[3][1],
            "DadosD": table_obs[4][0],
            "DadosX": table_obs[4][1],
            "DadosF": table_obs[5][0],
            "DadosY": table_obs[5][1],
            "DadosB": table_obs[6][0],
            "DadosL": table_obs[6][1],
            "Obs_Final": f"{row[-2]} {row[-1]}"
        }
        return obj_obs
import text
import nome_arquivo
import pdfplumber

def Observacoes(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_texto(num_page)
        
        dados1 = row[-11].split()
        dados2 = row[-10].split()
        dados3 = row[-9].split()
        dados4 = row[-8].split()
        dados5 = row[-7].split()
        obs_total = 0
        nome_obs = ''
        while obs_total <= len(dados1) - 7:
            nome_obs += f"{dados1[obs_total]} "
            obs_total += 1

        obj_OBS = {
            "Dados2": nome_obs,
            "DadosB": f"{dados1[-6]} {dados1[-5]} {dados1[-4]}",
            "DadosX": f"{dados1[-3]} {dados1[-2]} {dados1[-1]}",
            "Dados_Negocio": f"{dados2[0]} {dados2[1]} {dados2[2]} {dados2[3]}",
            "DadosA": f"{dados2[4]} {dados2[5]} {dados2[6]} {dados2[7]}",
            "DadosY": f"{dados2[8]} {dados2[9]} {dados2[10]} {dados2[11]} {dados2[12]}",
            "Dados8": f"{dados3[0]} {dados3[1]} {dados3[2]} {dados3[3]}",
            "DadosC": f"{dados3[4]} {dados3[5]} {dados3[6]} {dados3[7]} {dados3[8]} {dados3[9]} {dados3[10]} ",
            "DadosL": f"{dados3[11]} {dados3[12]} {dados3[13]}",
            "DadosD": f"{dados4[0]} {dados4[1]} {dados4[2]}",
            "DadosP": f"{dados4[3]} {dados4[4]} {dados4[5]} {dados4[6]}",
            "DadosT": f"{dados4[7]} {dados4[8]} {dados4[9]} {dados4[10]} {dados4[11]}",
            "DadosF": f"{dados5[0]} {dados5[1]} {dados5[2]}",
            "DadosH": f"{dados5[3]} {dados5[4]} {dados5[5]} {dados5[6]}",
            "Dados1": f"{dados5[7]} {dados5[8]} {dados5[9]}"
        }
        return obj_OBS
    
def Final_pagina(num_page):
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file):
        row = text.Pegar_texto(num_page)
        total_operacao = row[-6].split()
        total_i = 3
        observacao = ''
        while total_i <= len(total_operacao) - 1:
            observacao += f"{total_operacao[total_i]} "
            total_i += 1
        
        especificacao = row[-5].split('_')
        obj_info_inferior = {
            "Especificacoes_diversas": especificacao[0],
            "Observacao": observacao,
            "Informacoes_adicionais": f"{row[-3]} {row[-2]} {row[-1]}"
        }
        return obj_info_inferior

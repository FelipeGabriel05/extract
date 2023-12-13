import pdfplumber
import text
import nome_arquivo

def Resumo(num_page): 
    file = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(file) as pdf:
        row = text.Pegar_texto(num_page)
        
        lista_resumo = []
        total_linhas = -25
        while total_linhas <= -13:
            
            if row[total_linhas][-1] == 'C' or row[total_linhas][-1] == 'D':
                resumo = row[total_linhas].split()
            else:
                resumo = row[total_linhas].split()
                resumo.append('')
            
            lista_resumo.append(resumo)
            total_linhas += 1
            
        obj_resumo_negocios = {
            "Debentures": lista_resumo[0][1],
            "Vendas_a_vista": lista_resumo[1][3],
            "Compras_a_vista": lista_resumo[2][3],
            "Opcoes_Compras": lista_resumo[3][3],
            "Opcoes_Vendas": lista_resumo[4][3],
            "Operacoes_a_termo": lista_resumo[5][3],
            "Operacoes_a_Futuro": lista_resumo[6][3],
            "Valor_das_Oper_com_Til_Publ": lista_resumo[7][6],
            "Valor_das_Operacoes": lista_resumo[8][3],
            "Valor_do_Ajuste_pFuturo": lista_resumo[9][4],
            "IR_Sobre_Corretagem": lista_resumo[10][3],
            "IRRF_Sobre_Day_Trade": lista_resumo[11][4]
        }
        
        liquido =  f"{lista_resumo[12][0]} {lista_resumo[12][1]} {lista_resumo[12][2]}"
        obj_resumo_financeiro = {
            "Valor_Liquido_das_Operacoes_1": {
                "Valor": lista_resumo[0][-2],
                "DC": lista_resumo[0][-1]
            },
            "Taxa_de_Liquidacao_2": {
                "Valor":lista_resumo[1][-2],
                "DC": lista_resumo[1][-1]
            },
            "Taxa_de_Registro": {
                "Valor": lista_resumo[2][-2],
                "DC": lista_resumo[2][-1]
            },
            "Total_1_2_3_A": {
                "Valor": lista_resumo[3][-2],
                "DC": lista_resumo[3][-1]
            },
            "Taxa_de_Termos_Opcoes_Futuro": {
                "Valor":  lista_resumo[4][-2],
                "DC": lista_resumo[4][-1]
            },
            "Taxa_ANA": {
                "Valor": lista_resumo[5][-2],
                "DC": lista_resumo[5][-1]
            },
            "Emolumentos": {
                "Valor": lista_resumo[6][-2],
                "DC": lista_resumo[6][-1]
            },
            "Total_Bolsa_B": {
                "Valor":  lista_resumo[7][-2],
                "DC": lista_resumo[7][-1]
            },
            "Corretagem": {
                "Valor": lista_resumo[8][-2],
                "DC": lista_resumo[8][-1]
            },
            "ISS": {
                "Valor": lista_resumo[9][-2],
                "DC": lista_resumo[9][-1]
            },
            "IRRFs_operacoes_base": {
                "Valor":  lista_resumo[10][-2],
                "DC": lista_resumo[10][-1]
            },
            "Outras": {
                "Valor": lista_resumo[11][-2],
                "DC": lista_resumo[11][-1]
            },
            liquido: {
                "Valor":  lista_resumo[12][-2],
                "DC": lista_resumo[12][-1]
            }
        }
        
        obj = {
            "Resumo dos Negocios": obj_resumo_negocios,
            "Resumo Financeiro": obj_resumo_financeiro
        }
        return obj
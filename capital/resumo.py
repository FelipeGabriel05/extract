import pdfplumber
import nome_arquivo

def Resumo(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[num_page]
        coluna_inferior = page.crop((10, 628, page.width, 710))
    
        inferior_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "text",
            "explicit_vertical_lines": [ 39, 57, 110, 128, 180, 196, 201, 244, 250, 360,
        370, 479, 482, 594],
            "explicit_horizontal_lines": [635, 648, 654, 668, 675, 686, 696, 705]
        }
        
        dados = coluna_inferior.extract_table(inferior_settings)
        
        if len(dados) == 9:
            obj_resumo = {
                "Vendas_disponivel": dados[1][2],
                "Compra_disponivel": dados[1][6],
                "Vendas_opcoes": dados[1][8],
                "Compras_opcoes": dados[1][10],
                "Valor_dos_negocios": dados[1][11],
                "IRRF": dados[4][2],
                "Taxa_Corretora_Intermediacao": dados[4][6],
                "Taxa_Corretora_IMPLANT": dados[4][8],
                "Taxa_registro_BMeF": dados[4][10],
                "Taxa_registro_BMeF_emol": dados[4][11],
                "IRRF_day_Trade_projecao": dados[7][2],
                "Outros_custos": dados[7][4],
                "ISS": dados[7][6],
                "Ajuste_de_posicao": dados[7][8],
                "Ajuste_day_trade": dados[7][10],
                "Total_das_despesas": dados[7][11],
                "Outros": '',
                "IRRF_corretagem": '',
                "Total_Conta_Investimento": '',
                "Total_Conta_Normal": '',
                "Total_liquido": '',
                "Total_liquido_da_nota": ''
            }
        else:
            obj_resumo = {
                "Vendas_disponivel": dados[1][2],
                "Compra_disponivel": dados[1][6],
                "Vendas_opcoes": dados[1][8],
                "Compras_opcoes": dados[1][10],
                "Valor_dos_negocios": dados[1][11],
                "IRRF": dados[4][2],
                "Taxa_Corretora_Intermediacao": dados[4][6],
                "Taxa_Corretora_IMPLANT": dados[4][8],
                "Taxa_registro_BMeF": dados[4][10],
                "Taxa_registro_BMeF_emol": dados[4][11],
                "IRRF_day_Trade_projecao": dados[7][2],
                "Outros_custos": dados[7][4],
                "ISS": dados[7][6],
                "Ajuste_de_posicao": dados[7][8],
                "Ajuste_day_trade": dados[7][10],
                "Total_das_despesas": dados[7][11],
                "Outros": dados[10][0],
                "IRRF_corretagem": dados[10][2],
                "Total_Conta_Investimento": dados[10][6],
                "Total_Conta_Normal": dados[10][8],
                "Total_liquido": dados[10][10],
                "Total_liquido_da_nota": dados[10][11]
            }
        return obj_resumo
        
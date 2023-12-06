import pdfplumber

def templateBradesco(name_file):
    paginas = 0
    with pdfplumber.open('Bradesco.pdf') as pdf:
        while paginas <= len(pdf.pages) - 1:
            page = pdf.pages[0]
            text = page.extract_text()
            all_text = ''
            for row in text:
                all_text += text
            row = all_text.split('\n')
            coluna_titulo = page.crop((455, 20, page.width, 65))
            titulos_settings = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "explicit",
                "explicit_horizontal_lines": [50, 57],
                "explicit_vertical_lines": [458, 490, 523, 578]
            }
            titulos = coluna_titulo.extract_table(titulos_settings)
            
            corretora = page.crop((340, 90, page.width, 100))
            corretora_settings1 = {
                "vertical_strategy": "explicit",
                "explicit_vertical_lines": [390, 560]
            }
            email_corretora = corretora.extract_table(corretora_settings1)
            
            corretora2 = page.crop((340, 100, page.width, 110))
            corretora_settings2 = {
                "vertical_strategy": "explicit",
                "explicit_vertical_lines": [442, 550]
            }
            carta = corretora2.extract_table(corretora_settings2)
            
            corretora3 = page.crop((340, 110, page.width, 120))
            corretora_settings3 = {
                "vertical_strategy": "explicit",
                "explicit_vertical_lines": [420, 580]
            }
            email_ouvidoria = corretora3.extract_table(corretora_settings3)    
            
            coluna_cliente = page.crop((20, 125, 457, 162))
            cliente_settings = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "explicit",
                "explicit_horizontal_lines": [132, 142, 152, 159],
                "explicit_vertical_lines": [38, 100, 455]
            }
            tabela_cliente = coluna_cliente.extract_table(cliente_settings)
            documento = row[10].split()
            coluna_cliente2 = page.crop((454, 140, page.width, 162))
            cliente_settings2 = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "explicit",
                "explicit_horizontal_lines": [150, 160],
                "explicit_vertical_lines": [458, 538, 580]
            }
            tabela_cliente2 = coluna_cliente2.extract_table(cliente_settings2)
            obj_cliente = {
                "CPF_CNPJ_CVM_COB": documento[-1],
                "Numero_do_Cliente": tabela_cliente[0][0],
                "Nome": tabela_cliente[0][1],
                "Endereco_cliente": f"{tabela_cliente[1][1]} {tabela_cliente[2][1]}",
                "Codigo_cliente": tabela_cliente2[0][0],
                "Acessor": tabela_cliente2[0][1]
            }
            
            coluna_banco = page.crop((20, 160, page.width, 180))
            banco_settings = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "explicit",
                "explicit_horizontal_lines": [170, 178],
                "explicit_vertical_lines": [40, 250, 330, 456, 558, 578]
            }
            tabela_banco = coluna_banco.extract_table(banco_settings)
            coluna_banco2 = page.crop((20, 180, page.width, 200))
            banco_settings2 = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "explicit",
                "explicit_horizontal_lines": [188, 198],
                "explicit_vertical_lines": [38, 69, 169, 254, 333, 456, 558, 578]
            }
            tabela_banco2 = coluna_banco2.extract_table(banco_settings2)
            obj_banco = {
                "Participante_destino_do_repasse": tabela_banco[0][0],
                "Cliente": tabela_banco[0][2],
                "Valor": f"{tabela_banco[0][4]} {tabela_banco[0][5]}",
                "Custodiante": tabela_banco[0][6],
                "CI": tabela_banco[0][7],
                "Banco": tabela_banco2[0][0],
                "Agencia": tabela_banco2[0][1],
                "Conta_Corrente": tabela_banco2[0][2],
                "Acionista": tabela_banco2[0][3],
                "Administrador": tabela_banco2[0][4],
                "Complemento_nome": tabela_banco2[0][5],
                "P_Vinc": tabela_banco2[0][6]
            }
            
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
                total_negocios[f"negocio_{i}"] = negocio
                i += 1
            
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
                "DadosL": table_obs[6][1]
            }
            
            coluna_financeira = page.crop((307, 400, page.width, 660))
            
            financeiro = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "explicit",
                "explicit_vertical_lines": [308, 500, 564, 574],
                "explicit_horizontal_lines": [
                    440, 450, 460, 470, 478, 486, 496, 506, 516, 524, 532,
                    542, 552, 560, 570, 580, #alterações aqui
                    598, 608, 615, 625, 635
                ]
            }
            Resumo_financeiro = coluna_financeira.extract_table(financeiro) 
            obj_bolsa = {
                "titulo": Resumo_financeiro[5][0],
                Resumo_financeiro[6][0]: Resumo_financeiro[6][2],
                f"{Resumo_financeiro[6][0]}_DC": Resumo_financeiro[6][3],
                Resumo_financeiro[7][0]: Resumo_financeiro[7][2],
                f"{Resumo_financeiro[7][0]}_DC": Resumo_financeiro[7][3],
                Resumo_financeiro[8][0]: Resumo_financeiro[8][2],
                f"{Resumo_financeiro[8][0]}_DC": Resumo_financeiro[8][3],
                "Total_Bovespa_Soma": Resumo_financeiro[9][2],
                "Total_Bovespa_Soma_DC": Resumo_financeiro[9][3]
            }
            
            obj_Corretagem = {
                "Titulo": Resumo_financeiro[10][0],
                "Corretagem": Resumo_financeiro[12][2],
                "Corretagem_DC":Resumo_financeiro[12][3],
                "ISS": Resumo_financeiro[13][2],
                "ISS_DC": Resumo_financeiro[13][3],
                "IRRF": Resumo_financeiro[14][2],
                "IRRF_DC": Resumo_financeiro[14][3],
                "Outras": Resumo_financeiro[16][2],
                "Outras_DC": Resumo_financeiro[16][3],
                "Total_corretagem_Despesas": Resumo_financeiro[17][2],
                "Total_corretagem_Despesas_DC": Resumo_financeiro[17][3],
                Resumo_financeiro[18][0]: Resumo_financeiro[18][2],
                f"{Resumo_financeiro[18][2]}_obs": Resumo_financeiro[18][3],
                "Observacao": Resumo_financeiro[19][0]
            }
            
            obj_resumo_financeiro = {
                "titulo": Resumo_financeiro[0][0],
                "Valor_liquido_das_operacoes": Resumo_financeiro[1][2],
                "Valor_liquido_das_operacoes_DC": Resumo_financeiro[1][3],
                "Taxa_de_liquidacao": Resumo_financeiro[2][2],
                "Taxa_de_liquidacao_obs": Resumo_financeiro[2][3],
                "Taxa_de_registro": Resumo_financeiro[3][2],
                "Taxa_de_registro_obs": Resumo_financeiro[3][3],
                "Total_CBLC": Resumo_financeiro[4][2],
                "Total_CBLC": Resumo_financeiro[4][3],
                "Bolsa": obj_bolsa,
                "Corretagem": obj_Corretagem,
                "Observacao_final": f"{row[-2]} {row[-1]}"
            }
            
            templateBradesco = {
                "Tipo_de_Nota": row[0],
                "Nr_Nota": titulos[0][0],
                "Foha": titulos[0][2],
                "Data_pregao": titulos[0][3],
                "email": email_corretora,
                "Carta_Patente": carta,
                "email_ouvidoria": email_ouvidoria,
                "Cliente": obj_cliente,
                "Banco": obj_banco,
                "Negocios": total_negocios,
                "Resumos_dos_negocios": obj_resumo_negocios,
                "Observacoes_de_negocios": obj_obs,
                "Resumo_Financeiro": obj_resumo_financeiro
            }
            print(templateBradesco)

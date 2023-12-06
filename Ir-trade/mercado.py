import pdfplumber

total_meses = 3
negocios_mercado = {}
with pdfplumber.open('48976_informe_para_imposto_renda_ano_calendario_2021.pdf') as pdf:
    while total_meses <= 14:
        page = pdf.pages[total_meses]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        vista_acoes = row[9].split()
        vista_ouro = row[10].split()
        vista_outro = row[11].split()
        mercado_vista = {
            "Mercado à vista": {
                "Operações comuns": vista_acoes[-2],
                "Day-Trade": vista_acoes[-1]
            },
            "Mercado à vista - ouro": {
                "Operações comuns": vista_ouro[-2],
                "Day-Trade": vista_ouro[-1]
            },
            "Mercado à vista - outro at. fin. fora bolsa": {
                "Operações comuns": vista_outro[-2],
                "Day-Trade": vista_outro[-1]
            }
        }
        
        opcoes_acoes = row[13].split()
        opcoes_ouro = row[14].split()
        opcoes_fora_bolsa = row[15].split()
        opcoes_outros = row[16].split()
        mercado_opcoes = {
            "Mercado opções - ações": {
                "Operações comuns": opcoes_acoes[-2],
                "Day-Trade": opcoes_acoes[-1]
            },
            "Mercado opções - ouro": {
                "Operações comuns": opcoes_ouro[-2],
                "Day-Trade": opcoes_ouro[-1]
            },
            "Mercado opções - fora bolsa": {
                "Operações comuns": opcoes_fora_bolsa[-2],
                "Day-Trade": opcoes_fora_bolsa[-1]
            },
            "Mercado opções - outros": {
                "Operações comuns": opcoes_outros[-2],
                "Day-Trade": opcoes_outros[-1]
            }
        }
        
        futuro_dolar = row[18].split()
        futuro_indices = row[19].split()
        futuro_juros = row[20].split()
        futuro_outros = row[21].split()
        mercado_futuro = {
            "Mercado à vista - dólar dos EUA": {
                "Operações comuns": futuro_dolar[-2],
                "Day-Trade": futuro_dolar[-1]
            },
            "Mercado à vista - índices": {
                "Operações comuns": futuro_indices[-2],
                "Day-Trade": futuro_indices[-1]
            },
            "Mercado à vista - juros": {
                "Operações comuns": futuro_juros[-2],
                "Day-Trade": futuro_juros[-1]
            },
            "Mercado à vista - outros": {
                "Operações comuns": futuro_outros[-2],
                "Day-Trade": futuro_outros[-1]
            }
        }

        termo_acoes = row[23].split()
        termo_opcoes = row[24].split()
        mercado_termo = {
            "Mercado a termo - ações/outro": {
                "Operações comuns": termo_acoes[-2],
                "Day-Trade": termo_acoes[-1]
            },
            "Mercado opções - outros": {
                "Operações comuns": termo_opcoes[-2],
                "Day-Trade": termo_opcoes[-1]
            }
        }
        
        result_liquido = row[26].split()
        result_negativo = row[27].split()
        result_base = row[28].split()
        result_prejuizo = row[29].split()
        result_aliquota = row[30].split()
        result_imposto = row[31].split()
        
        resultado = {
            "RESULTADO LIQUÍDO DO MÊS": {
                "Operações comuns": result_liquido[-2],
                "Day-Trade": result_liquido[-1]
            },
            "Resultado negativo até o mês anterior": {
                "Operações comuns": result_negativo[-2],
                "Day-Trade": result_negativo[-1]
            }, 
            "BASE DE CÁLCULO DO IMPOSTO": {
                "Operações comuns": result_base[-2],
                "Day-Trade": result_base[-1]
            },
            "Prejuízo a compensar": {
                "Operações comuns": result_prejuizo[-2],
                "Day-Trade": result_prejuizo[-1]
            },
            "Alíquota do imposto": {
                "Operações comuns": result_aliquota[-2],
                "Day-Trade": result_aliquota[-1]
            },
            "IMPOSTO DEVIDO": {
                "Operações comuns": result_imposto[-2],
                "Day-Trade": result_imposto[-1]
            }
        }
        
        linha33 = row[33].split()
        linha34 = row[34].split()
        linha35 = row[35].split()
        linha36 = row[36].split()
        linha37 = row[37].split()
        linha38 = row[38].split()
        linha39 = row[39].split()
        linha40 = row[40].split()
        linha41 = row[41].split()
        consolidacao_mes = {
            "Total do imposto devido": linha33[-1],
            "IR Fonte de Day-Trade no mês": linha34[-1],
            "IR Fonte de Day-Trade nos meses anteriores": linha35[-1],
            "IR Fonte de Day-Trade a compensar": linha36[-1], 
            "IR Fonte (lei nº 11.033/2004) no mês": linha37[-1],
            "IR Fonte (lei nº 11.033/2004) nos meses anteriores": linha38[-1],
            "IR Fonte (lei nº 11.033/2004) meses a compensar": linha39[-1],
            "Imposto a pagar": linha40[-1],
            "Imposto pago": linha41[-1],
            "obs": f"{linha41[2]} {linha41[3]} {linha41[4]} {linha41[5]} {linha41[6]} {linha41[7]} {linha41[8]}"
        }
        
        mes = row[7].split()
        if total_meses == 14:    
            mercado = {
                "Mercado à vista": mercado_vista,
                "Mercado Opções": mercado_opcoes,
                "Mercado Futuro": mercado_futuro,
                "Mercado Termo": mercado_termo,
                "Resultados": resultado,
                "Consolidação do Mês": consolidacao_mes,
                "informação1": row[-4],
                "informação2": f"{row[-3]} {row[-2]}"
            }
        else:
            mercado = {
                "Mercado à vista": mercado_vista,
                "Mercado Opções": mercado_opcoes,
                "Mercado Futuro": mercado_futuro,
                "Mercado Termo": mercado_termo,
                "Resultados": resultado,
                "Consolidação do Mês": consolidacao_mes,
            }
        negocios_mercado[f"{mes[-1]}"] = mercado
        total_meses += 1
        
print(negocios_mercado)

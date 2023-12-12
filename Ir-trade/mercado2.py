import pdfplumber
import text
import nome_arquivo

def Mercado_Termo(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_Texto(num_page)
        
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
        return mercado_termo
    
def Resultados(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_Texto(num_page)
        
        result_liquido = row[26].split()
        result_negativo = row[27].split()
        result_base = row[28].split()
        result_prejuizo = row[29].split()
        result_aliquota = row[30].split()
        result_imposto = row[31].split()
        
        obj_resultado = {
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
        return obj_resultado
    
def Consolidacao(num_page):
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        row = text.Pegar_Texto(num_page)
        
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
        return consolidacao_mes
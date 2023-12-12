import pdfplumber
import nome_arquivo

def Detalhes():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        coluna_detalhes = page.crop((20, 430, page.width, 500))
        detalhes_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [40, 106, 170, 230, 318, 413, 496, 566]
        }
        table_detalhes = coluna_detalhes.extract_table(detalhes_settings)
        linha14 = row[14].split()
        linha15 = row[15].split()
        total_detalhes = {
            "Título": linha14[0],
            "Quantidade_total_de_compra": linha14[5],
            "Preço médio compra": f"{linha14[9]} {linha15[0]}",
            "Quantidade_total_de_venda": {linha14[14]},
            "Preço médio venda": f"{linha14[-1]} {linha15[-1]}"
        }
        total_negocios = 0
        while total_negocios <= len(table_detalhes) - 1:
            soma = total_negocios + 1
            negocio = {
                "CV": table_detalhes[total_negocios][0],
                "Vencimento": table_detalhes[total_negocios][1],
                "Quantidade": table_detalhes[total_negocios][2],
                "Preco_Ajuste": table_detalhes[total_negocios][3],
                "Tipo_de_negocio": table_detalhes[total_negocios][4],
                "Valor_Operacao": table_detalhes[total_negocios][5],
                "Taxa_Operacao": table_detalhes[total_negocios][6],
            }
            total_detalhes[f"negocio_{soma}"] = negocio 
            total_negocios += 1
        return total_detalhes
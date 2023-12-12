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
        
        coluna_detalhes = page.crop((20, 430, page.width, 480))
        detalhes_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "lines",
            "explicit_vertical_lines": [35, 90, 140, 210, 260, 340, 400, 480, 518, 567]
        }
        tabela_detalhes = coluna_detalhes.extract_table(detalhes_settings)
        
        linha14 = row[14].split()
        obj = {
            "Titulo": row[13],
            "Preco de Exercício": linha14[3],
            "Quantidade_total_de_compra": linha14[8],
            "Preço_médio_compra": f"{linha14[12]} {row[15]}",
            "Quantidade_total_de_venda": linha14[17],
            "Preço_médio_venda": f"{linha14[21]}{linha14[22]}"
        }
        
        obj_detalhes = {
            "Detalhes_Negocio": obj,
            "CV": tabela_detalhes[0][0],
            "Mercado": tabela_detalhes[0][1],
            "Quantidade": tabela_detalhes[0][2],
            "Preço": tabela_detalhes[0][3],
            "Valor_Operação": tabela_detalhes[0][4],
            "Vencimento": tabela_detalhes[0][5],
            "Tipo_Mercado": tabela_detalhes[0][6],
            "Envio": tabela_detalhes[0][7],
            "OBS": tabela_detalhes[0][8]
        }
        return obj_detalhes
        
import pdfplumber
import nome_arquivo

def Observacoes():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        linha19 = row[19].split()
        linha20 = row[20].split()
        
        total_increment = 12
        nome = ''
        while total_increment <= 26:
            nome += f" {linha19[total_increment]}"
            total_increment += 1
        ouvidoria = row[-3].split('Ouvidoria:')
        obj_especificacoes = {
            "IRRF_Day_Trade": {
                "Base": f"{linha19[7]} {linha19[8]}",
                "Projeção": f"{linha19[10]} {linha19[11]}",
                "obs": nome
            },
            "IRRF_Operacao_Comum": {
                "Base": linha20[4],
                "Projeção": linha20[6],
                "obs": row[21],
            },
            "informação adicional": f"{row[22]} {row[23]} {row[24]} {row[25]} {row[26]} {row[27]} {row[28]}",
            "Ouvidoria": ouvidoria[-1],
            "Dias_uteis": row[-2],
            "Página": row[-1]
        }
        return obj_especificacoes

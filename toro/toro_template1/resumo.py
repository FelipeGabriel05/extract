import pdfplumber
import nome_arquivo

def Resumo():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        coluna_resumo = page.crop((20, 155, page.width, 270))
        
        resumo_settings = {
            "vertical_strategy": "explicit",
            "horizontal_strategy": "text",
            "explicit_horizontal_lines": [160, 170, 190, 210, 220, 240, 255, 265],
            "explicit_vertical_lines": [35, 120, 158, 170, 250, 294, 304, 370, 430, 442, 500, 566]
        }
        table_resumo = coluna_resumo.extract_table(resumo_settings)
        
        i = 0
        lista_resumo = []
        while i <= len(table_resumo) - 1:
            if table_resumo[i][0] != '':
                lista_resumo.append(table_resumo[i])
            i += 1
            
        resumo = {
            "VOLUME FINANCEIRO E AJUSTES": {
                lista_resumo[0][0]: lista_resumo[0][1],
                lista_resumo[1][0]: lista_resumo[1][1],
                lista_resumo[2][0]: lista_resumo[2][1],
                lista_resumo[3][0]: lista_resumo[3][1],
                lista_resumo[4][0]: lista_resumo[4][1],
                lista_resumo[5][0]: lista_resumo[5][1],
                lista_resumo[6][0]: lista_resumo[6][1]
            },
            "TRIBUTOS": {
                lista_resumo[0][3]: lista_resumo[0][4],
                lista_resumo[1][3]: lista_resumo[1][4],
                lista_resumo[2][3]: lista_resumo[2][4],
                lista_resumo[3][3]: lista_resumo[3][4],
                lista_resumo[4][3]: lista_resumo[4][4],
                lista_resumo[5][3]: lista_resumo[5][4]
            },
            "CUSTOS": {
                lista_resumo[0][6]: lista_resumo[0][7],
                lista_resumo[1][6]: lista_resumo[1][7],
                lista_resumo[2][6]: lista_resumo[2][7],
                lista_resumo[3][6]: lista_resumo[3][7],
            },
            "RESULTADO": {
                lista_resumo[0][9]: lista_resumo[0][10],
                lista_resumo[1][9]: lista_resumo[1][10],
                lista_resumo[2][9]: lista_resumo[2][10],
                lista_resumo[3][9]: lista_resumo[3][10]
            }
        }
        
        return resumo

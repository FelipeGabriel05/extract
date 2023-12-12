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
            "explicit_vertical_lines": [35, 120, 158, 170, 250, 294, 304, 370, 430, 442, 500, 566],
            "explicit_horizontal_lines": [160, 170, 190, 210, 220, 240, 255]
        }
        table_resumo = coluna_resumo.extract_table(resumo_settings)
        
        i = 0
        resumo_list = []
        while i <= len(table_resumo) - 1:
            if table_resumo[i][4] != '':
                resumo_list.append(table_resumo[i])
            i += 1
            
        resumo = {
            "RESUMO DOS NEGÓCIOS": {
                resumo_list[0][0]: resumo_list[0][1],
                resumo_list[1][0]: resumo_list[1][1],
                resumo_list[2][0]: resumo_list[2][1],
                resumo_list[3][0]: resumo_list[3][1]
            },
            "Tributos": {
                resumo_list[0][3]: resumo_list[0][4],
                resumo_list[1][3]: resumo_list[1][4],
                resumo_list[2][3]: resumo_list[2][4],
                resumo_list[3][3]: resumo_list[3][4],
                resumo_list[-3][3]: resumo_list[-3][4],
                resumo_list[-2][3]: resumo_list[-2][4],
                resumo_list[-1][3]: resumo_list[-1][4]
            },
            "CUSTOS": {
                resumo_list[0][6]: resumo_list[0][7],
                resumo_list[1][6]: resumo_list[1][7],
                resumo_list[2][6]: resumo_list[2][7],
                resumo_list[3][6]: resumo_list[3][7],
                resumo_list[-2][6]: resumo_list[-2][7],
                resumo_list[-1][6]: resumo_list[-1][7],
            },
            "RESULTADO": {
                resumo_list[0][9]: resumo_list[0][10],
                resumo_list[1][9]: resumo_list[1][10],
                resumo_list[2][9]: resumo_list[2][10],
                resumo_list[3][9]: resumo_list[3][10],
                resumo_list[-2][-2]: resumo_list[-2][-1],
            }
        }
        return resumo        

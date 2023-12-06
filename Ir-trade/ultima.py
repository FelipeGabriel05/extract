import pdfplumber

with pdfplumber.open('48976_informe_para_imposto_renda_ano_calendario_2021.pdf') as pdf:
        page = pdf.pages[17]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        whatsapp = row[-1].split('17/17')
        obj = {
            "observação1": f"{row[7]} {row[8]} {row[9]} {row[10]} {row[11]} {row[12]}",
            "observação2": f"{row[13]} {row[14]} {row[15]}",
            "telefone": row[-3],
            "email": row[-2],
            "whatsapp": whatsapp[0] 
        }
        print(obj)
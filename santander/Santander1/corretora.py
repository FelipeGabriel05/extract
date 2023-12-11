import pdfplumber
import nome_arquivo

def Titulo():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        linha1 = row[0].split()
        linha3 = row[3].split()
        obj_titulo = {
            "Plataforma": linha1[-1],
            "Data_de_extração": f"{linha1[0]} {linha1[1]}",
            "Tipo_de_Nota": row[1],
            "N_Nota": linha3[0],
            "Data_Pregão": linha3[1]
        }
        return obj_titulo
    
def Corretora():
    arquivo = nome_arquivo.Nome_arquivo()
    with pdfplumber.open(arquivo) as pdf:
        page = pdf.pages[0]
        all_text = ''
        text = page.extract_text()
        for row in text:
            all_text += text
        row = all_text.split('\n')
        
        linha4 = row[4].split()
        linha5 = row[5].split()
        cnpj_carta = row[6].split()
        endereco = row[8].split('EMAIL: santander.acoes@santander.com.br')
        email = row[8].split()
        
        obj_corretora = {
            "Nome_Corretora": f"{linha4[0]} {linha4[1]} {linha4[2]} {linha4[3]} {linha4[4]} {linha4[5]} {linha5[0]} {linha5[1]}",
            "Telefone_capitais_e_regiãoMetropolitana": f"{linha4[7]} {linha4[8]}",
            "Telefone_demais_localidades": f"{linha4[-3]} {linha4[-2]} {linha4[-1]}",
            "Telefone_pessoas_com_deficiencia_auditiva_e_fala": f"{linha5[5]} {linha5[6]} {linha5[7]}",
            "CNPJ": cnpj_carta[1],
            "Carta Patente": cnpj_carta[-1],
            "Endereço": f"{row[7]} {endereco[0]}",
            "EMAIL": email[-1]
        } 
        return obj_corretora
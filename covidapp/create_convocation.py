from docx import Document

def create_convocation(nom_complet, centre, date):
    document = Document('static/Convocation de vaccination.docx')

    i = 1
    for paragraph in document.paragraphs:
        # print(f"{i}: {paragraph.text}")
    
        if i == 5:
            paragraph.insert_paragraph_before(nom_complet)

        if i == 7:
            paragraph.insert_paragraph_before(f"{centre}, {date}")

        i += 1



    document.save(f'Convocation de vaccination_{nom_complet}.docx')
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from fpdf import FPDF

# === PART 1 : Extract the PDF's content ===

def extract_pdf(path_to_pdf):
    resource_manager = PDFResourceManager(caching=True)
    out_text = StringIO()
    laParams = LAParams()
    text_converter = TextConverter(resource_manager, out_text, laparams=laParams)
    fp = open(path_to_pdf, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = out_text.getvalue()
    fp.close()
    text_converter.close()
    out_text.close()

    return text


# === PART 2 : Create a PDF with the extract content ===

def create_pdf(text, title, size=10):

    # Create FPDF object
        #Layout ('Portrait', 'Landscape')
        #Unit ('mm', 'cm', 'in')
        #format ('A3', 'A4', (default), 'Letter', 'Legal', (100, 150))
    pdf = FPDF('P', 'cm', 'A4')

    # Add a page
        # [ === perhaps useful for header & footer (need check doc) ===
        # W = width
        # h = height
        # pdf.cell(1000, 1000, get_pdf_file_content(path_to_pdf))
        # pdf.multi_cell(1000, 1000, get_pdf_file_content(path_to_pdf),0,'R')
        # pdf.ln(10000) ]
    pdf.add_page() # can add header & footer (check doc)


    # specify font
        # fonts ('times', 'courier', 'helvetica', 'symbol',  'unFontQuoi')
        # 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
    pdf.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', size)

    # Add text
    pdf.write(0.5, text)

    # Create PDF file
    pdf.output(title+'.pdf')


# path_to_pdf = "./DELL_Computer_CV.pdf"
# titre_pdf = "daco"
# create_pdf(extract_pdf(path_to_pdf), titre_pdf)
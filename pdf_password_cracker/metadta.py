import os
from pdfreader import PDFDocument

base_dir = os.path.abspath('')

pdf_path = os.path.join(base_dir, 'np.pdf')
with open(pdf_path, 'rb') as fd:
    doc = PDFDocument(fd, password='arun12')

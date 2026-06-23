import os

from tools.pdf_tool import read_pdf
from tools.docx_tool import read_docx
from tools.txt_tool import read_txt


def extract_content(filepath):

    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        return read_pdf(filepath)

    elif ext == ".docx":
        return read_docx(filepath)

    elif ext == ".txt":
        return read_txt(filepath)

    else:
        raise ValueError("Unsupported file type")
import pdfplumber

def load_pdf(file_path):
    documents = []

    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                documents.append({
                    "text": text,
                    "metadata": {
                        "source": file_path,
                        "page": page_num
                    }
                })

    return documents

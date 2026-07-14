from pathlib import Path

import fitz
from pypdf import PdfReader


root = Path(__file__).resolve().parent.parent
pdf_path = root / "output" / "pdf" / "肖雨菲-软件工程个人作品集.pdf"
render_dir = root / "tmp" / "pdfs"
render_dir.mkdir(parents=True, exist_ok=True)

document = fitz.open(pdf_path)
for index, page in enumerate(document):
    pixmap = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    pixmap.save(render_dir / f"portfolio-page-{index + 1}.png")

reader = PdfReader(pdf_path)
text = "\n".join(page.extract_text() or "" for page in reader.pages)
print(f"pages={len(reader.pages)}")
print(f"text_characters={len(text)}")
print(f"contains_name={'肖雨菲' in text}")
print(render_dir)

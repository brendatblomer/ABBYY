### Pick pages we need to put on ABBYY

# first we import the packages we need

from pypdf import PdfReader, PdfWriter
from pathlib import Path


# we create our path to the PDF and bring it here
pdf_file_path = Path("borrar_luego/Report_manufacturing_1973.PDF")
pdf_file = PdfReader(pdf_file_path)

# we create an empty file which will be later our file ready for ABBYY
pdf_file_ready = PdfWriter()

# we select the pages we want
# we select from page 53 to 148, we substract -1 to the start because it starts at 0, and we leave the actual page we want because it takes until the one before but it starts at 0.
pages = list(range(52, 148))

# we insert this in the new pdf file
for i in pages: 
    pdf_file_ready.add_page(pdf_file.pages[i])

# we saved the file year_pdf
# 1. In my case, I want this new file in my folder called "PDFs-recortadosparaabby" which is inside "ABBY" (made a mistake with the y) in my current directory
# 2. We create a path for the new file
# 3. We check that is correct and exists

root = Path(__file__).parent
output_path = root / "ABBY" / "PDFs-recortadosparaabby"
print(output_path.exists())

# now we create the file with the name "year.pdf" on the path describe before
with open(output_path / "1973.pdf", "wb") as out:
    pdf_file_ready.write(out)

print(f" Done in: {output_path}, now we can put file on ABBYY")


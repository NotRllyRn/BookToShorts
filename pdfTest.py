from pdfreader import PDFDocument, SimplePDFViewer

fileName = "The Great Gatsby.pdf"
startPage = 2

pdfFile = open(fileName, "rb")

viewer = SimplePDFViewer(pdfFile)

viewer.navigate(47)
viewer.render()

strings = viewer.canvas.strings
print('-'+''.join(strings)+'-')

for index, string in enumerate(strings):
    if "Chapter" in string:
        chapter = strings[index].strip()
        chapterIndex = index
        
content = strings[1:]
        
        
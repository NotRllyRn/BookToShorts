from pdfreader import PDFDocument, SimplePDFViewer

# import a regex module
import regex

# create a folder in the current directory named Chapters
from pathlib import Path
Path("Chapters").mkdir(parents=True, exist_ok=True)


fileName = "The Great Gatsby.pdf"

pdfFile = open(fileName, "rb")
viewer = SimplePDFViewer(pdfFile)

chapters = {}
currentChapter = 0

def doWithPage():
    global chapters
    global currentChapter
    
    unformattedText = ''.join(viewer.canvas.strings)
    chapterGroup = regex.search(r'(?<=THE GREAT GATSBY \d+Chapter\s)\d+\s', unformattedText)
    chapter = chapterGroup != None and int(chapterGroup.group(0).strip())
    
    text = ''
    if chapterGroup != None:
        text = unformattedText[chapterGroup.end():]
        
        print(chapter)
        chapters[chapter] = ''
        currentChapter = chapter
    else:
        text = regex.search(r'(?<=THE GREAT GATSBY \d+).+', unformattedText).group(0)
        
    chapters[currentChapter] += text

# write a try/except block to catch the StopIteration exception
try:
    while True:
        viewer.next()
        viewer.render()
        doWithPage()
        
        viewer.next()
except BaseException as e:
    pass

# write to file inside of the Chapters folder each chapter and the contents of each chapter
for chapter in chapters:
    chapterFile = open(f'Chapters/Chapter {chapter}.txt', 'w')
    chapterFile.write(chapters[chapter])
    chapterFile.close()
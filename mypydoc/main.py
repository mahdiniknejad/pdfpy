from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4


def hello(c: canvas.Canvas):
    c.drawString(100,100,"Hello World")
    
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()

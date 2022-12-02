import os
# file = open("4. Modelo relacional.md", "w")
# for i in range(117):
#     if i<10:
#         file.write("![](http://kunusoft.com/slides/bd1/bd104_relacional/Diapositiva0"+str(i)+".JPG)" + os.linesep)
#     elif i>99:
#         if i<110:
#             file.write("![](http://kunusoft.com/slides/bd1/bd104_relacional/Diapositiva990"+str(i)+".JPG)" + os.linesep)
#         else:
#             file.write("![](http://kunusoft.com/slides/bd1/bd104_relacional/Diapositiva99"+str(i)+".JPG)" + os.linesep)
#     else:
#         file.write("![](http://kunusoft.com/slides/bd1/bd104_relacional/Diapositiva"+str(i)+".JPG)" + os.linesep)
# file = open("11. Normalización II.md", "w")
# for i in range(100):
#     if i<10:
#         file.write("![](http://kunusoft.com/slides/bd1/bd111_norma2/Diapositiva0"+str(i)+".JPG)" + os.linesep)
#     else:
#         file.write("![](http://kunusoft.com/slides/bd1/bd111_norma2/Diapositiva"+str(i)+".JPG)" + os.linesep)


# file = open("11. Normalización II.md", "w")
# for i in range(100):
#     if i<10:
#         file.write("![](http://kunusoft.com/slides/bd1/bd111_norma2/Diapositiva0"+str(i)+".JPG)" + os.linesep)
#     else:
#         file.write("![](http://kunusoft.com/slides/bd1/bd111_norma2/Diapositiva"+str(i)+".JPG)" + os.linesep)

# file.close()








import os
from fpdf import FPDF
from PIL import Image
import requests
from io import BytesIO
#pdf = FPDF(orientation = 'L')

from PIL import Image
import requests

i = Image.open(requests.get("http://kunusoft.com/slides/ia1/ia101_intro/Diapositiva01.JPG", stream=True).raw)
w, h = i.size
margin=20
pdf = FPDF(unit="pt", format=[w + 2 * margin, h + 2 * margin])

pdf.add_page() #add a page first
im = i.convert('RGB')
pdf.image(im)
pdf.output("Lección 1 Introducción a la inteligencia artificial.pdf", "F")

# dirs = os.listdir('.')

# pdf1 = FPDF()
# #pdf1.add_page()
# for img in dirs:
#     if os.path.isfile(img) and os.path.splitext(img)[1].lower() in ('.jpg', '.jpeg', '.png'):
#         #print(img)
#         pdf1.add_page()
#         pdf1.image(img)

# pdf1.output("images.pdf", "F")
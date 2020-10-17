from PIL import Image as i
from PIL import ImageFilter
fug=i.open("kus.jpg")
degistir=(960,600)
fug.thumbnail(degistir)
fug.save("kus01.jpg")
fug.filter(ImageFilter.GaussianBlur(10)).save("Kuş345.jpg")

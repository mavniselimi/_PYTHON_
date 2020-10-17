from PIL import Image
atam=Image.open("original.jpg")
kus=Image.open("original e.jpg")
atam.show()
kus.show()
kus.rotate(70).save("kus4.jpg")
kus.convert(mode="L").save("kuş6.jpg")


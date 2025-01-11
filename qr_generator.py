import qrcode
import qrcode.image.svg


method = "path"

# inserir sempre entre aspas
data = "coloque aqui a url ou texto desejado"

if method == 'basic':
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    factory = qrcode.image.svg.SvgFragmentImage
elif method == 'path':
    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make(data, image_factory = factory)

# save svg file somewhere
img.save("qrcode.svg")
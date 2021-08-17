import qrcode

img = qrcode.make("https://ocw.mit.edu/index.htm")
img.save("MITQR.jpg")

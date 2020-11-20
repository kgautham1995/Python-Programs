# import qrcode
# qr=qrcode.QRCode(
#     version=1,
#     box_size=10,
#     border=5)
# data=input("Enter any text or number to which you want to create qrcode:")
# qr.add_data(data)
# qr.make(fit=True)
# img=qr.make_image(fill="black", back_color="white")
# img.save("2.png")

import qrcode
data=input("Enter any text or number to which you want to create qrcode:")
img=qrcode.make(data)
img.save("3.png")
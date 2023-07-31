import qrcode
import image
qr=qrcode.QRCode(version=10,border=5,box_size=10)
data="https://auth.geeksforgeeks.org/user/pkeerthisujitha/practice"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(back_color="white",fill="black")
img.save("qr.png")
# to use this module you need to install qrgenerator along with pillow modules
#use pip install qrgenerator[pil]
import qrcode
data = input("enter text or link=")
imgname=input("save image as=")
def qr(data,imgname):

# Creating an instance of QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=100,
        border=2,
    )
    # Adding data to the instance
    qr.add_data(data)
    #qr.make(fit=True)
    # Creating an image of the QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    # Saving the image
    img.save(imgname+".png")
qr(data,imgname)
print("sucessfull")
input("press enter to exit")


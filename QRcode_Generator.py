import qrcode as qr
img = qr.make(input("Enter link : "))
img.save(input("Enter the Name to save : ")+".png")
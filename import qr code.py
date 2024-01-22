def make_qrcode(content):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2
    )
    qr.add_data(content)
    qr.make(fit=True)
    image = qr.make_image(fill_color='black', back_color='white')
    image.save("qrcode.png")

    def identify_qrcode(file):
    qr_image = cv2.imread(file)
    qr_detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = qr_detector.detectAndDecode(qr_image)
    print(data)


make_qrcode("Hello Python")
identify_qrcode("qrcode.png")
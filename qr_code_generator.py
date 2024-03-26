# pip install segno
import segno

qrcode = segno.make_qr("https://github.com/MuhammetCanNamli")
qrcode.save(
    "basic_qrcode.png",
    scale = 10,
    border = 5,
)

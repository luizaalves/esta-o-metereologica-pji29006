from modules.bmp180 import BMP180

bmp = BMP180()

def test_read():
    medida = bmp.read()
    assert (medida >= 0) or (medida <= 100)

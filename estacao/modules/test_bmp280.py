from bmp280 import BMP280

driver_bmp280 = BMP280()
try:
    driver_bmp280.start()
except Exception as e:
    print(e)

if driver_bmp280.active:
    print(driver_bmp280.read("Temperatura"))
    print(driver_bmp280.read("Pressure"))
    print(driver_bmp280.read("altitude"))
else:
    print("Error")




# create qrCode in few steps
# import 
import pyqrcode

is_url = input('Enter URL to generate QRCode: ')

# generate qrcode and store as svg
def gen_qrcode(url='https://github.com/joshag/pyqrcode'):

    scale = input('Enter scale(N):')
    if not scale or int(scale) == 0:
        print('Scale value cannot be "0" or null')
        return

    qr_code = pyqrcode.create(url)
    qr_code.svg('Joshag_Qrcode_Generator.svg',int(scale))
    print(qr_code.terminal(quiet_zone=1))



gen_qrcode(is_url)

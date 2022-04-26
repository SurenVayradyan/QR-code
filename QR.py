import qrcode

def get_qrcode(url='https://www.google.com', name='hello'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.jpg')
    return f'QR code was created! Open the {name}.jpg'

def main():
    print(get_qrcode(url='https://img2.akspic.ru/originals/2/5/9/4/6/164952-hello_new_imac_2021_announcement_wallpaper_for_ipad-3208x3208.jpg', name='hello'))




if __name__ == '__main__':
    main()


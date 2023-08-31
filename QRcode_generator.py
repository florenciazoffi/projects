#%% QR generator by Florencia Zoffi
import time
import qrcode
import sys

def generator():
    url = input(f'Please enter what would want to be made into a QR code: ')
    print('Loading...')
    time.sleep(3)
    filename = ''.join(char if char.isalnum() or char in ('-', '_') else '_' for char in url)
    image = qrcode.make(url)
    out = open(filename+'_QR.png', "wb")
    image.save(out)
    print(f'Your text/url was created successfully, named {filename}_QR.png') 

def ask_leave():
    decision = input(f'Would you like to generate another QR code? y/n: ')
    decision.lower()
    if decision == 'y':
        generator()
        ask_leave()
    elif decision == 'n':
        print('Hope to see you again!')
        time.sleep(0.5)
        sys.exit()
    else: 
        print('Please enter a valid option: y(yes) or n(no).')
        ask_leave()

def main():
    print('''
***************************************************************************************
This program will ask you to provide a text or url to generate a QR code in PNG format.
          '''
          )
    time.sleep(1)
    generator()
    ask_leave()

if __name__ == "__main__":
    main()
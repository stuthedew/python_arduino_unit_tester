import serial

def main():
    ser = None
    try:
        with(serial.Serial('/dev/cu.usbmodem1411', 9600)) as ser:
            print(ser.name)
            while(True):
                message = ser.readline()
                print("{}".format(chr(message[0])))

    except Exception as e:
        print(e)

    finally:
        if(ser is not None):
            ser.close()

if __name__ == '__main__':
    main()

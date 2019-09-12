from modules.pins import Pins
from modules.servo import Servo
from modules.rgb import RGB

print("Loading...")


def main():
    print("Main function")
    tilt = Servo(Pins.servoTop, (1560, 1880), 60)
    pan = Servo(Pins.servoBottom, (560, 2450))
    rgb = RGB(Pins.ledRed,Pins.ledGreen,Pins.ledBlue)
    
    loop = True
    
    while loop:
        try:
            rgb.breathe(Pins.ledRed)
            #rgb.breathe(Pins.ledGreen)
            #rgb.breathe(Pins.ledBlue)
            pan.move(45)
            pan.move(55)
            tilt.move(0)
            tilt.move(100)
        except KeyboardInterrupt as e:
            print('EXITING!')
            pan.reset()
            tilt.reset()
            rgb.reset()
            loop = False
    
if __name__ == '__main__':
    main()

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        with open('/var/www/html/index.html', 'a') as f:
            f.write('Patient has checked in. Notify doctor.')
            break 
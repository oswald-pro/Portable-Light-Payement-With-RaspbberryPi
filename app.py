import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from Configs import I2C_LCD_driver

GPIO.setwarnings(False)
reader = SimpleMFRC522()
disp = I2C_LCD_driver.lcd()

username = 'ABC'
pin = "1234"
account =200

R1 = 11
R2 = 12
R3 = 13
R4 = 15

C1 = 22
C2 = 32
C3 = 33
C4 = 35

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


def start():
    global pin
    print("WELCOME TO SGL")
    disp.message(("   WELCOME TO SGL   "), 1)

    print("--Account Name: ABC--")
    disp.message(("  Account Name: ABC "), 3)
    time.sleep(10)
    disp.lcd_clear()
    print("Enter Password:")
    disp.message(("  Enter Password:   "), 1)
    password = input("Enter Password:")

    if pin == password:
        print("Login Successful")
        disp.message(("  Login Successful  "), 3)
        time.sleep(5)
        disp.lcd_clear()
        buy()
    else:
        print("Wrong Credentials")
        disp.message((" Wrong Credentials  "), 2)
        time.sleep(5)
        disp.lcd_clear()
        return start()

def buy():
    global account
    print("--------------------")
    disp.message(("   Enter Amount     "), 1)
    amount =int(input("Enter Amount: "))
    time.sleep(5)
    disp.lcd_clear()
    disp.message("    Processing......", 2)
    time.sleep(5)
    disp.lcd_clear()

    if amount <= account:
        amount =str(amount)
        print("you bought:", amount, "GHS")
        disp.message(("   Amount Bought:   "), 1)
        disp.message("       " + amount + " Ghs  ", 2)
        time.sleep(5)
        disp.lcd_clear()
        disp.message("    Processing......", 2)
        time.sleep(5)
        disp.lcd_clear()
        electricity = (int(amount) * 11.5)
        print("Consumption: ", electricity, "KWH")
        disp.message((" Elctricity Bundle: "), 1)
        disp.message("         " + str(electricity) + " KWH ", 2)
        time.sleep(10)
        disp.lcd_clear()
        # RFID PROCESS
        disp.message(" Now place your tag ", 1)
        disp.message("     to write.      ", 2)
        text = str(electricity)
        reader.write(text)
        disp.message("     Written!!!     ", 4)
        time.sleep(5)  # Give time for the message to be read
        disp.lcd_clear()

        disp.message("  Place your Card   ", 1)
        disp.message("To Check your Bundle", 2)
        id, text = reader.read()
        disp.message("      Cool!!!       ", 4)
        time.sleep(5)
        disp.lcd_clear()
        disp.message("    Processing......", 2)
        time.sleep(7)
        disp.lcd_clear()
        disp.message("      You Have:     ", 2)
        time.sleep(2)
        disp.lcd_clear()
        disp.message(str(text), 2)
        disp.message("         KWH        ", 3) 
        time.sleep(7)
        disp.lcd_clear()
        disp.message("     Thank you      ", 2)
    elif amount >= account:
        time.sleep(1)
        disp.lcd_clear()
        print("insufficient mount")
        disp.message(("Insufficient Amount"), 2)
        time.sleep(5)
        disp.lcd_clear()
    return start()
if __name__ == '__main__':
    start()




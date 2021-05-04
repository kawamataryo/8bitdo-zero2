#!/usr/bin/python

import Adafruit_PCA9685
from utils.eightbitdo import EightBitDo

# servo move
MOVE_MAX = 600
MOVE_MIN = 350

# servo channel
SERVO_1 = 0
SERVO_2 = 4
SERVO_3 = 6

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)


def action_on_r():
    pwm.set_pwm(SERVO_1, 0, 600)


def action_on_l():
    pwm.set_pwm(SERVO_1, 0, 350)


def main():
    controller = EightBitDo(
        action_on_r=action_on_r,
        action_on_l=action_on_l
    )
    controller.listen()


if __name__ == "__main__":
    main()
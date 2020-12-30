#
# smarsquad.py - SMARS quad robot control
#

import argparse
import logging

import Adafruit_PCA9685


#-------------------------------------------------------------------
# CLASS SmarsQuad
#

class SmarsQuad:

    #
    # Channel layout
    #
    LEFT_FRONT_LEG   = 0
    LEFT_FRONT_FRONT = 1

    RIGHT_FRONT_LEG  = 2
    RIGHT_FRONT_FOOT = 3

    LEFT_BACK_LEG    = 4
    LEFT_BACK_FOOT   = 5

    RIGHT_BACK_LEG   = 6
    RIGHT_BACK_FOOT  = 7


    def __init__ (self):
        self.pwm = Adafruit_PCA9685.PCA9685 ()
        self.pwm.set_pwm_freq (60)

    def reset (self):
        self.set_angle (SmarsQuad.LEFT_FRONT_LEG, 0)
        pass

    def set_angle (self, channel, angle):
        pulse_min = 150
        pulse_max = 600

        self.pwm.set_pwm (channel, 0, pulse_min + int (((pulse_max - pulse_min) * angle) / 180))


    def set_pulse (self, channel, pulse):

        assert channel >= 0 and channel <= 15
        assert pulse >= 0 and pulse <= 4096

        pulse_length = 1000000
        pulse_length //= 60
        pulse_length //= 4000
        pulse *= 1000
        pulse //= pulse_length

        self.pwm.set_pwm (channel, 0, pulse)


#-------------------------------------------------------------------
# MAIN
#

if __name__ == '__main__':

    parser = argparse.ArgumentParser ()
    parser.add_argument ('command')

    args = parser.parse_args ()

    smars = SmarsQuad ()

    if args.command == 'reset':
        smars.reset ()
    else:
        raise RuntimeError (f'Unknown command: {args.command}')



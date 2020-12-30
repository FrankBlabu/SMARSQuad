#
# smarsquad.py - SMARS quad robot control
#

import argparse
import logging

import adafruit_servokit

#-------------------------------------------------------------------
# CLASS SmarsQuad
#

class SmarsQuad:

    #
    # Channel layout
    #
    LEFT_FRONT_LEG   = 0
    RIGHT_FRONT_LEG  = 1
    RIGHT_BACK_LEG   = 2
    LEFT_BACK_LEG    = 3

    LEFT_FRONT_FOOT  = 4
    RIGHT_FRONT_FOOT = 5
    RIGHT_BACK_FOOT  = 6
    LEFT_BACK_FOOT   = 7

    def __init__ (self):
        self.kit = adafruit_servokit.ServoKit (channels=8)

    def reset (self):
        self.set_leg (SmarsQuad.LEFT_FRONT_LEG, 0)
        self.set_leg (SmarsQuad.RIGHT_FRONT_LEG, 0)
        self.set_leg (SmarsQuad.RIGHT_BACK_LEG, 0)
        self.set_leg (SmarsQuad.LEFT_BACK_LEG, 0)

        self.set_leg (SmarsQuad.LEFT_FRONT_FOOT, 0)
        self.set_leg (SmarsQuad.RIGHT_FRONT_FOOT, 0)
        self.set_leg (SmarsQuad.RIGHT_BACK_FOOT, 0)
        self.set_leg (SmarsQuad.LEFT_BACK_FOOT, 0)

    def sit (self):
        self.set_leg (SmarsQuad.LEFT_FRONT_LEG,  0)
        self.set_leg (SmarsQuad.RIGHT_FRONT_LEG, 0)
        self.set_leg (SmarsQuad.LEFT_BACK_LEG,   0)
        self.set_leg (SmarsQuad.RIGHT_BACK_LEG, 0)

    def stand (self):
        self.set_leg (SmarsQuad.LEFT_FRONT_LEG,  90)
        self.set_leg (SmarsQuad.RIGHT_FRONT_LEG, 90)
        self.set_leg (SmarsQuad.LEFT_BACK_LEG,   90)
        self.set_leg (SmarsQuad.RIGHT_BACK_LEG, 90)

    def set_leg (self, leg, angle):
        turned = [SmarsQuad.RIGHT_FRONT_LEG, SmarsQuad.LEFT_BACK_LEG, SmarsQuad.LEFT_FRONT_FOOT]

        if leg in turned:
            angle = 180 - angle

        self.kit.servo[leg].angle = angle


#-------------------------------------------------------------------
# MAIN
#

if __name__ == '__main__':

    parser = argparse.ArgumentParser ()
    parser.add_argument ('-c', '--channel', type=int, default=0, help='Channel to set')
    parser.add_argument ('-a', '--angle',   type=int, default=0, help='Angle to set')
    parser.add_argument ('command')

    args = parser.parse_args ()

    smars = SmarsQuad ()

    if args.command == 'set':
        smars.set_leg (args.channel, args.angle)
    elif args.command == 'reset':
        smars.reset ()
    elif args.command == 'sit':
        smars.sit ()
    elif args.command == 'stand':
        smars.stand ()
    else:
        raise RuntimeError (f'Unknown command: {args.command}')



#!/usr/bin/env python3

import time
import pygame
import os

def ClearScreen():
    os.system('clear')

def Notify(working):
    filename = ''
    if working:
        filename = 'work.wav'
    else:
        filename = 'rest.wav'
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def Update(working, length, mins):
    if working:
        print(length - mins, 'minute(s) of work left...')
    else:
        print(length - mins, 'minute(s) of rest left...')
    return


def WaitMinute():
    time.sleep(60)
    return 1

def Progression(length, working):
    mins = 0
    while mins < length:
        Update(working, length, mins)
        mins += WaitMinute()

def Pomodoro(work_length, rest_length):
    working = True
    while 1:
        ClearScreen()
        Notify(working)
        if working:
            Progression(work_length, working)
        else:
            Progression(rest_length, working)
        working = not working

def main():
    pygame.init()
    work_length = int(input('Minutes of work: '))
    rest_length = int(input('Minutes of rest: '))

    Pomodoro(work_length, rest_length)

main()

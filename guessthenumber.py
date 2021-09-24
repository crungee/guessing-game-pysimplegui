import random
import sys
import PySimpleGUI as sg

# layout the window
layout = [
            [sg.Text('Guess a number from 1 to 20 below:')],
            [sg.Input(expand_x=True)],
            [sg.ReadButton('Ok', bind_return_key=True), sg.ReadButton('New number', key="new")]
            ]

#create the window
window = sg.Window('Guess The Number', grab_anywhere=False).Layout(layout)

number = random.randint(1,20)  # secret number
# event loop
while True:
    event, values = window.Read()

    guess = int(values[0])
    if guess == number:
        sg.popup_quick_message('You guessed it!')
    if guess > number:
        sg.popup_quick_message('Your guess is too high.')
    if guess < number:
        sg.popup_quick_message('Your guess is too low.')
    if event == "new":
        sg.popup_quick_message("New number generated.")
        number = random.randint(1,20)

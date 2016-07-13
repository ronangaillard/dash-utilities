# dash-utilities
Python utilities to play with the Amazon dash button

## Requirements

You should set up your dash button using the Amazon Shopping App on Android or iOs. ( https://www.amazon.com/gp/help/customer/display.html?nodeId=201746340 )  The trick is to quit the app before chosing the product that will be ordered when pressing the button, so that you don't get bankrupt by playing with these scripts !

## How to find your button ?

Run the `scan-network.py` script to look for your button in the network : once you started the script, press the button and look at changes in the terminal.
The MAC address of your button should be displayed !

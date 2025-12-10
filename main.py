def on_button_pressed_a():
    radio.send_string("Message")
    basic.show_string("SENT")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global myNumber, enemyNumber
    myNumber = randint(1, 6)
    radio.send_number(myNumber)
    enemyNumber = randint(1, 6)
    basic.show_string("You:")
    basic.show_number(myNumber)
    basic.show_string(" Enemy:")
    basic.show_number(enemyNumber)
    if myNumber > enemyNumber:
        basic.show_icon(IconNames.HAPPY)
    elif myNumber < enemyNumber:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.B, on_button_pressed_b)

enemyNumber = 0
myNumber = 0
radio.set_group(1)
def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
    if receivedNumber > randomNumber:
        basic.show_icon(IconNames.SAD)
    elif receivedNumber < randomNumber:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.ASLEEP)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("Message")
    basic.show_string("SENT")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def generateEnemyNumber():
    global enemyNumber
    enemyNumber = randint(1, 6)
    radio.send_number(enemyNumber)
    return enemyNumber

def on_button_pressed_b():
    global randomNumber, enemyNumber2
    randomNumber = randint(1, 6)
    basic.show_number(randomNumber)
    enemyNumber2 = generateEnemyNumber()
    radio.send_number(randomNumber)
input.on_button_pressed(Button.B, on_button_pressed_b)

enemyNumber2 = 0
enemyNumber = 0
randomNumber = 0
radio.set_group(1)
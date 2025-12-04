radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    basic.showNumber(receivedNumber)
    if (receivedNumber > randomNumber) {
        basic.showIcon(IconNames.Sad)
    } else if (receivedNumber < randomNumber) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("Message")
    basic.showString("SENT")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
function generateEnemyNumber(): number {
    
    enemyNumber = randint(1, 6)
    radio.sendNumber(enemyNumber)
    return enemyNumber
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    randomNumber = randint(1, 6)
    basic.showNumber(randomNumber)
    enemyNumber2 = generateEnemyNumber()
    radio.sendNumber(randomNumber)
})
let enemyNumber2 = 0
let enemyNumber = 0
let randomNumber = 0
radio.setGroup(1)

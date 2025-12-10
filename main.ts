input.onButtonPressed(Button.A, function () {
    radio.sendString("Hola")
    basic.showString("SENT")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    myNumber = randint(1, 6)
    radio.sendNumber(myNumber)
    enemyNumber = randint(1, 6)
    basic.showString("You:")
    basic.showNumber(myNumber)
    basic.showString(" Enemy:")
    basic.showNumber(enemyNumber)
    if (myNumber > enemyNumber) {
        basic.showIcon(IconNames.Happy)
    } else if (myNumber < enemyNumber) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
let enemyNumber = 0
let myNumber = 0
radio.setGroup(1)

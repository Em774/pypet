# -*- coding: utf-8 -*-

pypet = "/ᐠ_ ꞈ _ᐟ\`"
name = "Kitty"
weight = 3.5
hungry = True
fed = 1

terminate = False

print "Hello, my name is " + name + ", I weigh " + str(weight) + "kg. "+ pypet

while not terminate:
    input = raw_input("$---> ")

    if input == "check":
        if hungry == False:
            print "I am not hungry now"
        elif hungry == True:
            print "What are you waiting for to feed me?"

    elif input == "feed":
        weight = weight + 1
        fed = fed + 1
        if weight <=7:
            print "I now weigh " + str(weight) + "kg."
        if fed == 3:
            hungry = False
            print "I am not hungry anymore"
        if weight == 6.5:
            print "WOOOWWW  are you trying to get me FAT?????"
        if weight == 7.5:
            print "STOOOPP this at once!!!!"
        if weight >= 8:
            weight = weight - 1
            print "NO WAY, let me die overweight in peace!"

    elif input == "exercise":
        if weight <= 1:
            print "I am DEAD, you killed me, you cat KILLER!! What is wrong with you?"
        if weight <= 7:
            weight = weight - 1.5
            lost = 1.5
            print "Yes!! I lost "+ str(lost) + "kg"
            print "My weight is now " + str(weight) + "."
        if weight == 7.5:
            weight = weight - 0.5
            print "Do you really think I am going to run for you after all the food you gave me??"
            print "I lost 0.5kg anyway, just to make you happy, HAPPY???"

    elif input == "quit":
        terminate = True

    else:
        print "Please enter a correct answer"

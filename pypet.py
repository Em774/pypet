# -*- coding: utf-8 -*-
import random
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[90m'

py_cat = {
    'photo': '/ᐠ_ ꞈ _ᐟ\`',
    'name': 'Kitty',
    'weight': 3.5,
    'hungry': True,
    'fed': 1,
    'chat': ["rrrrrrr", "whaaaaaat?", "nomnomnom"],
}

py_dog = {
    'photo': '/0_0\`',
    'name': 'Choupy',
    'weight': 3.5,
    'hungry': True,
    'fed': 1,
    'chat': ["woufff woufff", "Hi there :)", "I am happy!!"],
}

terminate = False

pypet = py_dog

os.system("say 'Welcome to Py pet! Choose the pet you want to play with.'")

print "Dog or Cat?"
choice = raw_input("$---> ")

if choice == "dog" or choice == "Dog":
    pypet = py_dog
    os.system("say 'You have chosen Choupy the dog'")
elif choice == "cat" or choice == "Cat":
    pypet = py_cat
    os.system("say 'You have chosen Kitty the cat'")
else:
    print "Wront input, please try again"

print bcolors.OKBLUE + "Hello, my name is " + pypet['name'] + ", I weigh " + str(pypet['weight']) + "kg. "+ pypet['photo']

os.system("say 'You can now check your pet's status, feed him, make him exercise, make him talk or just quit the game. What would it be?")
while not terminate:
    print bcolors.GREY + "check, feed, exercise, chat, quit"
    input = raw_input(bcolors.HEADER + "$---> ")

    if input == "check":
        if pypet['hungry'] == False:
            print bcolors.OKBLUE + "I am not hungry now"
        elif pypet['hungry'] == True:
            print bcolors.OKBLUE + "What are you waiting for to feed me?"

    elif input == "feed":
        pypet['weight'] = pypet['weight'] + 1
        pypet['fed'] = pypet['fed'] + 1
        if pypet['weight'] <=7:
            print bcolors.OKBLUE + "I now weigh " + str(pypet['weight']) + "kg."
        if pypet['fed'] == 3:
            pypet['hungry'] = False
            print bcolors.OKBLUE + "I am not hungry anymore"
        if pypet['weight'] == 6.5:
            print bcolors.OKBLUE + "WOOOWWW  are you trying to get me FAT?????"
        if pypet['weight'] == 7.5:
            print bcolors.OKBLUE + "STOOOPP this at once!!!!"
        if pypet['weight'] >= 8:
            pypet['weight'] = pypet['weight'] - 1
            print bcolors.OKBLUE + "NO WAY, let me die overweight in peace!"

    elif input == "exercise":
        if pypet['weight'] <= 1:
            print bcolors.OKBLUE + "I am DEAD, you killed me, you cat KILLER!! What is wrong with you?"
        if pypet['weight'] <= 7:
            pypet['weight'] = pypet['weight'] - 1.5
            lost = 1.5
            print bcolors.OKBLUE + "Yes!! I lost "+ str(lost) + "kg"
            print bcolors.OKBLUE + "My weight is now " + str(pypet['weight']) + "kg."
        if pypet['weight'] == 7.5:
            pypet['weight'] = pypet['weight'] - 0.5
            print bcolors.OKBLUE + "Do you really think I am going to run for you after all the food you gave me??"
            print bcolors.OKBLUE + "I lost 0.5kg anyway, just to make you happy, HAPPY???"
        # if pypet['weight'] <=0:
        #     lost = 0
        #     print "I am already dead! Did you want to kill me twice? Lunatic!!!!"

    elif input == "chat":
        print random.choice(pypet['chat'])

    elif input == "quit" or input == "Quit":
        print bcolors.OKGREEN + "Bye Bye!"
        os.system("say 'Bye Bye!'")
        terminate = True

    else:
        print "Please enter a correct answer"

wordofman = input("Enter any word: ")
print(wordofman[::-1])

yourscore = int(input("Enter your score: "))
if yourscore >= 86:
    print("You passed!!!")
else: print("You failed")

randomnumberofyours = int(input("Enter any number: "))
if randomnumberofyours % 2 == 0:
    print(randomnumberofyours, "is even")
else:
    print(randomnumberofyours, "is odd")

light = input('What is the color of the light: ')
if light == 'red': print('Stop')
if light == 'green': print('Drive')
if light == 'yellow' : print('Slow down')

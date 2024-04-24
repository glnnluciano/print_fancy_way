import pyfiglet, sys, time, os

name = str(input("Please input your name: "))
dream_job = str(input("Please eneter your dream job: "))

my_description = ("I am " + name + ". My dream career in the future is to be a/an " + dream_job + ".")

formated_description = pyfiglet.figlet_format(my_description)

for char in formated_description:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.001)
from os import popen
print("A" * 250)
text = popen("echo " + "A" * 250).read()
print(text.split("\n"))
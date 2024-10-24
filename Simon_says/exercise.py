import re

 # Exercise: 
 # Create a function which evaluates a list of commands (written in plain English) if the command begins with Simon says. Return the result as an integer.

def simon_says(list_commands):

    summe = 0

    for command in list_commands:
        if command.startswith("Simon says"):
            if("add" in command):
                zahlen = re.findall(r'\d+', command)
                zahlen = [int(z) for z in zahlen]
                summe += sum(zahlen)
            if("subtract" in command):
                zahlen = re.findall(r'\d+', command)
                zahlen = [int(z) for z in zahlen]
                summe -= sum(zahlen)
            if("multiply" in command):
                zahlen = re.findall(r'\d+', command)
                zahlen = [int(z) for z in zahlen]
                summe *= sum(zahlen)

    return summe




list1 = [
  "Simon says add 4",
  "Simon says add 6",
  "Then add 5"
]    
# Output should be = 10

list2 = [
  "Susan says add 10",
  "Simon says add 3",
  "Simon says multiply by 8"
]  
# Output should be = 24

list3 = [
  "Firstly, add 4",
  "Simeon says subtract 100" # Look at the name closely :)
]
# Output should be = 0




print(simon_says(list1))
print(simon_says(list2))
print(simon_says(list3))

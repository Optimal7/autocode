#AutoCode - Optimal
#Imports
import os
import time

#Variables
divider = '------------------'

#Code
print("AutoCode")
print(divider)
time.sleep(1)

#Project Name
while True:
    print("Choose a name for your project.")
    file = input()
    project_name = file

    if not file.strip():
        print("You need to type a valid project name.")
        time.sleep(2)

    else:
        file = file.replace(" ", "_")
        #break

    try:
        #Creates File
        project_create = open(f"projects/{file}.py", "x+")
        project_create.close()

        #Adds a comment into the file
        project_file = open(f"projects/{file}.py", "w")
        project_file.write(f"#{project_name} - AutoCode \n")
        project_file.close()
        break

    except:
        print("File already exists! Please make a new file.")
        time.sleep(2)


print("Continuing in 2 seconds.")
time.sleep(2)
os.system('CLS')

#Code "Chunks"
#Text
def text(string):
    code = f"""
#Text
print("{string}")
    """
    project_file = open(f"projects/{file}.py", "a")
    project_file.write(code)
    project_file.close()
    print("Added Text.")

#Variable
def variable(var_name, var_content):
    code = f"""
#Variable
{var_name} = "{var_content}"
    """
    project_file = open(f"projects/{file}.py", "a")
    project_file.write(code)
    project_file.close()
    print("Added Variable.")

def inputc(var_name, input_resp):
    code = f"""
#Input/Question
{var_name} = input("{input_resp} > ")
"""
    project_file = open(f"projects/{file}.py", "a")
    project_file.write(code)
    project_file.close()
    print("Added Input.")

#Actual program
while True:
    options = [1, 2, 3]
    option_list = """> OPTIONS <
[1] Text
[2] Variable
[3] Input
    """

    #Input
    print("Select a option. Note: The Options are explained in the Readme.")
    print(option_list)
    try:
        option = int(input("> "))

    except:
        print("Invalid Option")
        time.sleep(1)

    if option not in options:
        print("Invalid Option")
        time.sleep(1)

    #Text Option
    if option == 1:
        print("Select a text to be displayed.")
        string = input()
        text(string)
        time.sleep(1)
        os.system('CLS')

    #Variable
    if option == 2:
        print("Select the variable name.")
        var_name = input()
        print("Select the value of the variable.")
        var_content = input()
        variable(var_name, var_content)
        time.sleep(1)
        os.system('CLS')

    #Input
    if option == 3:
        print("Select the variable name.")
        var_name = input()
        print("Select the question to get the value of the variable.")
        var_input = input()
        inputc(var_name, var_input)
        time.sleep(1)
        os.system('CLS')


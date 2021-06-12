"""
TASK
#####
Create a program that will receive commands until the command "End".    The commands can be:
############################################################################################
"Create-{file_name}" :
Creates the given file with an empty content.
If the file already exists, remove the existing text in it (as if the file is created again)
###########################################################################################
"Add-{file_name}-{content}" :
Append the content and a new line after it.
If the file does not exist, create it, and add the content
###########################################################
"Replace-{file_name}-{old_string}-{new_string}" :
Open the file and replace all the occurrences of the old string with the new string. If the file does not exist, print:
"An error occurred"
#############################################################################################
"Delete-{file_name}" :
Delete the file. If the file does not exist, print:
"An error occurred"
"""
import os

command_me = input()

while not command_me == "End":
    line = command_me

    if line.startswith("Create"):
        _, file_to_create = line.split("-")
        file_name = file_to_create
        with open(file_name, "w") as file:
            file.close()

    elif line.startswith("Add"):
        _, file_name, line_to_add = line.split("-")
        with open(file_name, "a") as file:
            file.writelines(line_to_add)

    elif line.startswith("Replace"):
        _, file_name, old_string, new_string = line.split("-")
        new_string = new_string

        try:
            with open(file_name, "r+") as file:
                content = "\n".join(file.readlines())
                replaced_strings = content.replace(old_string, new_string)
                file.seek(0), file.truncate(), file.writelines(replaced_strings)  # same as a on new lines
                # .seek(0) = position at start; .truncate() clears all after position = 0 (.seek(0))
                # this is how i managed the extra new lines
                #
                # uncomment following lines to add a log file, to see result of the deleted file
                #
                with open("log_file.txt", "a+") as log:
                    log.seek(0), log.truncate(), log.writelines(replaced_strings)

        except FileNotFoundError:
            print("An error occurred")

    elif line.startswith("Delete"):
        _, file_to_delete = line.split("-")
        file_name = file_to_delete

        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command_me = input()

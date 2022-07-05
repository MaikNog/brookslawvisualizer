# TODO Write Readme with purpose and instructions
# TODO Explain all print statements as debug infos
# TODO Write loading bar for higher team size rendering time in terminal?
# TODO Explain why i wrote the graph (e.g. no variables can be used directly in dot notation)
# TODO Make the user chose rendering algorithm (default is circo)
# TODO Why / how did I choose Python and GraphViz/dot? Research, article links, little programming knowledge etc.
# TODO Make a warning if user choses large team size. Its not forecastable how long the rendering will take.
# TODO Team size 100 takes >10 minutes to render? Team Size 30 took 10 seconds; team size 40 took 2 min
# TODO Make Readme also with Graph example of different algos? Keep 100 image
# TODO How to test it?
# TODO Write down the software requirements (GraphViz, Python3)
# TODO Ask for input number… warning when bigger than 40. If Yes, than go with it
# TODO Write a ReWrite Tech blog post
# TODO Add team size + comm lines in image


# Variable declaration block
team_size = 2
iteration = 1
total_list = []
team_list = []

# User Input dialogue
# With validation check if input is an integer
# Made it a def block
# TODO Need an exit break to avoid endless loop in unit test
def user_input_team_size():
    IsNotAnInteger = True
    input_value = None
    while IsNotAnInteger:
        input_value = input("Please input a team size: ")
        match_val = re.match("[-+]?\\d+$", input_value)
        if match_val is None:
            print("Please enter a valid integer.")
        else:
            IsNotAnInteger = False
    return int(input_value)

# Feeding the input from def function to variable
team_size = user_input_team_size()

# Create list with elements from team_size, e.g. team_size=4 has list (1, 2, 3, 4)
# Need to set team_size+1 since <list> count start with 0
def fill_team_list():
    for i in range(1, team_size+1):
        team_list.append(int(i))
    return team_list

fill_team_list()

# TODO TIL that i had unused code (total_list function), which i didnt need in the end.
# Maybe I worked on it one day and by next day I had a different approach
# Unused code was working, but not called or needed

# Create a GraphViz GV file in current directory
fp = open('brookslawvisualizer.gv', 'w')

# Opening bracket of file and graph name
fp.write('graph Brookslawvisualizer {')
fp.write('\n')

# Duplicate created team_list to iterate through
team_list_duplicate = team_list

# Create the graph entries for the GV file with content from team_list
# We iterate and compare the 1st list (team_list) with all entries in 2nd list (team_list_duplicate)
# If it is lesser, we create an entry for the Graphviz GV file
#
# Example:
# team_size=3 has list (1, 2, 3) & team_list_duplicate has list (1, 2, 3)
# 1 >= 1 // skip
# 1 >= 2 // write: 1 -- 2
# 1 >= 3 // write: 1 -- 3
# 2 >= 1 // skip
# 2 >= 2 // skip
# 2 >= 3 // write: 2 -- 3
# 3 >= 1 // skip
# 3 >= 2 // skip
# 3 >= 3 // skip

for item in team_list:
    for item2 in team_list_duplicate:
        if item >= item2:
            pass
        else:
            fp.writelines(str(item) + " -- " + str(item2) +'\n')

# End of content from team_list

# Closing bracket in last line of file and closing the file
fp.write('\n')
fp.write('}')
fp.close()

# Execute the DOT command in the terminal to create the dot graph image "output.png"
# Careful! The drawing of the image takes longer, the higher the team size.

# TODO When making it a program, make it user option to disable drawing
# TODO Make the gv and png filenames as variables
bashCommand = "circo -Tpng brookslawvisualizer.gv -o brookslawvisualizer.png"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
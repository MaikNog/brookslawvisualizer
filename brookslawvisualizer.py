# TODO Write Readme with purpose and instrcutions
# TODO Explain all print statements as debug infos
# TODO Write comment to each block and explain what it does
# TODO Write loading bar for higher team size rendering time in terminal?
# TODO Explain why i wrote the graph (e.g. no variables can be used directly in dot notation)
# TODO Make the user chose rendering algorithm (default is circo)

team_size = 10
iteration = 1

total_list = []
team_list = []

# TODO Make the debug/print statements enabled by replacing text? #print for print ?
#print("team_size:", team_size)

# Create list with elements from team_size
# e.g. team_size=4 has list (1, 2, 3, 4)

# Need to set team_size+1 since list count start with 0
for i in range(1, team_size+1):
    team_list.append(int(i))
#print("team list :", team_list)

while iteration < team_size:
    repetition = team_size - iteration
    new_list = [iteration] * repetition
    total_list += new_list
    iteration += 1
#print("total_list :", total_list)

# Duplicate created team_list to iterate through
team_list_duplicate = team_list
#print("team_list_duplicate :", team_list_duplicate)
#print("=======================")

# create a GraphViz GV file from the total_list in current directory
fp = open('brookslawvisualizer.gv', 'w')

# Opening definition and bracket of file
fp.write('graph MyGraph {')
fp.write('\n')

# Content from team_list
for item in team_list:
    #print("item", item)
    for item2 in team_list_duplicate:
        #print("item2", item2)
        if item >= item2:
            pass
            #print("Was equal or greater", item, item2)
        else:
            #print("Was lesser", item, item2)
            fp.writelines(str(item) + " -- " + str(item2) +'\n')

# End of content from team_list

# Closing bracket in last line of file
fp.write('\n')
fp.write('}')
fp.close()

# Execute the DOT command in the terminal to create the dot graph image "output.png"
# Careful! The drawing of the image takes longer, the higher the team size.

# TODO When making it a progam, make it user option to disable drawing
import subprocess

# TODO Make the gv and png filenames as variables
bashCommand = "circo -Tpng brookslawvisualizer.gv -o brookslawvisualizer.png"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
team_size = 3
iteration = 1

total_list = []
team_list = []
team_list_duplicate = []

print("team_size:", team_size)

# Create list with elements from team_size
# e.g. team_size=4 has list (1, 2, 3, 4)

# Need to set team_size+1 since list count start with 0
for i in range(1, team_size+1):
    team_list.append(int(i))
print("team list :", team_list)

while iteration < team_size:
    repetition = team_size - iteration
    new_list = [iteration] * repetition
    total_list += new_list
    iteration += 1
print("total_list :", total_list)

# create a GV file from the total_list in current directory
fp = open('input.gv', 'w')

# Opening definition and bracket of file
fp.write('graph Brooks Law Visualizer {')
fp.write('\n')

# Content

# Duplicate created team_list to iterate through
team_list_duplicate = team_list
print("team_list_duplicate :", team_list_duplicate)
print("=======================")

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


# End of content

# Closing bracket in last line of file
fp.write('\n')
fp.write('}')
fp.close()


# Execute the DOT command in the terminal to create the dot graph image "output.png"
import subprocess

bashCommand = "dot -Tpng brookslawvisualizer.gv -o brookslawvisualizer.png"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
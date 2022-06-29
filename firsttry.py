team_size = 3
iteration = 1

total_list_count = 0
total_list = []
team_list = []

print("team_size:", team_size)
# Create list with elements from team_size in reverse order (range syntax)
# e.g. team_size=4 has list (4, 3, 2, 1)
for i in range(team_size, 0, -1):
    team_list.append(int(i))
print("team list :", team_list)

while iteration < team_size:
    repetition = team_size - iteration
    new_list = [iteration] * repetition

    total_list_count += len(new_list)
    total_list += new_list
    iteration += 1
print("total_list :", total_list)

# create a GV file from the total_list in current directory
fp = open('input.gv', 'w')

# Opening definition and bracket of file
fp.write('graph MyGraph {')
fp.write('\n')

# Content from total_list
for items in total_list:
    fp.writelines(str(items) + " -- " + "2" +'\n')

# replace 2 with connecting teamnumber thingy




# End of content from total_list

# Closing bracket in last line of file
fp.write('\n')
fp.write('}')
fp.close()

# Execute the DOT command in the terminal to create the dot graph image "output.png"
import subprocess

bashCommand = "dot -Tpng input.gv -o output.png"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
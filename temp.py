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

"""" Idea
for each list_entry iterate through the team_list entries
Check if list_entry is greater or equal with the team_list entry, then skip

for each... iteration durch new_list!
    if new_list_item > team_list
        doch nicht reversed!!
        1, 1, 2      =<   1, 2, 3
        fp.writelines(str(items) + " -- " + team_list_item" +'\n') 
        
        teamsize 3
        team list 1,2,3
        new_list 1,1,2
        
        1 => 2
        1 => 3
        2 => 3
"""


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
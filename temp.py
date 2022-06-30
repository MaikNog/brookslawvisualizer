team_size = 5
iteration = 1

total_list_count = 0
total_list = []
team_list = []

print("team_size:", team_size)

# Create list with elements from team_size
# e.g. team_size=4 has list (4, 3, 2, 1)
for i in range(1, team_size+1):
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

# helper variable to increase team_list position
tlentry = 0
for item in total_list:
    if item <= team_list[tlentry]:
        #continue
        #print("teamlist element:", team_list[0])
        #print("item is less or equal than team_list element")
        #print("item", item)
        print("If", "node_1:", item, "node_2:", team_list[tlentry])
        #fp.writelines(str(item) + " -- " + str(team_list[tlentry]) +'\n')
    else:
        #print("teamlist element:", team_list[0])
        #print("item is greater than team_list element")
        #print("item", item)
        print("Else", "node_1:", item, "node_2:", team_list[tlentry])
    if tlentry < len(team_list)-1:
        tlentry = tlentry + 1
    print(tlentry)

# !! problem: tlentry is counted up to 5 with first four 1 item in total_list
# !! tlentry needs to reset
# !! tlentry X needs to iterate to ALL total_list entries, then reset

""" today i learned / observed myself:
running the print output helped me visualize my thought flow.
Also having an actual example written in excel (on paper) helped.
In excel was the mathematical solution/example
"""

#    fp.writelines(str(item) + " -- " + "2" +'\n')

# replace 2 with connecting teamnumber thingy

"""" Idea
for each list_entry iterate through the team_list entries
Check if list_entry is lesser or equal with the team_list entry, then skip

for each... iteration durch new_list!
    if new_list_item > team_list
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
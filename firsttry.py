"""
n*(n-1)/2

Get input variable "team member"
Save input to variable "team member"
Calculate "lines of communication"
Save calc result to variable "lines of communication"

how to build up all possible connections?

erste serie ist 6-1 wiederholt (1,1,1,1,1)
Folgeserien sind 6-2, dann 6-3, dann 6-4, dann 6-5
oder: team_size – iteration (faengt bei 1 an)

Nummer=1
while iteration < team_size ..
    do repeat iteration (team_size – iteration)
print iteration
iteration+
"""


"""
6 -> 15
7 -> 21

*5	10		*6	15

1		2
1		3
1		4
1		5
1		6
			2		3
			2		4
			2		5
			2		6
				3		4
					3		5
					3		6
						4		5
						4		6
							5		6
"""

#team_size = 6
team_size = 3
iteration = 1

total_list_count = 0
total_list = []

#print("team_size", "number", "repetition")
print("team_size:", team_size)
print(" ")
while iteration < team_size:
    repetition = team_size - iteration
    new_list = [iteration] * repetition

    #print(team_size, iteration, repetition)
    #print("iteration, repetition :", iteration, repetition, " ==> ", "new_list :", new_list)

    #print(len(new_list), "==>", new_list)
    #print(new_list)

    total_list_count += len(new_list)
    #print(total_list_count)

    total_list += new_list

    iteration += 1
print(" ")
print("total_list :", total_list)

# create a GV file from the total_list
# in current directory
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
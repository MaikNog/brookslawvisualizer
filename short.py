team_size = 3
iteration = 1
total_list_count = 0
total_list = []
team_list = []
team_list_duplicate = []

#print("team_size:", team_size)
for i in range(1, team_size+1):
    team_list.append(int(i))
print("team list :", team_list)

while iteration < team_size:
    repetition = team_size - iteration
    new_list = [iteration] * repetition
    total_list += new_list
    iteration += 1
#print("total_list :", total_list)

# Duplicate created team_list to iterate through
team_list_duplicate = team_list
print("team_list_duplicate :", team_list_duplicate)
print("=======================")

for item in team_list:
    #print("item", item)

    for item2 in team_list_duplicate:
        #print("item2", item2)

        if item >= item2:
            print("Was equal or greater", item, item2)
        else:
            print("Was lesser", item, item2)


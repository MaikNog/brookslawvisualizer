"""
n*(n-1)/2

erste serie ist 6-1 wiederholt (1,1,1,1,1)
Folgeserien sind 6-2, dann 6-3, dann 6-4, dann 6-5
oder: team_size – iteration (faengt bei 1 an)

"""
team_size = 5
iteration = 1

total_list_count = 0
total_list = []

# Create list with elements from team_size in reverse order (range syntax)
# e.g. team_size=4 has list (4, 3, 2, 1)

print("team list")
team_list = []
for i in range(team_size, 0, -1):
    team_list.append(int(i))
print(team_list)



print("iteration", " ==> ", "new_list")

while iteration < team_size:
    repetition = team_size - iteration
    new_list = [iteration] * repetition

    #print(iteration)
    #print(team_size, iteration, repetition)
    #print("iteration, repetition :", iteration, repetition, " ==> ", "new_list :", new_list)

    #print(len(new_list), "==>", new_list)
    #print(new_list)
    print(iteration, " ==> ", new_list)

    total_list_count += len(new_list)
    #print(total_list_count)

    total_list += new_list

    iteration += 1
#print(" ")
#print("total_list :", total_list)
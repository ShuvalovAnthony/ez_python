f = open("Mihail/26/Baranov/26var01.txt")


num_of_teams, num_of_aircrafts = [int(i) for i in f.readline().split()]


data = [int(i) for i in f]

teams = sorted(data[:num_of_teams])
capacities = sorted(data[num_of_teams:])

counter = 0
max_team_size = 0
last_capacity_index = -1

print(len(teams), len(capacities))

for team_index in range(len(teams)):
    team = teams[team_index]
    temp_capacity = 0

    for capacity_index in range(last_capacity_index + 1, len(capacities)):
        temp_capacity += capacities[capacity_index]

        if temp_capacity >= team:
            counter += 1
            max_team_size = team
            last_capacity_index = capacity_index
            break

        
    # print(counter, team, capacity_index, capacities[capacity_index])

print(capacities[last_capacity_index:])
print(temp_capacity, teams[::-1][:5])
print(counter, max_team_size)
        



import matplotlib.pyplot as plt

def calculate_costs(num_days, num_teams):
    consumables_cost_per_day = 30
    accommodation_cost_per_day = 300
    meals_cost_per_day = 300

    total_consumables_cost = num_days * num_teams * consumables_cost_per_day
    total_accommodation_cost = num_days * accommodation_cost_per_day
    total_meals_cost = num_days * meals_cost_per_day

    total_cost = total_consumables_cost + total_accommodation_cost + total_meals_cost

    return total_cost

# List of days and teams to iterate over
days_list = [3, 5, 11]
teams_list = [2, 4, 10]

# Prepare data for the graph
costs = []
for num_teams in teams_list:
    team_costs = []
    for num_days in days_list:
        total_cost = calculate_costs(num_days, num_teams)
        team_costs.append(total_cost)
    costs.append(team_costs)

# Create the graph
for i in range(len(teams_list)):
    plt.plot(days_list, costs[i], label=f'{teams_list[i]} teams')

plt.xlabel('Number of Days')
plt.ylabel('Total Cost')
plt.title('Total Cost for Different Number of Teams and Days')
plt.legend()
plt.show()

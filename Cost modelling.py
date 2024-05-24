import matplotlib.pyplot as plt
import numpy as np

# Constants from Script 1
NUM_PEOPLE_PER_TEAM = 2
CONSUMABLES_COST_PER_DAY = 30
ACCOMMODATION_COST_PER_PERSON_PER_DAY = 150
MEALS_COST_PER_PERSON_PER_DAY = 100

# Constants from Script 2
Data_time = 0.25
Number_of_Plots_per_Day = 3
Travel_Days_to_Site = 2
No_of_People_Team = 2.0

# Costs function from Script 1
def calculate_costs(num_teams, days_available):
    total_consumables_cost = CONSUMABLES_COST_PER_DAY * days_available
    total_accommodation_cost = ACCOMMODATION_COST_PER_PERSON_PER_DAY * NUM_PEOPLE_PER_TEAM * num_teams * days_available
    total_meals_cost = MEALS_COST_PER_PERSON_PER_DAY * NUM_PEOPLE_PER_TEAM * num_teams * days_available
    total_cost = total_consumables_cost + total_accommodation_cost + total_meals_cost
    cost_per_day = total_cost / days_available
    return cost_per_day

# Data from Script 2
Number_plots = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
Total_no_People_options = [2, 4, 14]

# Initialize dictionaries to store the results for comparison
costs_dict = {}
blocks_dict = {}
staff_days_dict = {}
costs_per_individual_day_dict = {}

# Iterate through the number of people options
for Total_no_People in Total_no_People_options:
    # Adjust Number_days_available based on Total_no_People
    Number_days_available = 3 if Total_no_People < 10 else 5
    Number_of_Teams = Total_no_People / No_of_People_Team
    cost_per_day = calculate_costs(Number_of_Teams, Number_days_available)

    # Initialize lists to store the results
    total_cost_list = []
    no_of_blocks_required_list = []
    total_staff_days_list = []
    costs_per_individual_day_list = []

    # Iterate through the number of plots
    for plots in Number_plots:
        Days_Required_for_Plots = plots / (Number_of_Teams * Number_of_Plots_per_Day)
        No_of_Blocks_Required = np.ceil(Days_Required_for_Plots / Number_days_available)
        Safety_days = Days_Required_for_Plots
        Data_days = Days_Required_for_Plots * Data_time * Number_of_Teams
        Travel_days_forcampaign = Travel_Days_to_Site * No_of_Blocks_Required
        Traveldays_all_teams = Travel_days_forcampaign + Total_no_People
        Staff_days = Total_no_People * Days_Required_for_Plots
        Total_staff_days = Staff_days + Traveldays_all_teams + Data_days + Traveldays_all_teams + Safety_days
        Total_cost = Total_staff_days * cost_per_day
        Cost_per_individual_day = cost_per_day / Total_no_People

        # Append the results to the lists
        total_cost_list.append(Total_cost)
        no_of_blocks_required_list.append(No_of_Blocks_Required)
        total_staff_days_list.append(Total_staff_days)
        costs_per_individual_day_list.append(Cost_per_individual_day)

    # Store the results in the dictionaries
    costs_dict[Total_no_People] = total_cost_list
    blocks_dict[Total_no_People] = no_of_blocks_required_list
    staff_days_dict[Total_no_People] = total_staff_days_list
    costs_per_individual_day_dict[Total_no_People] = costs_per_individual_day_list

# Plotting
plt.figure(figsize=(14, 10))

# Plot for Total Cost
plt.subplot(2, 2, 1)
for Total_no_People, costs in costs_dict.items():
    plt.plot(Number_plots, costs, marker='o', label=f'Total People: {Total_no_People}')
plt.title('Total Cost by Number of Plots')
plt.xlabel('Number of Plots')
plt.ylabel('Total Cost ($)')
plt.legend()

# Plot for Number of Blocks Required
plt.subplot(2, 2, 2)
for Total_no_People, blocks in blocks_dict.items():
    plt.plot(Number_plots, blocks, marker='o', label=f'Total People: {Total_no_People}')
plt.title('Number of Blocks Required by Number of Plots')
plt.xlabel('Number of Plots')
plt.ylabel('Number of Blocks Required')
plt.legend()

# Plot for Total Staff Days
plt.subplot(2, 2, 3)
for Total_no_People, staff_days in staff_days_dict.items():
    plt.plot(Number_plots, staff_days, marker='o', label=f'Total People: {Total_no_People}')
plt.title('Total Staff Days by Number of Plots')
plt.xlabel('Number of Plots')
plt.ylabel('Total Staff Days')
plt.legend()

# Bar Chart for Costs per Individual Day
plt.subplot(2, 2, 4)
bar_width = 0.25
bar_index = np.arange(len(Number_plots))
colors = ['r', 'g', 'b']

for i, Total_no_People in enumerate(Total_no_People_options):
    plt.bar(bar_index + i * bar_width, costs_per_individual_day_dict[Total_no_People], width=bar_width, color=colors[i], label=f'Total People: {Total_no_People}')

plt.title('Costs per Individual Day by Number of Plots')
plt.xlabel('Number of Plots')
plt.ylabel('Cost per Individual Day ($)')
plt.xticks(bar_index + bar_width, Number_plots)
plt.legend()

plt.tight_layout()
plt.show()

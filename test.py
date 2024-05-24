import matplotlib.pyplot as plt
import numpy as np

# Start Variables
Number_plots = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
Total_no_People_options = [2, 4, 14]

# Constants
Data_time = 0.25
Number_of_Plots_per_Day = 3
Travel_Days_to_Site = 2
No_of_People_Team = 2.0

# Costing Variables
Accommodation_per_day = 200
Meals_per_day = 150
Consumables_per_day = 50

# Initialize dictionaries to store the results for comparison
comparison_dict = {}
cost_comparison_dict = {}
cost_per_plot_dict = {}

# Iterate through the number of people options
for Total_no_People in Total_no_People_options:
    # Adjust Number_days_available based on Total_no_People
    Number_days_available = 3 if Total_no_People < 10 else 5

    # Adjust costing variables based on Number_days_available
    if Number_days_available == 3:
        Accommodation_cost = Accommodation_per_day * 4
        Meals_cost = Meals_per_day * 4.5
        Consumables_cost = Consumables_per_day * 4.5
    else:
        Accommodation_cost = Accommodation_per_day * Number_days_available
        Meals_cost = Meals_per_day * Number_days_available
        Consumables_cost = Consumables_per_day * Number_days_available

    # Calculated Variables
    Number_of_Teams = Total_no_People / No_of_People_Team
    total_plots_per_day = Number_of_Teams * Number_of_Plots_per_Day
    Cost_per_day_per_team = (Accommodation_cost + Meals_cost + Consumables_cost) * Number_of_Teams

    # Initialize lists to store the results
    total_staff_days_list = []
    no_of_blocks_required_list = []
    total_cost_list = []
    cost_per_plot_list = []

    # Iterate through the number of plots
    for plots in Number_plots:
        Days_Required_for_Plots = plots / total_plots_per_day
        No_of_Blocks_Required = np.ceil(Days_Required_for_Plots / Number_days_available)
        Safety_days = Days_Required_for_Plots
        Data_days = Days_Required_for_Plots * Data_time * Number_of_Teams
        Travel_days_forcampaign = Travel_Days_to_Site * No_of_Blocks_Required
        Traveldays_all_teams = Travel_days_forcampaign + Total_no_People
        Staff_days = Total_no_People * Days_Required_for_Plots
        Total_staff_days = Staff_days + Traveldays_all_teams + Data_days + Traveldays_all_teams + Safety_days

        Cost_per_block = Cost_per_day_per_team * Number_days_available
        Total_cost = Cost_per_block * No_of_Blocks_Required
        Cost_per_plot = Total_cost / plots

        # Append the results to the lists
        total_staff_days_list.append(Total_staff_days)
        no_of_blocks_required_list.append(No_of_Blocks_Required)
        total_cost_list.append(Total_cost)
        cost_per_plot_list.append(Cost_per_plot)

    # Store the results in the comparison dictionaries
    comparison_dict[Total_no_People] = (total_staff_days_list, no_of_blocks_required_list)
    cost_comparison_dict[Total_no_People] = total_cost_list
    cost_per_plot_dict[Total_no_People] = cost_per_plot_list

    # Print cost per person and per team
    Cost_per_person = Cost_per_day_per_team / Total_no_People
    print(f"Total no. of People: {Total_no_People}")
    print(f"Cost per person per day: {Cost_per_person}")
    print(f"Cost per team per day: {Cost_per_day_per_team}")

    # Plotting for each Total_no_People
    plt.figure(figsize=(14, 7))

    # Total staff days plot
    plt.subplot(1, 3, 1)
    plt.plot(Number_plots, total_staff_days_list, marker='o', label=f'Total People: {Total_no_People}')
    plt.title('Total Staff Days per Number of Plots')
    plt.xlabel('Number of Plots')
    plt.ylabel('Total Staff Days')
    plt.legend()

    # Number of blocks required plot
    plt.subplot(1, 3, 2)
    plt.plot(Number_plots, no_of_blocks_required_list, marker='o', color='red', label=f'Total People: {Total_no_People}')
    plt.title('Number of Blocks Required per Number of Plots')
    plt.xlabel('Number of Plots')
    plt.ylabel('Number of Blocks Required')
    plt.legend()

    # Cost per plot plot
    plt.subplot(1, 3, 3)
    plt.plot(Number_plots, cost_per_plot_list, marker='o', color='green', label=f'Total People: {Total_no_People}')
    plt.title('Cost per Plot')
    plt.xlabel('Number of Plots')
    plt.ylabel('Cost per Plot ($)')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Final comparison plot for Total Staff Days, Number of Blocks Required, Cost per Plot, and Total Cost
plt.figure(figsize=(18, 7))

# Total staff days comparison plot
plt.subplot(1, 4, 1)
for Total_no_People, (staff_days, _) in comparison_dict.items():
    plt.plot(Number_plots, staff_days, marker='o', label=f'Total People: {Total_no_People}')
plt.title('Comparison of Total Staff Days')
plt.xlabel('Number of Plots')
plt.ylabel('Total Staff Days')
plt.legend()

# Number of blocks required comparison plot
plt.subplot(1, 4, 2)
for Total_no_People, (_, blocks_required) in comparison_dict.items():
    plt.plot(Number_plots, blocks_required, marker='o', label=f'Total People: {Total_no_People}')
plt.title('Comparison of Number of Blocks Required')
plt.xlabel('Number of Plots')
plt.ylabel('Number of Blocks Required')
plt.legend()

# Cost per plot comparison plot
plt.subplot(1, 4, 3)
for Total_no_People, cost_per_plot in cost_per_plot_dict.items():
    plt.plot(Number_plots, cost_per_plot, marker='o', label=f'Total People: {Total_no_People}')
plt.title('Comparison of Cost per Plot')
plt.xlabel('Number of Plots')
plt.ylabel('Cost per Plot ($)')
plt.legend()

# Total cost comparison plot
plt.subplot(1, 4, 4)
for Total_no_People, total_cost in cost_comparison_dict.items():
    plt.plot(Number_plots, total_cost, marker='o', label=f'Total People: {Total_no_People}')
plt.title('Comparison of Total Cost')
plt.xlabel('Number of Plots')
plt.ylabel('Total Cost ($)')
plt.legend()

plt.tight_layout()
plt.show()


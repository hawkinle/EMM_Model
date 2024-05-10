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

# Initialize a dictionary to store the results for comparison
comparison_dict = {}

# Iterate through the number of people options
for Total_no_People in Total_no_People_options:
    # Adjust Number_days_available based on Total_no_People
    Number_days_available = 3 if Total_no_People < 10 else 5

    # Calculated Variables
    Number_of_Teams = Total_no_People / No_of_People_Team
    total_plots_per_day = Number_of_Teams * Number_of_Plots_per_Day

    # Initialize lists to store the results
    total_staff_days_list = []
    no_of_blocks_required_list = []

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

        # Append the results to the lists
        total_staff_days_list.append(Total_staff_days)
        no_of_blocks_required_list.append(No_of_Blocks_Required)

    # Store the results in the comparison dictionary
    comparison_dict[Total_no_People] = total_staff_days_list

    # Plotting for each Total_no_People
    plt.figure(figsize=(14, 5))

    # Total staff days plot
    plt.subplot(1, 2, 1)
    plt.plot(Number_plots, total_staff_days_list, marker='o', label=f'Total People: {Total_no_People}')
    plt.title('Total Staff Days per Number of Plots')
    plt.xlabel('Number of Plots')
    plt.ylabel('Total Staff Days')
    plt.legend()

    # Number of blocks required plot
    plt.subplot(1, 2, 2)
    plt.plot(Number_plots, no_of_blocks_required_list, marker='o', color='red', label=f'Total People: {Total_no_People}')
    plt.title('Number of Blocks Required per Number of Plots')
    plt.xlabel('Number of Plots')
    plt.ylabel('Number of Blocks Required')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Final comparison plot for Total Staff Days
plt.figure(figsize=(10, 5))
for Total_no_People, staff_days in comparison_dict.items():
    plt.plot(Number_plots, staff_days, marker='o', label=f'Total People: {Total_no_People}')
plt.title('Comparison of Total Staff Days')
plt.xlabel('Number of Plots')
plt.ylabel('Total Staff Days')
plt.legend()
plt.show()

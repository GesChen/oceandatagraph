import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV
df = pd.read_csv('data.csv')

# Set Consolas as the default font
plt.rcParams['font.family'] = 'Consolas'

# Scatter plot with color based on 'Annual anomaly'
plt.figure(figsize=(8, 6))  # Adjust the figure size if needed

# Set a dark theme using seaborn
sns.set(style="darkgrid")

# Set the background color of the entire figure to black
fig, ax = plt.subplots(facecolor='black')

# Scatter plot with color based on 'Annual anomaly' values
scatter_plot = ax.scatter(df['Year'], df['Annual anomaly'], c=df['Annual anomaly'], cmap='coolwarm', vmin=-1, vmax=1)

# Add colorbar
cbar = plt.colorbar(scatter_plot, label='Annual Anomaly')

# Set labels and title with white color
ax.set_xlabel('Year', color='white')
ax.set_ylabel('Annual Anomaly', color='white')
ax.set_title('Scatter Plot of Annual Anomaly Over Years', color='white')

# Customize colorbar ticks and labels with white color
cbar.set_ticks([-1, -0.5, 0, 0.5, 1])
cbar.set_ticklabels(['-1', '-0.5', '0', '0.5', '1'])
cbar.ax.yaxis.label.set_color('white')
cbar.ax.tick_params(color='white', labelcolor='white')

# Customize tick colors to white
ax.tick_params(axis='both', colors='white')

# Show the plot
plt.show()

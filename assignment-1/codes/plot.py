import numpy as np
import matplotlib.pyplot as plt

# Read angle from output.tex
with open('output.tex', 'r') as f:
    angle_line = f.readline()
    angle = float(angle_line.split(':')[0].strip().replace('degrees', ''))

# Define speeds
rain_speed = 35  # m/s (downward)
wind_speed = 12  # m/s (east to west)

# Create vectors
rain_vector = np.array([0, -rain_speed])
wind_vector = np.array([-wind_speed, 0])
umbrella_vector = np.array([-wind_speed, -rain_speed]) / np.sqrt(wind_speed**2 + rain_speed**2) * 35  # Scale to rain speed

# Plotting
plt.quiver(0, 0, rain_vector[0], rain_vector[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Rain (35 m/s)')
plt.quiver(0, 0, wind_vector[0], wind_vector[1], angles='xy', scale_units='xy', scale=1, color='green', label='Wind (12 m/s)')
plt.quiver(0, 0, umbrella_vector[0], umbrella_vector[1], angles='xy', scale_units='xy', scale=1, color='red', label='Umbrella Direction')

# Annotations
plt.text(0.5, -10, f'Rain: {rain_speed} m/s', color='blue', fontsize=10)
plt.text(-10, -2, f'Wind: {wind_speed} m/s', color='green', fontsize=10)
plt.text(5, -15, f'angle made by resultant vector \nwith west direction: {90-angle:.2f}°', color='red', fontsize=10)

# Set limits and labels
plt.xlim(-20, 10)
plt.ylim(-40, 5)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('Vectors of Rain, Wind, and their resultant')
plt.xlabel('Horizontal (East)')
plt.ylabel('Vertical (Downward)')
plt.grid()
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('vector_plot.png')  # Save the plot as a PNG file
plt.show()

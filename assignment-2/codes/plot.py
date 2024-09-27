import numpy as np
import matplotlib.pyplot as plt

# Load points from the output.txt file
points = np.loadtxt('output.txt')

# Extract x, y, z coordinates
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(x, y, z, color='red', s=100)

# Plot lines connecting the points
ax.plot(x, y, z, color='blue')

# Label the points A, B, C with their coordinates
labels = ['A', 'B', 'C']
for i in range(len(labels)):
    ax.text(x[i], y[i], z[i], f"{labels[i]} ({x[i]:.1f}, {y[i]:.1f}, {z[i]:.1f})", 
            size=12, color='black')

# Label the axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Save the plot as .png and .jpg
plt.savefig('3d_plot.png')
#plt.savefig('3d_plot.jpg')

# Show the plot
plt.show()


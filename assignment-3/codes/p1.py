import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Function to calculate intersection points of the two circles
def intersection_points():
    center1 = np.array([0, 0])
    center2 = np.array([1, 0])
    r = 1  # Radius of both circles

    d = np.linalg.norm(center1 - center2)

    if d > r + r:  # No intersection
        return []
    if d < abs(r - r):  # One circle inside the other
        return []

    a = (r**2 - r**2 + d**2) / (2 * d)
    h = np.sqrt(r**2 - a**2)
    p2 = center1 + a * (center2 - center1) / d
    intersection1 = p2 + np.array([h * (center2[1] - center1[1]) / d, -h * (center2[0] - center1[0]) / d])
    intersection2 = p2 - np.array([h * (center2[1] - center1[1]) / d, -h * (center2[0] - center1[0]) / d])

    return intersection1, intersection2

# Function to read the area from the output.txt file
def read_area_from_file(filename):
    try:
        with open(filename, 'r') as file:
            area = float(file.readline().strip())
            return area
    except Exception as e:
        print(f"Error reading area from file: {e}")
        return None

# Circle equations
theta = np.linspace(0, 2 * np.pi, 100)
circle1_x = np.cos(theta)
circle1_y = np.sin(theta)

circle2_x = 1 + np.cos(theta)
circle2_y = np.sin(theta)

# Get intersection points
intersections = intersection_points()

# Read area from output.txt
area = read_area_from_file("output.txt")

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(circle1_x, circle1_y, label='Circle 1: $(x^2 + y^2 = 1)$', color='blue')
plt.plot(circle2_x, circle2_y, label='Circle 2: $((x-1)^2 + y^2 = 1)$', color='red')

# Plot centers
plt.scatter([0, 1], [0, 0], color='black', label='Centers', zorder=5)  # Centers
plt.text(0, 0, 'Center (0,0)', fontsize=12, ha='right')
plt.text(1, 0, 'Center (1,0)', fontsize=12, ha='left')

# Plot intersections
if intersections:
    for point in intersections:
        plt.scatter(point[0], point[1], color='green', zorder=5)
        plt.text(point[0], point[1], f'({point[0]:.2f}, {point[1]:.2f})', fontsize=10, ha='right')

# Shading the lens-shaped area
x_fill = np.linspace(0, 1, 100)

# Upper halves of both circles
y_fill1_upper = np.sqrt(1 - x_fill**2)  # Upper half of the first circle
y_fill2_upper = np.sqrt(1 - (x_fill - 1)**2)  # Upper half of the second circle
y_fill1_lower = -np.sqrt(1 - x_fill**2)  # Lower half of the first circle
y_fill2_lower = -np.sqrt(1 - (x_fill - 1)**2)  # Lower half of the second circle

# Fill between the two curves for both upper and lower halves
plt.fill_between(x_fill, np.minimum(y_fill1_upper, y_fill2_upper), color='lightgreen', alpha=0.5)
plt.fill_between(x_fill, np.maximum(y_fill1_lower, y_fill2_lower), color='lightgreen', alpha=0.5)

# Labels and legend
plt.xlim(-1.5, 2.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')

# Custom legend handle for the shaded area
shaded_area_handle = Line2D([0], [0], color='lightgreen', lw=4, label='Area bounded by circles = {:.5f}'.format(area) if area is not None else 'Shaded Area (Lens Shape)')

# Add custom legend handles
plt.legend(handles=[
    Line2D([0], [0], color='blue', lw=4, label='Circle 1: $(x^2 + y^2 = 1)$'),
    Line2D([0], [0], color='red', lw=4, label='Circle 2: $((x-1)^2 + y^2 = 1)$'),
    shaded_area_handle
])

plt.title("Area Bounded by Two Circles")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Save the plot as a PNG file
plt.savefig('figure1.png', bbox_inches='tight')

# Show plot
plt.show()


import matplotlib.pyplot as plt

x1, y1 = 2, 5
x2, y2 = 4, 8   

# Calculate differences in x and y
dx = x2 - x1
dy = y2 - y1

# Determine the number of steps required for the line
steps = int(max(abs(dx), abs(dy)))

# Calculate the increment in x and y for each step
x_increment = dx / steps
y_increment = dy / steps

# Initialize starting points
x, y = x1, y1

line_points = []

for _ in range(steps + 1):  
    line_points.append((round(x), round(y)))
    x += x_increment
    y += y_increment

x_coords, y_coords = zip(*line_points)

# Plot the line
plt.plot(x_coords, y_coords, marker="*", color="blue")
plt.title(f"DDA Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()

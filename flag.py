import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def plot_burundi_flag():
    fig, ax = plt.subplots()

    # Draw the background
    ax.add_patch(patches.Rectangle((0, 0), 3, 2, color='white'))

    # Draw the red diagonal cross
    ax.add_patch(patches.Polygon([[0, 0], [1.5, 1], [3, 0], [3, 0.2], [1.5, 1.2], [0, 0.2]], color='red'))
    ax.add_patch(patches.Polygon([[0, 2], [1.5, 1], [3, 2], [3, 1.8], [1.5, 0.8], [0, 1.8]], color='red'))

    # Draw the green triangles
    ax.add_patch(patches.Polygon([[0, 0], [1.5, 1], [0, 2]], color='#bebf'))
    ax.add_patch(patches.Polygon([[3, 0], [1.5, 1], [3, 2]], color='yellow'))

    # Draw the white central circle
    circle = patches.Circle((1.5, 1), 0.4, color='white')
    ax.add_patch(circle)

    # Draw the three red stars
    for angle in [90, 210, 330]:
        x = 1.5 + 0.25 * np.cos(np.radians(angle))
        y = 1 + 0.25 * np.sin(np.radians(angle))
        star = patches.RegularPolygon((x, y), numVertices=5, radius=0.1, orientation=np.radians(-90), color='red', edgecolor='green')
        ax.add_patch(star)

    # Set the aspect of the plot to be equal
    ax.set_aspect('equal')

    # Remove the axes
    ax.axis('off')

    plt.show()

if __name__ == "__main__":
    plot_burundi_flag()
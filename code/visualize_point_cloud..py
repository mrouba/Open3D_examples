import numpy as np
import open3d as o3d

# Load a 3D point cloud from a file
#pcd = o3d.io.read_point_cloud("C:/Users/PC/Desktop/saidikamel/XYZ/222.pts")
pcd = o3d.io.read_point_cloud("C:/Users/PC/Desktop/saidikamel/ICP/cloud_bin_2.pcd")



# Extract point coordinates as a NumPy array
points = np.asarray(pcd.points)

# Define a center
centre = [0, 0, 0]

# Calculate distances of each point from the center
distances = np.linalg.norm(points - centre, axis=1)

# Normalize distances 
normalized_distances = (distances - np.min(distances)) / (np.max(distances) - np.min(distances))

# Create an array for colors based on normalized distances
colors = np.zeros((len(points), 3))
colors[:, 1] = normalized_distances  # Set green channel based on normalized distances

# Set colors to the point cloud
pcd.colors = o3d.utility.Vector3dVector(colors)

# Visualize
o3d.visualization.draw_geometries([pcd])


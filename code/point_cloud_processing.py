import numpy as np
import open3d as o3d


# Create a 3D array representing point cloud coordinates
array = [[100, 256, 145], [1562, 1425, 214], [12, 126, 432], [5698, 1254, 32065]]

# Create an Open3D PointCloud object
pcd = o3d.geometry.PointCloud()

# Set the points of the PointCloud object using the 3D array
pcd.points = o3d.utility.Vector3dVector(array)



# Save the PointCloud object to a PLY file 
o3d.io.write_point_cloud('data3d\\testing_points.ply', pcd)

# Rading PointCloud from the file
pcd = o3d.io.read_point_cloud('data3d\\testing_points.ply')

# Draw the PointCloud using the Open3D visualization window
o3d.visualization.draw_geometries([pcd])

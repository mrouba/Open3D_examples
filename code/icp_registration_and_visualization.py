

'''The general idea of the provided code is to perform Iterative Closest Point (ICP)
    registration between two 3D point clouds. ICP is a common technique used in 
     computer vision and robotics to align two sets of points.
 
 '''


import numpy as np
import open3d as o3d

# Load two point clouds 
pcd_1 = o3d.io.read_point_cloud("path/to/ICP/cloud_bin_2.pcd")
pcd_2 = o3d.io.read_point_cloud("path/to/ICP/cloud_bin_1.pcd")

# Use CTRL + Left click to pick point
#Use Escape Key when you done picking points 
# Visualize and pick points from the first point cloud

vis1 = o3d.visualization.VisualizerWithEditing()
vis1.create_window()
vis1.add_geometry(pcd_1)
vis1.run()
picked_points_1 = vis1.get_picked_points()
points_1 = np.asarray(pcd_1.points)[picked_points_1]

# Visualize and pick points from the second point cloud
vis2 = o3d.visualization.VisualizerWithEditing()
vis2.create_window()
vis2.add_geometry(pcd_2)
vis2.run()
picked_points_2 = vis2.get_picked_points()
points_2 = np.asarray(pcd_2.points)[picked_points_2]

# Estimate normals for both point clouds
pcd_1.estimate_normals()
pcd_2.estimate_normals()

# Perform ICP registration to align the picked points of the two point clouds
current_transformation = np.identity(4)
result_icp = o3d.registration.registration_icp(
    o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points_1)),
    o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points_2)),
    0.02, current_transformation,
)

# Extract the transformation matrix from the registration result
transformation_matrix = result_icp.transformation

# Transform the first point cloud using the obtained transformation matrix
pcd_1_trans = pcd_1.transform(transformation_matrix)

# Combine the transformed point cloud with the second point cloud
consu_pcd_1 = pcd_1_trans + pcd_2

# Set colors for visualization
pcd_1.paint_uniform_color([0, 0, 1])
consu_pcd_1.paint_uniform_color([1, 0, 0])

# Visualize the combined point clouds
o3d.visualization.draw_geometries([consu_pcd_1, pcd_1])

import numpy as np
import open3d as o3d

pcd = o3d.io.read_point_cloud("path/to/ICP/cloud_bin_2.pcd")

points = np.asarray(pcd.points)
centre = [0, 0, 0]

distances = np.linalg.norm(points - centre, axis=1)
indices = np.where(distances > 50)[0]
filtered_distances = distances[indices]

normalized_filtered_distances = (filtered_distances - np.min(filtered_distances)) / (np.max(filtered_distances) - np.min(filtered_distances))


colors = np.zeros((len(points), 3))
colors[indices, 0] = normalized_filtered_distances  

pcd.colors = o3d.utility.Vector3dVector(colors)

o3d.visualization.draw_geometries([pcd])
#print(indices)

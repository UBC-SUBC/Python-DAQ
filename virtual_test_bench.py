import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import matplotlib
from imu import IMU_module
import time

def update_line(hl, new_data):
	xdata, ydata, zdata = hl._verts3d
	hl.set_xdata(list(np.append(xdata, new_data[0])))
	hl.set_ydata(list(np.append(ydata, new_data[1])))
	hl.set_3d_properties(list(np.append(zdata, new_data[2])))
	plt.draw()
 
 
def plot_yaw_ptich_row(euler, ax):
    euler = np.radians(euler)
    yaw = euler[0]
    pitch = euler[1]
    roll = euler[2]
    
    # Plot unit circle
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 5 * np.outer(np.cos(u), np.sin(v))
    y = 5 * np.outer(np.sin(u), np.sin(v))
    z = 5 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='lightgray', alpha=0.5)
    
    x = np.sin(yaw) * np.sin(pitch) * np.sin(roll) + np.cos(yaw) * np.cos(roll)
    y = np.sin(yaw) * np.sin(pitch) * np.cos(roll) - np.cos(yaw) * np.sin(roll)
    z = np.sin(yaw) * np.cos(pitch) * np.sin(roll) + np.cos(yaw) * np.sin(pitch) * np.cos(roll)

    
    # Plot the data
    ax.plot3D(x, y, z, 'b.')

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set plot title
    ax.set_title('Yaw, Pitch, and Roll')
    
    plt.pause(0.00001)

    # # Apply rotation to the unit circle
    # rotated_x, rotated_y, rotated_z = np.dot(rotation_matrix, [x.flatten(), y.flatten(), z.flatten()])

    # ax.plot_surface(rotated_x, rotated_y, rotated_z, color='blue', alpha=0.8)

    # # Reshape the rotated coordinates
    # rotated_x = np.reshape(rotated_x, x.shape)
    # rotated_y = np.reshape(rotated_y, y.shape)
    # rotated_z = np.reshape(rotated_z, z.shape)
            
def update_point(data):
    # map_ax.plot3D(data[0], data[1], data[2], 'gray')
    print(f"Plotting point {data}")
    
    map_ax.plot(data[0], data[1], data[2], 'gray', markersize=10)
    plt.draw()
    plt.pause(1)


plt.ion()

fig = plt.figure()
# map_ax = Axes3D(fig)
map_ax = fig.add_subplot(111, projection='3d')
map_ax.autoscale(enable=True, axis='both', tight=True)

limit = 20
# # # Setting the axes properties
map_ax.set_xlim3d([-limit, limit])
map_ax.set_ylim3d([-limit, limit])
map_ax.set_zlim3d([-limit, limit])

hl, = map_ax.plot3D([0], [0], [0])

imu = IMU_module()


while True:
    # time.sleep(1)
    imu_dict = imu.outputDict()
    # print(imu_dict)
    print()
    print(imu_dict["euler"])
    if imu_dict["euler"] != (0, 0, 0) or imu_dict["euler"] != None:
        print("start plotting")
        euler_tuple = imu_dict["euler"]
        euler_tuple = 5/np.cos(np.radians(euler_tuple))
        # update_point(euler_tuple)
        plot_yaw_ptich_row(imu_dict["euler"], map_ax)
        # plt.show(block=False)
        # plt.pause(1)


# plt.show(block=True)
# update_line(hl, (2,2, 1))
# plt.show(block=False)
# plt.pause(1)

# update_line(hl, (5,5, 5))
# plt.show(block=False)
# plt.pause(2)

# update_line(hl, (8,1, 4))
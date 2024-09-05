#!/usr/bin/env python

import rospy
from nav_msgs.msg import OccupancyGrid
import numpy as np

def occupancy_grid_callback(msg):
    # Get grid metadata
    width = msg.info.width
    height = msg.info.height

    # Convert the 1D data to a 2D numpy array
    occupancy_grid_2d = np.array(msg.data).reshape((height, width))

    # Print the 2D array (for demonstration purposes)
    rospy.loginfo("Occupancy Grid 2D Array:")
    rospy.loginfo(occupancy_grid_2d)

def listener():
    # Initialize the ROS node
    rospy.init_node('occupancy_grid_listener', anonymous=True)

    # Subscribe to the occupancy grid topic
    rospy.Subscriber('/map', OccupancyGrid, occupancy_grid_callback)

    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

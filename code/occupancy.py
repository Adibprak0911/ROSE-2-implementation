#!/usr/bin/env python

import rclpy
from nav_msgs.msg import OccupancyGrid
import numpy as np
from PIL import Image
import time
from rclpy.node import Node
import os

class MapSubscriber(Node):
    
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.occupancy_grid_callback,
            10)
        self.subscription

    def occupancy_grid_callback(self, msg):
        self.get_logger().info("got map")
        # Get grid metadata
        width = msg.info.width
        height = msg.info.height
        save_dir = os.path.join('code', 'data','INPUT','new')
        os.makedirs(save_dir, exist_ok=True)
        # Convert the 1D data to a 2D numpy array
        occupancy_grid_2d = np.array(msg.data).reshape((height, width)).astype(np.float64)
        image = Image.fromarray(occupancy_grid_2d)
        image = image.convert('RGB')
        image_path = os.path.join(save_dir, str(time.time())+".jpg")
        image.save(image_path)


def main(args=None):
    rclpy.init(args=args)
    map_subscriber = MapSubscriber()
    rclpy.spin(map_subscriber)
    map_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
import numpy as np

class ScanData:
    def __init__(self, scan_data, range_min, range_max):
        self.range_min = range_min
        self.range_max = range_max

        # points: [[x, y], ...]
        points = [np.array([np.cos(data[0]) * data[1], np.sin(data[0]) * data[1]]) for data in scan_data]

        nodes = [np.array([points[i + 1][0] - points[i][0], points[i + 1][1] - points[i][1]]) for i in range(len(points) - 1)]
        nodes_length = [ np.linalg.norm(node) for node in nodes ]
        nodes_direction = [ node / nodes_length[i] for i, node in enumerate(nodes) ]

        # unit_nodes = [[x, y, length]]
        unit_nodes = []
        print("points")
        print(points)
        print("nodes")
        print(nodes)
        print("nodes_length ")
        print(nodes_length)
        print("nodes_direction")
        print(nodes_direction)


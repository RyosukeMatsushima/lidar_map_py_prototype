import numpy as np

# This class detects feature nodes in non-nan nodes
class FeatureDetector:
    def __init__(self, feature_length, poitns, _nodes_length, nodes_direction):

        self.feature_length = feature_length
        self.points = points
        self.nodes_length = nodes_length
        self.nodes_direction = nodes_direction

        # calculate order to check
        distance_from_first_node = []
        sum_length = 0.0
        for length in self.nodes_length:
            distance_from_first_node += [sum_length]
            sum_length += length

        switch_order_material= [ (distance, True) for distance in distance_from_first_node ]
        switch_order_material += [ (distance + self.feature_length, False) for distance in distance_from_first_node ]

        dtype = [('distance', float), ('is_front', bool)]
        som = np.array(switch_order_material, dtype=dtype)
        print(np.sort(som, order='distance'))

        # TODO: refactor to get end_point fast
        self.start_point = 0
        self.end_point = 0

        sum_length = 0.0
        for i, length in enumerate(self.nodes_length):
            sum_length += length
            self.end_point = i

            if sum_length < self.feature_length:
                break

    def search(self):
        return

    def get_min_l(self):
        a_1 = self.points[self.start_point]
        b_1 = self.points[self.end_point]
        e_a = self.nodes_direction[self.start_point]
        e_b = self.nodes_direction[self.end_point]

        # TODO: recheck pointer count
        sum_nodes_length = np.sum(self.nodes_length[self.start_point: self.end_point])

        eb_m_ea = e_b - e_a
        # TODO: recheck pointer count
        l_b = self.feature_length - np.sum(self.nodes_length[self.start_point: self.end_point])

        return - np.dot((b_1 - a_1 + l_b * e_b), eb_m_ea) / np.dot(eb_m_ea, eb_m_ea)



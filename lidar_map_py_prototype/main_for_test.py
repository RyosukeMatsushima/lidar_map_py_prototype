from scan_data import ScanData
from feature_detector import FeatureDetector

import csv

if __name__ == '__main__':

    with open('scan_data.csv') as f:
        reader = csv.reader(f)
        scan_data = [[float(row[0]), float(row[1])] for row in reader]

    scanData = ScanData(scan_data, 0.2, 10)

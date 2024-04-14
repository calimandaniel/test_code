import time
import unittest

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('unit_test')
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    t = 10  # Set the time interval (in seconds) here
    while True:
        run_tests()
        time.sleep(t)
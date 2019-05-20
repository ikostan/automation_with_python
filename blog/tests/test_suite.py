import unittest
loader = unittest.TestLoader()
start_dir = 'C:/Users/superadmin/Desktop/Python/automation_with_python/blog/tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)


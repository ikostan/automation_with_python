import unittest
loader = unittest.TestLoader()
start_dir = 'C:/Users/superadmin/Desktop/Python/automation_with_python/blog_console_app/tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

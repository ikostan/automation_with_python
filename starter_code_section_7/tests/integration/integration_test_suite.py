import unittest

# TODO: refactor the file in order to make it as a test and not just python file

loader = unittest.TestLoader()

integration = 'C:/Users/superadmin/Desktop/Python/automation_with_python/starter_code_section_7/tests/integration/models'

suite_integration = loader.discover(integration)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_integration)


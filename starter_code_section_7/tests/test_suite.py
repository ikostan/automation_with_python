import runpy
import time


unit = "C:/Users/superadmin/Desktop/Python/automation_with_python/starter_code_section_7/tests/unit/unit_test_suite.py"
integration = "C:/Users/superadmin/Desktop/Python/automation_with_python/starter_code_section_7/tests/integration/integration_test_suite.py"
system = "C:/Users/superadmin/Desktop/Python/automation_with_python/starter_code_section_7/tests/system/system_test_suite.py"

files = {'UNIT': unit, 'INTEGRATION': integration, 'SYSTEM': system}

# execute the file
for key in files.keys():
    print('\nRunning {0} test suite:'.format(key))
    run = runpy.run_path(files[key])
    run.clear()
    time.sleep(1)


#!/bin/bash
def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)


# execute the file
print('\nRunning UNIT test suite:')
unit = "C:/Users/superadmin/Desktop/Python/automation_with_python/starter_code_section_7/tests/unit/unit_test_suite.py"
execfile(unit)

print('\nRunning INTEGRATION test suite:')
integration = "C:/Users/superadmin/Desktop/Python/automation_with_python/starter_code_section_7/tests/integration/integration_test_suite.py"
execfile(integration)


print('\nRunning SYSTEM test suite:')
system = "C:/Users/superadmin/Desktop/Python/automation_with_python/starter_code_section_7/tests/system/system_test_suite.py"
execfile(system)


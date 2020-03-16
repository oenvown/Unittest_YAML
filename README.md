**What the project does**

This project demonstrates how yaml input can be unittested before using it in the code.

**Why the project is useful**

When code is accepting yaml data as an input it might be useful to unittest input before running the script. This small project can be used as an example or reference to accomplish this task

**How users can get started with the project**

Following modules are used in this demonstration and has to be installed in to the virtual environment:

* PyYaml
* netaddr

Description of the project files:

* metadata.yml - it's our input data in YAML format
* yaml_test.py - our unittest script. It can be ran standalone or can be imported and used by do_something.py script.
* do_something.py - it's demonstration script showing how yaml input can be unittested before using it in the script itself.

**Where you can get help**

Project utilizes standard Python unittest module.
It is documented here:
https://docs.python.org/3/library/unittest.html
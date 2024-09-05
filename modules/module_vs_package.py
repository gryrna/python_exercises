''' 
A module is a single file with a .py suffix.
Module is loaded using import.
To use variable/function use,
'from module_name import variable_name,function_name'
'''

'''
A package has more than one module.
It is a directory.
To use a package, put its path in sys.path

To use a module from a package, use
'from package_name import module_name'
To use functions of module, use
'module_name.function_name'

Alternatively, you can use,
'import package_name'
but this will only work if the package has
a file named __init__.py
In that file, you can import one or more modules within
the package.
'''

'''
To distribute your package, you have to create a packet
using PyPi
A PyPi is a wrapper around your package that contains
information about author, compatible versions, licensing
automated tests, dependencies, and installation instructions

Both the distribution packet and your package are directories
having same name.
Example:
mypackage(distribution_name)/mypackage(your_package_name)/modules

To create a distribution packet we need to create a setup.py file
Or, you Poetry to create packages with ease.

To distribute Packet using PyPi, register for a username, and password
To upload using Poetry on UNIX
$poetry new packet_name
$cd package_name
cp -R ~/package_name/* package_name
poetry build
poetry publish

Also edit the pyproject.toml config file
that describes version, license, and dependencies.
'''
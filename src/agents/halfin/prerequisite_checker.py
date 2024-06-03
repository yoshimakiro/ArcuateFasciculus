import subprocess
import modulefinder
import pkg_resources
import os

def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call(['pip', 'install', package])
            print(f'Successfully installed {package}')
        except subprocess.CalledProcessError:
            print(f'Failed to install {package}')

def find_required_packages(directory):
    finder = modulefinder.ModuleFinder()
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            finder.run_script(os.path.join(directory, filename))
    return finder.modules.keys()

def get_installed_packages():z
    return set([d.key for d in pkg_resources.working_set])

def check_for_prerequisites(directory):
    required_packages = find_required_packages(directory)
    installed_packages = get_installed_packages()
    packages_to_install = [package for package in required_packages if package not in installed_packages]
    
    # Add 'autogen' to the list of packages to install
    if 'autogen' not in installed_packages:
        packages_to_install.append('autogen')
    
    install_packages(packages_to_install)
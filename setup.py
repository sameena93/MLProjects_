from setuptools import find_packages, setup
from typing import List


hyphen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    """this will return a list of requirements"""
    requirements = []
    with open(file_path) as file:
        content = file.read()
        requirements = [req.replace('\n',"") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements
setup(
    name='mymlprojects',
    version='1.0',
    author='Sameena',
    author_email='sameenamujawar101@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)
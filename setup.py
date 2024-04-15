from setuptools import setup , find_packages
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    return requirements
setup(
    name='END-TO-END-ML-PROJECT',
    version='1.0.0',
    author='Sarvesh Karanjkar',
    author_email='sarveshkaranjkar516@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')
)
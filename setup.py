from setuptools import setup, find_packages
from typing import List


hyphen_e_dot = "-e ."
def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath, 'rb') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements

setup(
    name='MLproject2',
    version='0.0.1',
    author='Sierra',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
from setuptools import setup,find_packages
from typing import List
from pathlib import Path

HYPEN_E_DOT = "-e ."

def get_requirements(filepath:Path)->List[str]:
    """This function is used to fetch all packages from the requirements.txt"""

    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()

        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    author="Arjun Singh Shekhawat",
    author_email="shekhawatsingharjun12345@gmail.com",
    version="0.0.1",
    description="Cat Dog Classifier Project",
    name="Cat Dog Classification",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
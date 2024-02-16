from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT_E = "-e ."

def get_requirements(file_path) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements


setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Deepjyoti Bhattacharjee",
    author_email="deepjyotibhattacharjee217@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages=find_packages()
)


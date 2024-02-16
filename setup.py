from setuptools import find_packages,setup

def get_requirements():...

setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Deepjyoti Bhattacharjee",
    author_email="deepjyotibhattacharjee217@gmail.com",
    # install_requires = get_requirements("requirements.txt"),
    packages=find_packages()
)


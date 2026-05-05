from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Multi-Agent-Platform",
    version="0.1",
    author="Hossain",
    packages=find_packages(),
    install_requires = requirements,
)
from setuptools import setup, find_packages

setup(
    name='daily-check-in',  # Replace with your project's name
    version='0.1',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),  # Read dependencies from requirements.txt
)

from setuptools import find_packages, setup

setup(
    name='engine',
    version='1.0',
    author='...',
    description='...',
    long_description='...',
    url='https://github.com/arnab-api/engine',
    python_requires='>=3.7',
    packages=find_packages(include=['.', '.*']),
    install_requires=[
        'pyyaml',
    ]
)
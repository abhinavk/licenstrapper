from setuptools import setup, find_packages

from licenstrapper import __version__

setup(
    name='licenstrapper',
    version=__version__,
    url='https://github.com/abhinavk/licenstrapper',
    description='Generates license files for your projects',
    author='Abhinav Kumar',
    author_email='abhinav@outlook.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'licenstrapper = licenstrapper.__main__:main'
        ]
    }
)

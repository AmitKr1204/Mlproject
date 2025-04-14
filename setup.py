#setup.py is like buiding our application as a package itself
#is a special file used in Python projects to define how your package should be built, installed, and distributed. It's basically the "build script" for packaging your Python code — especially when you're publishing a library or tool to PyPI (Python Package Index).
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Amit',
    author_email='amitkumar12015@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

from setuptools import find_packages,setup
from typing import List

HYPEN_E_Dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requiremnts=[]
    with open (file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace("\n","") for req in requiremnts]
        if HYPEN_E_Dot in requiremnts:
            requiremnts.remove(HYPEN_E_Dot)
            
    return requiremnts
    
setup(
    name='MLPROJECT',
    version='0.0.01',
    author='Dhanush',
    author_email="nadigdhanush@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

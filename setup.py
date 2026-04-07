from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''this fun retuns the list of requirements
    '''
    reaquirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read line from fie
            lines=file.readlines()
            # process each line
            for line in lines:
                reaquirement=line.strip()
                # ignore empty line and -e .
                if reaquirement and reaquirement !='-e .':
                    reaquirement_lst.append(reaquirement)
        
    except FileNotFoundError:
        print("requirements.txt file not found")
    return reaquirement_lst

setup(
name='NetworkSecurity',
version='0.0.1',
author='Shubham Langade',
author_email='slangade68@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
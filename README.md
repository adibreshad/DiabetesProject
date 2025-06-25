# DiabetesProject

This project aims to predict diabetes using a machine learning pipeline.

## Project Structure

The directory structure is organized as follows:

```
├── .gitignore
├── requirements.txt
├── setup.py
└── src
    ├── __init__.py
    ├── exception.py
    ├── logger.py
    ├── utils.py
    ├── components
    │   ├── __init__.py
    │   ├── data_ingestion.py
    │   ├── data_transformation.py
    │   └── model_trainer.py
    └── pipeline
        ├── __init__.py
        ├── stage_01_data_ingestion.py
        └── stage_02_data_validation.py
```

## Setup and Installation

1.  **Create and activate the Conda environment:**
    ```bash
    conda create -p venv python=3.8 -y
    conda activate ./venv
    ```

2.  **Install the project and its dependencies:**
    ```bash
    pip install -e .
    ```
  
 

3. **The setup.py file:**

'''from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirements(file_path: str)-> List[str]:
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='diabetics_project',
    version='0.1.0',
    author='adibreshad',
    author_email="adibahmadreshad@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

    '''


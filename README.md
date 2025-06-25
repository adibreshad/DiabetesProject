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

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

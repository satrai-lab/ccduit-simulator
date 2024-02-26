
# Installation Guide for Scalability_Simulation.py

## Introduction
This document provides detailed instructions for installing and setting up the environment required to run the `Scalability_Simulation.py` script for analyzing the scalability of federated data spaces using CCDUIT.

## Prerequisites
- Python 3.x
- pip (Python package installer)

## Installation Steps

1. **Clone the Repository**: If you have git installed, clone the repository using:
   ```bash
   git clone [repository-url]
   ```
   Alternatively, download the ZIP file of the code and extract it to your local machine.

2. **Set Up a Python Virtual Environment** (recommended):
   Navigate to the project directory and run:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   While in the project directory and the virtual environment activated, install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
4. **Verification**:
   In order to verify quickly that everything runs ok and see some results, you can comment out lines 253,255,257 of the "Scallability_simulation.py" file (the simulate scenarios functions), and uncomment line 249. Then running the file will print operational outputs that were put to see the progress of the simulation and  should alsoproduce some quick results (a figure as the end result). 


## Troubleshooting
- **Issue**: Missing dependencies or modules.
  **Solution**: Ensure you have activated the virtual environment and run `pip install -r requirements.txt`.
- **Issue**: Python or pip is not recognized.
  **Solution**: Verify that Python and pip are correctly installed and added to your system's PATH.


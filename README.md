
# Scalability Simulation for CCDUIT Federated Networks

## Overview

This [repository](https://github.com/satrai-lab/ccduit-simulator/) contains the `Scalability_Simulation.py` Python script, which is used to analyze and depict the scalability of CCDUIT across simulated federated data spaces. This simulation is part of the research presented in the paper "CCDUIT: A Software Overlay for Cross-Federation Collaboration between Data Spaces" and illustrates how different federation configurations can impact operational efficiency and code volume. The Folder "Experiment Scenarios" is provided as reference for the targeted case study within a controlled environment across three federations, focusing on the exchange of transportation data, as showcased in section VI of the paper. This is also important as the steps present in this folder are used to initialise variables regarding lines of code for different kinds of operations inside the simulator. 

## Simulation Objective

The script simulates varying scenarios within federated networks focusing on data exchange and collaboration strategies, highlighting the benefits of CCDUIT in reducing the complexity and effort involved in managing federated data spaces.

## Installation Instructions

Ensure Python 3.x and necessary libraries are installed. Clone this repository - Download this folder, and navigate to the directory containing `Scalability_Simulation.py`. Install required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the Simulation

Execute the script with:

```bash
python3 Scalability_Simulation.py
```

The simulation runs multiple scenarios varying by data type diversity (DT%), context exchange percentage (CE%), and pre-configured nodes percentage (PC%). Results are visualized through multi-panel plots.

## Expected Results

You will receive graphical outputs representing the scalability analysis, showing the total effort (in lines of code) required under different network configurations. This demonstrates the operational advantages of adopting CCDUIT in federated environments. The program requires no user input, you should be able to just run it and get the results when it finishes. As it takes a long time to replicate the figure present in the paper, please refer to "Customizing the simulation" in order to run a simplified example if you wish to do so.

## Customizing the Simulation

You can adjust parameters such as the number of nodes and percentages for DT%, CE%, and PC% to explore different scenarios. Refer to the comments within the script for guidance on making these changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact Information

For further assistance or questions, please contact us at nikolaos.papadakis@telecom-sudparis.eu 

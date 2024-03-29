# LLMExperiment_Subjects [Under development - not working]
repository to host EconLLM lab python package for implementing the framework in paper "..." published in "..." 

## Overview

The LLMExperiment_Subjects package is designed to facilitate the creation and management of economic experiments using Language Model (LLM) subjects. This package enables researchers to build profiles for target populations, instantiate experiment subjects with preferences or value structures matching those profiles, and set up and run economic experiments, such as the ultimatum game. The package is structured to provide a clear, modular approach to experiment creation, ensuring ease of use and flexibility for conducting sophisticated LLM-based research.

## Pacakge structure

The package consists of a main module directory, a testing directory, and essential project files. Here is a brief overview of the package's architecture:


LLMExperiment_Subjects/
│
├── LLMExperiment_Subjects/
│   ├── __init__.py
│   ├── BuildProfile.py
│   ├── BuildExperimentSubject.py
│   └── BuildExperiment.py
│
├── tests/
│   ├── __init__.py
│   └── hazda_test.py
|
├── utils/
│   ├── __init__.py
│   ├── search.py
│   └── process_and_index.py
│
├── .gitignore
├── LICENSE
├── .env
├── README.md
└── setup.py


- BuildProfile.py: Contains the ProfileBuilder class, which is responsible for generating a comprehensive profile for a target population. This module implements a custom version of a RAG architecture to build a knowledge vector store, essential for creating detailed and accurate population profiles.

- BuildExperimentSubject.py: Features the ExperimentSubjectBuilder class that utilizes the profile generated by ProfileBuilder to instantiate an LLM. This LLM is carefully prompted to mimic the preferences or value structure of the target population, creating a realistic subject for economic experiments.

- BuildExperiment.py: Houses two classes, ExperimentSetup and RunExperiment. ExperimentSetup is tasked with configuring the settings and parameters for economic experiments like the ultimatum game. RunExperiment takes these configurations and executes the experiment, handling the logistics and flow of the experimental process.

## Testing

The tests/ directory contains unit tests for the package, ensuring the reliability and accuracy of its components. Current tests include:

- hazda_test.py: A test case using the Hazda tribe as the target population and several economic games.

## Design Logic

The LLMExperiment_Subjects package is built with modularity and extendibility in mind. Each component focuses on a specific aspect of experiment creation, from profile generation to subject instantiation and experiment execution. This separation of concerns allows for greater flexibility in research design and facilitates easy updates and enhancements to each module without affecting the others. Our approach ensures that researchers can tailor the experimental setup to their specific needs while maintaining a high level of detail and transparency of LLM behavior in the simulation of target populations.
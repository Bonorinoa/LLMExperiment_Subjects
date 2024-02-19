from setuptools import setup, find_packages

setup(
    name='LLMExperiment_Subjects',
    version='0.1.0',
    author='Augusto Gonzalez-Bonorino',
    author_email='augusto.gonzalez-bonorino@cgu.com',
    description='A framework for simulating economic agents for target populations and economic games to evaluate the LLM subjects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/Bonorinoa/LLMExperiment_Subjects',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GNU GENERAL PUBLIC LICENSE Version 3.0',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add your package dependencies here
        # e.g., 'requests>=2.19.1',
    ],
)

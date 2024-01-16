from setuptools import find_packages, setup

# with open('README.md' , 'r' , encoding='utf-8' ) as f:
#     long_description = f.read()

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='This project aims to build a movie recommendation system using data on genres,, cast, crew, overview, release_year , runtime , keywords , vote_average , Director of several thousand films. It combines features such as cosine similarity and Euclidean distance to provide movie recommendations.',
    author='Abdelrahman mohamed',
    license='MIT',
    # long_description= long_description,
    # packages=['src'],
    python_requires = '>=3.10.8',
    # install_requires = ['streamlit']
)

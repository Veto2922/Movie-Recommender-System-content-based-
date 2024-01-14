# Movies Recommendation System

This project aims to build a movie recommendation system using data on plot, cast, crew of several thousand films. It combines features such as cosine similarity and Euclidean distance to provide movie recommendations.

## About Dataset

What can we say about the success of a movie before it is released? Are there certain companies (Pixar?) that have found a consistent formula? Given that major films costing over $100 million to produce can still flop, this question is more important than ever to the industry. Film aficionados might have different interests. Can we predict which films will be highly rated, whether or not they are a commercial success?

This is a great place to start digging into those questions, with data on the plot, cast, crew, budget, and revenues of several thousand films.

### Data source

The dataset used in this project is obtained from [TMDB Movie Metadata on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data).

## Data Cleaning Summary

#### Objective
The purpose of this notebook is to clean and preprocess the movie dataset obtained from TMDB. The dataset includes information about movies, such as plot details, cast, crew, release date, genres, and more.

#### Steps Taken

1. **Data Loading:**
   - Loaded the movie and credits datasets from CSV files using pandas.

2. **Merging Datasets:**
   - Merged the two datasets using the 'movie_id' column.

3. **Handling Missing Values:**
   - Explored and addressed missing values in the dataset.
   - Dropped columns 'tagline' and 'homepage' due to a high percentage of missing values.

4. **Selecting Features:**
   - Selected relevant features for analysis and recommendation.
   - Renamed columns for clarity.

5. **Correcting Data Types:**
   - Adjusted data types of certain columns (e.g., 'movie_id' to object, 'release_date' to datetime).

6. **Checking for Duplicates:**
   - Identified and checked for duplicate records.

7. **Handling Outliers:**
   - Explored and visualized potential outliers in the dataset.
   - Decided not to remove outliers in the 'vote_count' column.
---
## Feature Engineering Summary

#### Objective
The Feature Engineering notebook focuses on transforming the selected movie dataset to create meaningful features for building a recommendation system. The goal is to enhance the dataset by handling dictionary columns, text processing, and creating new features.

#### Steps Taken


2. **Untangling Dictionary Columns:**
   - Converted dictionary columns ('genres', 'keywords', 'cast', 'crew') into lists.
   - Applied functions to extract relevant information from these columns.

3. **Text Processing:**
   - Processed text data by converting the 'overview' column from a string to a list of words.
   - Removed spaces from list columns for count vectorization.

4. **Combining Text Features:**
   - Created a new column 'tags' by combining relevant text features ('overview', 'genres', 'cast', 'keywords', 'Director').

5. **Extracting Movie Year:**
   - Extracted the release year from the 'release_date' column and created a new 'release_year' column.

6. **Selecting Final Features:**
   - Selected the final columns for analysis and recommendation.

7. **Converting Tags to String:**
   - Converted the 'tags' column from a list to a string.


## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third-party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     the creator's initials, and a short `-` delimited description, e.g.,
    │   │                     `1.0-jqp-initial-data-exploration`.
    │   ├── 1.0-data-exploration.ipynb  <- Initial data exploration notebook.
    │   └── ...            <- Additional notebooks for various stages of the project.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.,
    │                         generated with `pip freeze > requirements.txt`.
    │
    ├── setup.py           <- Makes the project pip installable (pip install -e .) so src can be imported.
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module.
    │   │
    │   ├── data           <- Scripts to download or generate data.
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling.
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions.
    │   │   ├── train_model.py
    │   │   └── predict_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results-oriented visualizations.
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io.

--------

<small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small>





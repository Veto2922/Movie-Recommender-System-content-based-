# Movie Recommendation System

## Content

1. [About the Project](#about-the-project)
   - [Website Overview](#website-overview)
   - [Features](#features)
   - [How to Use](#how-to-use)

2. [About the Dataset](#about-the-dataset)
   - [Data Cleaning Summary](#data-cleaning-summary)
   - [Feature Engineering Summary](#feature-engineering-summary)

3. [Data Preprocessing and Similarity Matrix](#data-preprocessing-and-similarity-matrix)

4. [Project Organization](#project-organization)

---

## About the Project

This project is dedicated to constructing an advanced movie recommendation system by leveraging popularity and content-based filtering. The model integrates diverse data features, such as genres, cast, crew, overview, release year, runtime, keywords, vote average, and director information, obtained from a comprehensive dataset of several thousand films. The recommendation system employs advanced techniques like cosine similarity and Euclidean distance to enhance the accuracy and personalization of movie suggestions.

### Website Overview

#### Overview

This Streamlit application serves as the frontend for the movie recommendation system, offering users an interactive experience to explore top movies and discover similar films based on their preferences.

Website Link: [Movie Recommender System](https://movie-recommender-sys2.streamlit.app/)

![Movie Recommender System](https://github.com/Veto2922/Movie-Recommender-System-content-based-/assets/114834171/24883710-1dc3-4c6c-96cd-f4ca59c2b481)

#### Features

1. **Top Movies Display:**
   - The home page showcases top movies with posters, release year, runtime, and vote average.
   - Users can click on a movie poster to view recommendations for similar films.

2. **Movie Recommendations:**
   - Clicking a movie poster opens a sidebar with recommendations similar to the selected film.
   - The sidebar displays posters and details for each recommended movie.

3. **Developer Information:**
   - The footer provides information about the developer, Abdelrahman Mohamed, with links to LinkedIn and GitHub.

#### How to Use

1. **Installation:**
   - Clone the repository to your local machine:
     ```bash
     git clone https://github.com/Veto2922/Movie-Recommender-System-content-based-.git
     ```

2. **Navigate to the App:**
   - Change directory to the app folder:
     ```bash
     cd Movie-Recommender-System-content-based-
     ```

3. **Install Dependencies:**
   - Install the required Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the App:**
   - Execute the following command in your terminal:
     ```bash
     streamlit run app.py
     ```
   - The app will open in your default web browser.

5. **Explore Recommendations:**
   - Click on movie posters to explore recommendations for similar movies.
   - View movie details and discover new films based on your preferences.

## About the Dataset

This project utilizes a dataset obtained from [TMDB Movie Metadata on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data). The dataset includes comprehensive information about movies, covering plot details, cast, crew, release date, genres, and more.

### Data Cleaning Summary

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

### Feature Engineering Summary

#### Objective
The Feature Engineering notebook focuses on transforming the selected movie dataset to create meaningful features for building a recommendation system. The goal is to enhance the dataset by handling dictionary columns, text processing, and creating new features.

#### Steps Taken

1. **Untangling Dictionary Columns:**
   - Converted dictionary columns ('genres', 'keywords', 'cast', 'crew') into lists.
   - Applied functions to extract relevant information from these columns.

2. **Text Processing:**
   - Processed text data by converting the 'overview' column from a string to a list of words.
   - Removed spaces from list columns for count vectorization.

3. **Combining Text Features:**
   - Created a new column 'tags' by combining relevant text features ('overview', 'genres', 'cast', 'keywords', 'Director').

4. **Extracting Movie Year:**
   - Extracted the release year from the 'release_date' column and created a new 'release_year' column.

5. **Selecting Final Features:**
   - Selected the final columns for analysis and recommendation.

6. **Converting Tags to String:**
   - Converted the 'tags' column from a list to a string.

## Data Preprocessing and Similarity Matrix

This section focuses on preparing and processing data to build a movie recommendation system. The process involves loading a preprocessed dataset, applying text preprocessing techniques, such as stemming, and using Count Vectorization on the tags column to create a word vector matrix. Numerical details about movies, including

release year, runtime, and vote average, were extracted and standardized using StandardScaler. Two similarity measures were employed: cosine similarity for the word vector matrix and Euclidean distance for numerical movie details.

To ensure a balanced recommendation, a final similarity matrix was created by combining these two similarity matrices, with higher weight assigned to the word matrix. This approach provides users with a more comprehensive and personalized movie suggestion experience.

For testing the recommendation system, a simple function named `recommend(movie)` was implemented. Users can input a movie title, and the system will output the top 10 similar movies. The similarity matrix was saved using the joblib library for reusability.

## Project Organization

```
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
```

<small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small>

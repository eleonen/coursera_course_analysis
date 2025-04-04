# Coursera Course Dataset Analysis

## Overview
This project provides an exploratory data analysis (EDA) of a Coursera course dataset, uncovering insights into course popularity, engagement, difficulty levels, certificate types, and ratings. The analysis explores trends in course enrollments, the influence of course difficulty on ratings, the distribution of certificate types, and other factors that might impact course success.

Using Python, this analysis is reproducible, with dependencies managed via Poetry. The included Jupyter notebook demonstrates the analytical steps and findings.

## Table of Contents
1. [Setup](#setup)
2. [Project Structure](#project-structure)
3. [Data Analysis](#data-analysis)
4. [Usage](#usage)
5. [Improvements and Future Work](#improvements-and-future-work)
6. [Contributors](#contributors)

## Setup

### Prerequisites
- Python 3.x
- Poetry for dependency management
- Jupyter Notebook (optional, for viewing the analysis)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TuringCollegeSubmissions/eleone-DS.v3.1.4.5
   cd eleone-DS.v3.1.4.5
   ```

2. Set up a virtual environment and install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. (Optional) If using Jupyter Notebook to view or modify the analysis:  
   ```bash
   poetry add notebook
   ```

## Project Structure
- `pyproject.toml`: Poetry configuration file listing dependencies.
- `poetry.lock`: Lock file with exact package versions.
- `coursera_data.csv`: Dataset containing information about Coursera courses.
- `coursera_data_analysis.ipynb`: Jupyter notebook with the analysis and insights derived from the dataset.
- `src/utilities.py`: Contains helper functions like `find_outliers` and `add_labels` for visualizations.

## Data Analysis

### Key Questions Answered:
1. **Dataset Overview:**
   - Total number of observations.
   - Checking for missing or duplicate values.
   - Outlier detection in numerical fields (e.g., rating).
   - Identification of categorical and numerical features.
2. **Course Popularity and Engagement:**
   - Distribution of enrollments, both visually and on a logarithmic scale.
   - Identifying the most and least popular courses.
3. **Course Ratings:**
   - Exploring rating distributions by course difficulty.
   - Identifying highest and lowest rated courses.
   - Analyzing correlation between course ratings and enrollment numbers.
4. **Certificate Types:**
   - Distribution of different certificate types and their popularity.
   - Analyzing certificate types across course difficulty levels.
5. **Difficulty Level Insights:**
   - Frequency of beginner, intermediate, mixed, and advanced level courses.
   - Analysis of course ratings by difficulty level.
6. **Organization Analysis:**
   - Total number of unique organizations.
   - Top 15 organizations by the number of courses offered.
   - Top 15 organizations by average course rating.

## Usage

### Running the Jupyter Notebook
To interact with the data analysis or run your own queries, use the Jupyter notebook:
1. Start Jupyter Notebook:
   ```bash
   jupyter notebook coursera_data_analysis.ipynb
   ```
2. Follow the cells to explore the analysis, or modify them to perform your own exploration.

## Improvements and Future Work
- **Numeric Encoding for Difficulty Levels:** Assign numeric values to difficulty levels to enable correlation analysis.
- **Student-Enrollment Correlation:** Analyze how difficulty levels influence the number of enrolled students.
- **Course Completion Data:** Analyze course completion rates if data expansion allows, helping assess course effectiveness and learner commitment.

## Contributors
- [Erikas Leonenka](https://github.com/eleonen)

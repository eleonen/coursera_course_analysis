"""
This module provides utility functions for data analysis and visualization tasks.
It includes tools to detect outliers in numerical features of a DataFrame and
to add value labels on bar plots.

Functions:
    - find_outliers: Identifies outliers in specified DataFrame columns using the IQR method.
    - add_labels: Adds value labels on bars in a bar plot for improved readability.

Dependencies:
    - pandas as pd
    - matplotlib.axes.Axes
"""

import pandas as pd
from matplotlib.axes import Axes
from typing import List
    
def find_outliers(df: pd.DataFrame, features: List[str]) -> pd.DataFrame:
    """
    Detects outliers in multiple features using the IQR method.

    Args:
        df: DataFrame containing the data.
        features: List of features to detect outliers in.

    Returns:
        DataFrame containing the outliers for each feature.
    """
    outliers_list = []
    for feature in features:
        if feature not in df.columns:
            print(f"Feature '{feature}' not found in DataFrame.")
            continue

        q1 = df[feature].quantile(0.25)
        q3 = df[feature].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        feature_outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
        if not feature_outliers.empty:
            print(f"Outliers in '{feature}':")
            print(feature_outliers[feature], end="\n\n")
            outliers_list.append(feature_outliers)
        else:
            print(f"No outliers in '{feature}'")

    if outliers_list:
        outliers = pd.concat(outliers_list)
        outliers = outliers[features]
    else:
        outliers = pd.DataFrame(columns=features)
        
    return outliers

def add_labels(ax: Axes, orientation: str ="v") -> None:
    """
    Adds value labels on top of bars in a bar plot.

    Parameters:
    ax (Axes): The axes object containing the plot.
    orientation (str): Orientation of bars, 'v' for vertical (default) or 'h' for horizontal.
    """
    if orientation == "v":
        for b in ax.patches:
            height = b.get_height()
            if height != 0:
                label = f"{int(height)}" if isinstance(height, int) or height.is_integer() else f"{b.get_height():.2f}"
                ax.text(
                    b.get_x() + b.get_width() / 2,
                    b.get_height(),
                    label, 
                    ha="center",
                    va="bottom"
                )
        ax.set_yticks([])
    elif orientation == "h":
        for b in ax.patches:
            width = b.get_width()
            if width != 0:
                label = f"{int(width)}" if isinstance(width, int) or width.is_integer() else f"{b.get_width():.2f}"
                ax.text(
                    b.get_width(),
                    b.get_y() + b.get_height() / 2,
                    label, 
                    ha="left",
                    va="center"
                )
        ax.set_xticks([])
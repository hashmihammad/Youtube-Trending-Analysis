# YouTube Trending Video Analysis

This project analyzes **YouTube Trending Videos** using **Python, Pandas, and Matplotlib**.
The dataset is taken from **Kaggle** and includes details like video views, likes, dislikes, comments, and categories.

## Features

* Clean and preprocess the Kaggle dataset.
* Merge video data with category metadata (`US_category_id.json`).
* Perform **Exploratory Data Analysis (EDA)**.
* Visualize insights such as:

  * Most popular video categories.
  * Top trending channels.
  * Best time/day to publish videos.
  * Relationship between views, likes, and comments.

## Project Structure

```
youtube-trending-analysis/
├── main.py                 # Main analysis script
├── US_category_id.json     # Category metadata (JSON)
├── USvideos.csv            # Sample dataset (Kaggle - US region)
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```


The script will generate multiple visualizations, including:

* **Top 10 video categories by average views**
* **Average views by publish hour**
* **Average views by day of the week**
* **Top 10 channels with most trending videos**
* **Views vs Like Ratio (scatter plot)**
* **Views vs Comment Ratio (scatter plot)**

## Dataset

The dataset is available on Kaggle:
[YouTube Trending Video Dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)

Note: Only a sample (`USvideos.csv` and `US_category_id.json`) is included in this repository.
For the full dataset, please download it directly from Kaggle.

## License

This project is licensed under the **MIT License**.

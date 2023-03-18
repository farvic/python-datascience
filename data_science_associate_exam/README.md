EMO Electric Motorcycles Survey Analysis

This project aims to analyze the ratings and feedback from customers who have used EMO's electric motorcycles in India. The goal is to gain insights into customer satisfaction and preferences, and to develop a model that can predict whether a review was written by an owner or not.

Dataset

The dataset used in this project contains the following columns:

* owned: Whether the reviewer owns the moped (1) or not (0)
* make_model: The make and model of the bike
* review_month: The month the review was given
* web_browser: Web browser used by the user leaving the review
* reviewer_age: Age of the user leaving the review
* primary_use: The main reason the user reports that they use the bike for
* value_for_money: Rating given by the user on value for money of the bike
* overall_rating: Total rating score after combining multiple rating scores

Preprocessing

Before conducting the analysis, the dataset was preprocessed to handle missing values and ensure consistency in data types. Missing values were imputed or removed as appropriate, and string data was converted to numerical values.

Analysis

The following tasks were performed in the analysis:

Visualized the number of reviews from owners and non-owners to determine whether the observations are balanced across categories of the variable owned.
Described the distribution of the overall rating across the possible values.
Examined the relationship between ownership and overall rating using a scatterplot.
Developed a baseline model to predict whether a review came from an owner or not.
Developed a comparison model to predict whether a review came from an owner or not.
Compared the performance of the two models using accuracy, precision, and recall metrics.
Conclusion
Based on the analysis, we found that the majority of reviews were written by owners, and that the overall ratings were generally positive. The scatterplot showed a weak positive relationship between ownership and overall rating. We developed two models to predict whether a review was written by an owner or not, and found that the comparison model performed better than the baseline model.

Future Work

Future work could include exploring the relationship between other variables in the dataset, such as make and model, and overall rating. Additionally, alternative modeling techniques could be explored to improve the accuracy and performance of the prediction models.
This project aims to use variouse ML techniques and technologies to predict phishing.

To do so Random forest, Decision Trees, Gradient Boosting, Logistic Regression, AdaBoost, KNN and XGB Classifiers were used.

Process workflow - 

Step 1: Data Ingestion - Fetches phishing data from MongoDB client.
Step 2: Data transformation - Handles missing values with KNN Imputer, performs train test split, saves object in their directories.
Step 3: Data Vaildation - Compares count of columns, Data drift checks
Step 4: Model Training - Uses ML flow to track F1 score precision and recall score. Using GridSearchCV compares multiple models at multiple hyperparameters.
                          Best model is used to predict the output for the phishing data.

Step 5: A simple web application layer using FastAPI and flask for interaction
Step 6: Using GitHub Actions deployed a CI/CD pipeline to GCP and dockerized for containerisation. 

The trained model was deployed as rest API on GCP Compute Engine.

Trained models, transformation pipeline, and datasets were stored into GCP.

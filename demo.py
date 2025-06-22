from datetime import datetime
import pandas as pd
from feast import FeatureStore

# Load feature store
store = FeatureStore(repo_path="feature_repo")

# Create entity dataframe
entity_df = pd.DataFrame.from_dict({
    "flower_id": [1, 2, 3],
    "event_timestamp": [datetime.utcnow(), datetime.utcnow(), datetime.utcnow()],
})

# Fetch historical features
features = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_features:sepal_length",
        "iris_features:sepal_width",
        "iris_features:petal_length",
        "iris_features:petal_width",
        "iris_features:species",
    ],
)

df = features.to_df()
print(df)

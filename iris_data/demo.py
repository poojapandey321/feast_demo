import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path=".")

entity_df = pd.DataFrame({
    "flower_id": [1, 2, 3],
    "event_timestamp": pd.to_datetime(["2025-06-01T10:00:00"] * 3)
})

features = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_features:sepal_length",
        "iris_features:sepal_width",
        "iris_features:petal_length",
        "iris_features:petal_width",
    ]
)

df = features.to_df()
print(df)

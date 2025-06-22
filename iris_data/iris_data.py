import pandas as pd
from datetime import timedelta
from feast.types import Float32

from feast import Entity, FeatureView, Field, FileSource, ValueType

# Create flower_id and timestamp
def prepare_iris_csv():
    df = pd.read_csv("../data/iris.csv")
    df.insert(0, "flower_id", range(1, len(df) + 1))
    df["event_timestamp"] = pd.to_datetime("2025-06-01T10:00:00")
    df.to_csv("../data/iris_feast.csv", index=False)
    print("iris_feast.csv created.")

prepare_iris_csv()

# Define Feast entity, source, and feature view
flower = Entity(name="flower_id", join_keys=["flower_id"], value_type=ValueType.INT64)

iris_source = FileSource(
    path="../data/iris_feast.csv",
    event_timestamp_column="event_timestamp",
)

iris_fv = FeatureView(
    name="iris_features",
    entities=[flower],
    ttl=timedelta(days=1),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
    ],
    source=iris_source,
)

import pandas as pd
from datetime import datetime
from datetime import timedelta
import os
from feast import Entity, FeatureView, Field, FileSource, ValueType
from feast.types import Float32 
# Step 1: Prepare CSV with timestamp and flower_id
def prepare_iris_csv():
    input_path = os.path.join("..", "data", "iris.csv")
    output_path = os.path.join("..", "data", "iris_feast.csv")

    df = pd.read_csv(input_path)

    # Add unique flower_id
    df.insert(0, "flower_id", range(1, len(df) + 1))

    # Add event_timestamp (same for all rows here)
    df["event_timestamp"] = pd.to_datetime("2025-06-01T10:00:00")

    # Save to new file
    df.to_csv(output_path, index=False)
    print("✅ iris_feast.csv generated.")

# Run preparation
prepare_iris_csv()

# Step 2: Define Feast components
# Entity
flower = Entity(name="flower_id", join_keys=["flower_id"], value_type=ValueType.INT64)


# Source
iris_source = FileSource(
    path="../data/iris_feast.csv",
    event_timestamp_column="event_timestamp",
)

# Feature View
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


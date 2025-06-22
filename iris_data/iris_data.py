import pandas as pd
from datetime import timedelta
from feast.types import Float32
from feast import Entity, FeatureView, Field, FileSource, ValueType
import os

def prepare_iris_csv():
    # Resolve base directory where the script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct full paths
    iris_input_path = os.path.join(base_dir, "../data/iris.csv")
    iris_output_path = os.path.join(base_dir, "../data/iris_feast.csv")

    # Read and write
    df = pd.read_csv(iris_input_path)
    df.insert(0, "flower_id", range(1, len(df) + 1))
    df["event_timestamp"] = pd.to_datetime("2025-06-01T10:00:00")
    df.to_csv(iris_output_path, index=False)

    print(f"iris_feast.csv created at {iris_output_path}")

prepare_iris_csv()

# STEP 2: Define Entity
flower = Entity(name="flower_id", join_keys=["flower_id"], value_type=ValueType.INT64)

# STEP 3: Define File Source
iris_source = FileSource(
    path="../data/iris_feast.csv",
    event_timestamp_column="event_timestamp",
)

# STEP 4: Define Feature View
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

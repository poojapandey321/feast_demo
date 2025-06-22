import pandas as pd
from datetime import timedelta
from feast.types import Float32
from feast import Entity, FeatureView, Field, FileSource, ValueType
import os

# STEP 2: Define Entity
flower = Entity(name="flower_id", join_keys=["flower_id"], value_type=ValueType.INT64)
base_dir = os.path.dirname(os.path.abspath(__file__))
# STEP 3: Define File Source
iris_source = FileSource(
    path=os.path.join(base_dir, "../data/iris_feast.csv"),
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
    online=True,
    source=iris_source,
)

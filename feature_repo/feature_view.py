from feast import FeatureView, Field
from timestemp import timedelta
from feast.types import Float32, String
from feast.entity import Entity
from data_source import iris_source

flower = Entity(name="flower_id", join_keys=["flower_id"])

iris_view = FeatureView(
    name="iris_features",
    entities=[flower],
    ttl=timedelta(days=365),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
        Field(name="species", dtype=String),
    ],
    online=True,
    source=iris_source,
)

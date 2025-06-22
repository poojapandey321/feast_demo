from feast import FileSource
from datetime import timedelta

iris_source = FileSource(
    path="../data/iris_feast.csv",  # CSV path
    event_timestamp_column="event_timestamp",
    created_timestamp_column=None,
    date_partition_column=None,
)

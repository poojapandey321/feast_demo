import os 
def prepare_iris_csv():
    # Resolve base directory where the script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct full paths
    iris_input_path = os.path.join(base_dir, "..iris.csv")
    iris_output_path = os.path.join(base_dir, "..iris_feast.csv")

    # Read and write
    df = pd.read_csv(iris_input_path)
    df.insert(0, "flower_id", range(1, len(df) + 1))
    df["event_timestamp"] = pd.to_datetime("2025-06-01T10:00:00")
    df.to_csv(iris_output_path, index=False)

    print(f"iris_feast.csv created at {iris_output_path}")

prepare_iris_csv()
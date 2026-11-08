import pandas as pd

INPUT_MODE_TO_COLUMNS = [
    "type_of_breast_surgery",
    "cancer_type_detailed",
    "cellularity",
    "er_status_measured_by_ihc",
    "neoplasm_histologic_grade",
    "tumor_other_histologic_subtype",
    "oncotree_code"]

UNKNOWN_COLS = [
    "primary_tumor_laterality",
    "3-gene_classifier_subtype",
    "tumor_stage"]

def input_mutation_count(df: pd.DataFrame) -> None:
    # Only fill NaN values, the existing ones are correct.
    df["mutation_count"] = df["mutation_count"].fillna(0)
    
    
def input_mode_over_columns(df: pd.DataFrame, columns: list[str]) -> None:
    mode = df.mode()
    
    for col in columns:
        df[col] = df[col].fillna(mode[col][0])
    
        
def input_tumor_size(df: pd.DataFrame) -> None:
    median_ = df.median(numeric_only=True)["tumor_size"]
    df["tumor_size"] = df["tumor_size"].fillna(median_)


def fill_unknown_columns(df: pd.DataFrame, columns: list[str]) -> None:
    for col in columns:
        df[col] = df[col].astype("object").fillna("Unknown")
    
    
def drop_outcome_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(subset=["death_from_cancer"])
        

def load_inputed_data(filepath: str, display_logs=None) -> pd.DataFrame:
    df = pd.read_csv(filepath, low_memory=False)
    
    if display_logs:
        print(f"Size : {len(df)} - Missing values : {df.isnull().sum().sum()}")
    
    input_mutation_count(df)
    input_mode_over_columns(df, INPUT_MODE_TO_COLUMNS)
    input_tumor_size(df)
    fill_unknown_columns(df, UNKNOWN_COLS)
    df = drop_outcome_data(df)
    
    if display_logs:
        print(f"Size : {len(df)} - Missing values : {df.isnull().sum().sum()}")

    return df

if __name__ == "__main__":
    df = load_inputed_data("data/METABRIC.csv", display_logs=True)
    
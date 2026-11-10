from impute_missing_data import load_imputed_data, write_imputed_data

if __name__ == "__main__":
    # df = load_imputed_data("data/METABRIC.csv", display_logs=True)
    write_imputed_data("data/METABRIC.csv", "data/METABRIC_imputed.csv")
    
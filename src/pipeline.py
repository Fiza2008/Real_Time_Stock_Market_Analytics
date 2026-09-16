from .config import DEFAULT_SYMBOLS
from .database import create_tables, load_to_database
from .data_ingestion import fetch_stock_data
from .data_processing import clean_data, add_features
from .analytics import calculate_summary, top_volume_records


def run_pipeline(symbols=None):
    symbols = symbols or DEFAULT_SYMBOLS

    create_tables()

    all_data = []

    for symbol in symbols:
        print(f"Fetching data for {symbol}...")
        raw_data = fetch_stock_data(symbol)
        clean = clean_data(raw_data)
        featured = add_features(clean)
        load_to_database(featured)
        all_data.append(featured)

    combined = (
        __import__("pandas").concat(all_data, ignore_index=True)
        if all_data else __import__("pandas").DataFrame()
    )

    print("\n=== Stock Summary ===")
    print(calculate_summary(combined).to_string(index=False))

    print("\n=== Highest Volume Records ===")
    print(top_volume_records(combined).to_string(index=False))

    return combined


if __name__ == "__main__":
    run_pipeline()

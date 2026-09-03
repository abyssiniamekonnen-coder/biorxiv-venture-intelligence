import os
import requests
import pandas as pd

def fetch_biorxiv_preprints(interval="2026-08-01/2026-09-01"):
    url = f"https://api.biorxiv.org/details/biorxiv/{interval}/0/json"
    print("Fetching data from bioRxiv API...")
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        collection = data.get("collection", [])
        print(f"Successfully retrieved {len(collection)} records.")
        return pd.DataFrame(collection)
    else:
        print(f"Error fetching data. HTTP Status: {response.status_code}")
        return pd.DataFrame()

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    df = fetch_biorxiv_preprints()
    
    if not df.empty:
        output_file = "data/raw_biorxiv_data.csv"
        df.to_csv(output_file, index=False)
        print(f"\nSaved raw data to {output_file}")
        print("\n--- Data Sample ---")
        print(df[['doi', 'title', 'category', 'authors']].head())
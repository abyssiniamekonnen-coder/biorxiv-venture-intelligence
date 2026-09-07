import requests
import pandas as pd
import os

def fetch_failed_clinical_trials(max_records=100):
    """
    Fetches terminated, suspended, or withdrawn clinical trials from 
    the ClinicalTrials.gov API v2 to analyze trial failure modes.
    """
    url = "https://clinicaltrials.gov/api/v2/studies"
    
    params = {
        "filter.overallStatus": "TERMINATED,WITHDRAWN,SUSPENDED",
        "pageSize": min(max_records, 100)
    }
    
    print(f"Fetching clinical trial failure data from ClinicalTrials.gov API...")
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error: API returned status code {response.status_code}")
        return None
        
    data = response.json()
    studies = data.get("studies", [])
    
    parsed_data = []
    for study in studies:
        protocol = study.get("protocolSection", {})
        
        nct_id = protocol.get("identificationModule", {}).get("nctId")
        title = protocol.get("identificationModule", {}).get("briefTitle")
        status = protocol.get("statusModule", {}).get("overallStatus")
        why_stopped = protocol.get("statusModule", {}).get("whyStopped", "Not Provided")
        phase = protocol.get("designModule", {}).get("phases", ["Unknown"])
        conditions = protocol.get("conditionsModule", {}).get("conditions", [])
        
        parsed_data.append({
            "nct_id": nct_id,
            "title": title,
            "status": status,
            "why_stopped": why_stopped,
            "phase": ", ".join(phase),
            "conditions": ", ".join(conditions)
        })
        
    df = pd.DataFrame(parsed_data)
    
    os.makedirs("data", exist_ok=True)
    output_path = "data/clinical_failures.csv"
    df.to_csv(output_path, index=False)
    print(f"Successfully saved {len(df)} records to {output_path}")
    
    return df

if __name__ == "__main__":
    fetch_failed_clinical_trials()
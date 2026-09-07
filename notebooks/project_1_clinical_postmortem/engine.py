"""
Project 1: Failed Clinical Trial Post-Mortem & Repurposing Engine
----------------------------------------------------------------
Analyzes trial termination logs, failure reasons, and 
identifies novel repositioning indications for abandoned assets.
"""

import pandas as pd
import os

def run_engine():
    print("Initializing Clinical Trial Post-Mortem Engine...")
    
    # Sample data for failed Phase II/III assets
    data = {
        "drug_name": ["Asset-X", "Compound-Y", "Molecule-Z"],
        "phase_failed": ["Phase III", "Phase II", "Phase III"],
        "failure_reason": ["Lack of Efficacy", "Hepatotoxicity", "Business Pivot"],
        "repurposing_target": ["Traumatic Brain Injury", "Fibrotic Lung Disease", "NASH"]
    }
    
    df = pd.DataFrame(data)
    print("\n--- Failed Assets & Repurposing Candidates ---")
    print(df.to_string(index=False))

if __name__ == "__main__":
    run_engine()
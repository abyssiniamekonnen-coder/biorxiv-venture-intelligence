"""
Biotech Intelligence & R&D Suite - Master Orchestrator
----------------------------------------------------
Orchestrates clinical trial failure analysis and dark proteome target prioritization.
"""

import sys
import os

# Add notebooks/src paths if necessary, or import directly if in the same folder
from target_agent import DarkProteomeAgent

def run_pipeline():
    print("==================================================")
    print("Initializing Biotech Intelligence & R&D Suite...")
    print("==================================================")
    
    # Path to clinical failures data
    data_path = "../data/clinical_failures.csv"
    
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}. Please check your path.")
        return

    # Step 1: Run Dark Proteome Target Agent
    print("\n[Phase 1] Executing Dark Proteome Target Scan...")
    agent = DarkProteomeAgent(data_path)
    df_targets = agent.scan_targets()
    
    print("\n--- Top Prioritized Drug Targets ---")
    print(df_targets.to_string(index=False))
    
    print("\n==================================================")
    print("Pipeline execution complete successfully!")
    print("==================================================")

if __name__ == "__main__":
    run_pipeline()
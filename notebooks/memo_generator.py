import pandas as pd
from datetime import datetime

def generate_investment_memo():
    print("--- Generating Executive Venture Intelligence Memo ---")
    
    # Simulating data ingestion from our target scan pipeline
    memo_data = {
        "Target_ID": ["TGT-001", "TGT-002", "TGT-003"],
        "Protein": ["GPRX", "ZNF99", "KIAA-Alt"],
        "Novelty_Score": [0.89, 0.94, 0.91],
        "Associated_Failures": [3, 1, 5],
        "Investment_Thesis": [
            "High unexplored GPCR variant with robust downstream metabolic pathway coupling.",
            "Exceptional novelty index with minimal historical clinical trial attrition.",
            "Novel structural candidate requiring further target validation."
        ]
    }
    
    df = pd.DataFrame(memo_data)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memo_content = f"""# EXECUTIVE BIOTECH INVESTMENT MEMO
Generated: {timestamp}
Suite: biorxiv-venture-intelligence

## 1. Executive Summary
This memorandum evaluates top-tier dark proteome targets identified via automated bioinformatics pipelines. Targets are scored based on structural novelty, pathway bottleneck optimization, and historical trial failure metrics to de-risk venture investments.

## 2. Prioritized Target Portfolio
{df.to_string(index=False)}

## 3. Strategic Recommendation
Proceed with deep-dive pharmacokinetic modeling on ZNF99 (Target ID: TGT-002) due to its optimal balance of high novelty (0.94) and low historical failure association.
"""
    
    output_filename = "venture_memo.md"
    with open(output_filename, "w") as f:
        f.write(memo_content)
        
    print(f"Successfully generated executive brief: {output_filename}")

if __name__ == "__main__":
    generate_investment_memo()
"""
pathway_optimizer.py
Production-grade metabolic pathway optimization module incorporating
Michaelis-Menten kinetics, multi-variable matrix scans, and JSON export 
for GitHub portfolio readiness.
"""

import json
from datetime import datetime, timezone

class MetabolicPathwayOptimizer:
    def __init__(self, vmax: float = 100.0, km: float = 15.0, yield_threshold: float = 50.0):
        self.max_substrate_input = 100.0
        self.vmax = vmax
        self.km = km
        self.yield_threshold = yield_threshold

    def calculate_enzyme_efficiency(self, substrate_concentration: float) -> float:
        """Computes dynamic conversion efficiency via Michaelis-Menten kinetics."""
        if substrate_concentration <= 0:
            return 0.0
        velocity = (self.vmax * substrate_concentration) / (self.km + substrate_concentration)
        return velocity / self.vmax

    def optimize_pathway(self, pathway_name: str, substrate_concentration: float, flux_rate: float) -> dict:
        efficiency = self.calculate_enzyme_efficiency(substrate_concentration)
        simulated_yield = self.max_substrate_input * flux_rate * efficiency
        is_viable = simulated_yield >= self.yield_threshold

        return {
            "pathway": pathway_name,
            "substrate_concentration": substrate_concentration,
            "flux_rate": flux_rate,
            "conversion_efficiency": round(efficiency, 4),
            "simulated_yield": round(simulated_yield, 2),
            "viable_for_scaleup": is_viable
        }

    def execute_full_pipeline(self, pathway_name: str, concentrations: list, flux_rates: list) -> dict:
        """Executes a multi-variable matrix scan and compiles a structured report."""
        print(f"[*] Executing full pipeline optimization for: {pathway_name} 🧬")
        results = []
        for conc in concentrations:
            for rate in flux_rates:
                res = self.optimize_pathway(pathway_name, conc, rate)
                results.append(res)
        
        viable_count = sum(1 for r in results if r["viable_for_scaleup"])
        
        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "pathway": pathway_name,
            "parameters": {
                "vmax": self.vmax,
                "km": self.km,
                "yield_threshold": self.yield_threshold,
                "max_substrate_input": self.max_substrate_input
            },
            "summary": {
                "total_configurations_tested": len(results),
                "viable_scaleup_configurations": viable_count
            },
            "results": results
        }
        return report

    def save_report_to_json(self, report: dict, filename: str = "optimization_report.json"):
        with open(filename, "w") as f:
            json.dump(report, f, indent=4)
        print(f"[+] Optimization report successfully exported to {filename} 📊")

if __name__ == "__main__":
    import sys
    from pathlib import Path

    # 1. Dynamically import Pharma-Agent Orchestrator
    pharma_path = Path(__file__).resolve().parent.parent / "pharma-agent-core"
    sys.path.append(str(pharma_path))

    try:
        from agent_orchestrator import AgentOrchestrator

        print("=== Step 1: Generating Molecular Candidates ===")
        orchestrator = AgentOrchestrator()
        targets = list(orchestrator.generator.scaffolds.keys())

        passed_targets = []
        for target in targets:
            candidate = orchestrator.generator.generate_candidate(target)
            eval_result = orchestrator.evaluator.evaluate_molecule(candidate)
            if eval_result.get("passes_adme_tox", False):
                passed_targets.append(target)

        print(f"[+] Approved targets for biosyn pathway design: {passed_targets}\n")
    except ImportError:
        print("[!] Pharma-Agent core not found, running with default targets.")
        passed_targets = ["violacein_biosynthesis"]

    # 2. Run SynBio Metabolic Optimization on Approved Targets
    print("=== Step 2: Optimizing Metabolic Pathways ===")
    optimizer = MetabolicPathwayOptimizer()
    concentrations = [10.0, 25.0, 50.0, 100.0]
    flux_rates = [0.5, 0.75, 0.9]

    for target in passed_targets:
        report_data = optimizer.execute_full_pipeline(
            target,
            concentrations,
            flux_rates
        )
        optimizer.save_report_to_json(report_data)
"""
agent_orchestrator.py
Manages the iterative design loop, coordinating the molecule generator 
and property evaluator to find optimal clinical candidates.
"""

from molecule_generator import MoleculeGenerator
from property_evaluator import PropertyEvaluator

class AgentOrchestrator:
    def __init__(self):
        self.generator = MoleculeGenerator()
        self.evaluator = PropertyEvaluator()

    def run_discovery_loop(self, target_name: str):
        """
        Executes the closed-loop optimization cycle.
        """
        print(f"\n[🚀] Initializing Agent Discovery Loop for target: {target_name}")
        
        # Step 1: Generate initial molecular candidate
        smiles = self.generator.generate_candidate(target_name)
        
        # Step 2: Evaluate through property and toxicity filters
        evaluation = self.evaluator.evaluate_molecule(smiles)
        
        # Step 3: Agent decision output
        print("\n[📊] Pipeline Execution Summary:")
        print(f" - Target Profile: {target_name}")
        print(f" - SMILES Candidate: {evaluation['smiles']}")
        print(f" - Molecular Weight: {evaluation['molecular_weight']} g/mol")
        print(f" - Binding Affinity: {evaluation['binding_affinity']} kcal/mol")
        print(f" - Passes ADME/Tox Filters: {evaluation['passes_adme_tox']}")
        
        if evaluation['passes_adme_tox']:
            print("\n[✨] SUCCESS: Candidate cleared for preclinical consideration.")
        else:
            print("\n[!] REFINEMENT NEEDED: Candidate failed safety or binding thresholds.")

if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    
    # Run loop over all targets defined in MoleculeGenerator
    targets = list(orchestrator.generator.scaffolds.keys())
    
    print(f"[*] Starting batch agent run for targets: {targets}\n")
    for target in targets:
        print(f"--- Running Target: {target} ---")
        candidate = orchestrator.generator.generate_candidate(target)  # or your generator's method name
        result = orchestrator.evaluator.evaluate_molecule(candidate)    # or your evaluator's method name
        print(f"[+] Result for {target}: Passes ADME/Tox = {result.get('passes_adme_tox')}\n")
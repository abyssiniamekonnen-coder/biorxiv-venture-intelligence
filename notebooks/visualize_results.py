import json
from pathlib import Path
import matplotlib.pyplot as plt

def plot_optimization_results(report_path="optimization_report.json"):
    path = Path(report_path)
    if not path.exists():
        print(f"[!] Report not found at {report_path}.")
        return

    with open(path, "r") as f:
        data = json.load(f)

    print("[*] Found JSON keys:", list(data.keys()))
    
    results = data.get("optimization_results", data.get("results", []))

    if not results:
        print("[!] Still no results found. Full data content:", data)
        return

    flux_groups = {}
    for res in results:
        rate = res.get("flux_rate", 0.1)
        flux_groups.setdefault(rate, {"conc": [], "yield": []})
        flux_groups[rate]["conc"].append(res.get("substrate_concentration", 0))
        flux_groups[rate]["yield"].append(res.get("simulated_yield", 0))

    plt.figure(figsize=(8, 5))
    for rate, metrics in flux_groups.items():
        plt.plot(metrics["conc"], metrics["yield"], marker='o', label=f"Flux Rate: {rate}")

    plt.title("Metabolic Pathway Optimization")
    plt.xlabel("Substrate Concentration (mM)")
    plt.ylabel("Simulated Yield")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    
    output_image = "optimization_curve.png"
    plt.savefig(output_image, dpi=300)
    print(f"[+] Plot successfully saved to {output_image}")
    plt.show()

if __name__ == "__main__":
    plot_optimization_results()
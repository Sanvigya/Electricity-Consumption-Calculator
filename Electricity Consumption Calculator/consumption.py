"""Feature: daily & monthly consumption and estimated bill."""
from calculations import summarize
from config import DAYS_IN_MONTH


def show_consumption(data):
    rows, total_daily, total_monthly, bill = summarize(data)
    if not rows:
        print("\nNo appliances added yet.")
        return
    rate = data["rate_per_unit"]
    print(f"\n--- Consumption ({DAYS_IN_MONTH}-day month, rate {rate:g}/unit) ---")
    print(f"{'Appliance':<18} {'Daily kWh':>10} {'Monthly kWh':>12} {'Cost':>10}")
    for r in rows:
        label = r["name"] + (f" x{r['qty']}" if r["qty"] > 1 else "")
        print(f"{label:<18} {r['daily']:>10.2f} {r['monthly']:>12.2f} {r['cost']:>10.2f}")
    print("-" * 53)
    print(f"{'TOTAL':<18} {total_daily:>10.2f} {total_monthly:>12.2f} {bill:>10.2f}")
    print(f"\nEstimated daily cost:   {total_daily * rate:.2f}")
    print(f"Estimated monthly bill: {bill:.2f}")

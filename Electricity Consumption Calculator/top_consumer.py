"""Feature: identify the appliance using the most electricity."""
from calculations import summarize


def show_top_consumer(data):
    rows, _, total_monthly, _ = summarize(data)
    if not rows:
        print("\nNo appliances added yet.")
        return
    top = max(rows, key=lambda r: r["monthly"])
    share = (top["monthly"] / total_monthly * 100) if total_monthly else 0
    print("\n--- Highest Consumer ---")
    print(f"{top['name']} uses {top['monthly']:.2f} kWh/month "
          f"({share:.1f}% of total), costing about {top['cost']:.2f}.")


from calculations import daily_kwh, summarize
from config import DAYS_IN_MONTH

TIPS = {
    "heater": "Heaters are power-hungry. Use only when needed and switch off with a timer.",
    "geyser": "Heat water only when needed; switch off the geyser right after use.",
    "iron": "Iron clothes in one batch instead of a few pieces at a time.",
    "ac": "Set the AC to 24-26°C and use sleep mode to cut consumption.",
    "cooler": "Turn off the cooler when you leave the room.",
    "fan": "Switch off fans when the room is empty; consider a 5-star fan.",
    "light": "Replace old bulbs with LED and switch off when not in use.",
    "bulb": "Replace old bulbs with LED (up to 80% less energy).",
    "tube": "Swap tube lights for LED battens to save energy.",
    "charger": "Unplug chargers once devices are full; they draw power idle.",
    "laptop": "Enable power-saving mode and unplug once charged.",
    "kettle": "Boil only the water you need.",
    "fridge": "Keep the fridge away from walls and avoid opening it often.",
    "tv": "Turn off completely instead of leaving on standby.",
    "monitor": "Lower brightness and enable sleep after a few minutes.",
}


def energy_saving_report(data):
    rows, total_daily, total_monthly, bill = summarize(data)
    if not rows:
        print("\nNo appliances added yet.")
        return
    rate = data["rate_per_unit"]
    print("\n========== ENERGY-SAVING REPORT ==========")
    print(f"Total: {total_daily:.2f} kWh/day | {total_monthly:.2f} kWh/month "
          f"| Bill ≈ {bill:.2f}")

    ranked = sorted(rows, key=lambda r: r["monthly"], reverse=True)
    print("\nTop consumers:")
    for i, r in enumerate(ranked[:3], 1):
        share = r["monthly"] / total_monthly * 100 if total_monthly else 0
        print(f"  {i}. {r['name']}: {r['monthly']:.2f} kWh ({share:.1f}%)")

    print("\nTips:")
    shown = set()
    for r in ranked:
        lname = r["name"].lower()
        for key, tip in TIPS.items():
            if key in lname and tip not in shown:
                print(f"  - [{r['name']}] {tip}")
                shown.add(tip)
                break

    top = max(data["appliances"], key=daily_kwh)
    saved = top["wattage"] * top.get("quantity", 1) / 1000.0 * DAYS_IN_MONTH
    print(f"\nQuick win: using '{top['name']}' 1 hour less per day saves "
          f"{saved:.2f} kWh (≈ {saved * rate:.2f}) per month.")
    print("General: switch off appliances when leaving the room, unplug chargers,")
    print("and prefer LED lighting and star-rated appliances.")
    print("==========================================")

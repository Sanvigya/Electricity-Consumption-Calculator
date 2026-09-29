"""Pure energy/bill calculations (no printing, no I/O)."""
from config import DAYS_IN_MONTH


def daily_kwh(appliance):
    qty = appliance.get("quantity", 1)
    return appliance["wattage"] * appliance["hours_per_day"] * qty / 1000.0


def summarize(data):
    """Return (rows, total_daily_kwh, total_monthly_kwh, monthly_bill)."""
    rate = data["rate_per_unit"]
    rows = []
    for a in data["appliances"]:
        daily = daily_kwh(a)
        monthly = daily * DAYS_IN_MONTH
        rows.append({
            "name": a["name"],
            "qty": a.get("quantity", 1),
            "daily": daily,
            "monthly": monthly,
            "cost": monthly * rate,
        })
    total_daily = sum(r["daily"] for r in rows)
    total_monthly = sum(r["monthly"] for r in rows)
    return rows, total_daily, total_monthly, total_monthly * rate

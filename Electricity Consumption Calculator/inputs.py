def ask_float(prompt, min_val=0.0, max_val=None):
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("  Please enter a number.")
            continue
        if val <= min_val:
            print(f"  Value must be greater than {min_val}.")
        elif max_val is not None and val > max_val:
            print(f"  Value must be at most {max_val}.")
        else:
            return val


def ask_int(prompt, min_val=1, max_val=None):
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("  Please enter a whole number.")
            continue
        val = int(raw)
        if val < min_val or (max_val is not None and val > max_val):
            print(f"  Enter a number between {min_val} and {max_val}.")
        else:
            return val

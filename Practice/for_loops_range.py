# Print every element's index and value

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(str(idx) + ": " + names[idx])
    # Or, we can write print(f"{idx}: {names[idx]}"")

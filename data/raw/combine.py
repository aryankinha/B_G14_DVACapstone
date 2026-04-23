"""
Run this script once to reassemble the full dataset locally.
Output: US_Accidents_March23.csv (2.9 GB)
"""
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
part1 = os.path.join(script_dir, "US_Accidents_part1.csv")
part2 = os.path.join(script_dir, "US_Accidents_part2.csv")
output = os.path.join(script_dir, "US_Accidents_March23.csv")

if os.path.exists(output):
    print(f"Already exists: {output}")
    exit(0)

print("Combining parts...")
with open(output, "w", encoding="utf-8") as out:
    with open(part1, "r", encoding="utf-8") as f:
        for line in f:
            out.write(line)
    with open(part2, "r", encoding="utf-8") as f:
        next(f)  # skip header
        for line in f:
            out.write(line)

size = os.path.getsize(output)
print(f"Done: {output} ({size / 1e9:.2f} GB)")

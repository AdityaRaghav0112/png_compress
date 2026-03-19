import subprocess
from pathlib import Path

input_file = Path("inputs/input.png")
output_file = Path("outputs/pico_output.png")

output_file.parent.mkdir(parents=True, exist_ok=True)

# picopt edits in-place, so copy the file to outputs first
import shutil
shutil.copy(input_file, output_file)

result = subprocess.run([
    "picopt",
    "-o",          # optimize
    str(output_file)
], capture_output=True, text=True)

if result.returncode == 0:
    original = input_file.stat().st_size / 1024
    compressed = output_file.stat().st_size / 1024
    saved = (1 - compressed / original) * 100
    print(f"{input_file.name}: {original:.1f}KB → {compressed:.1f}KB ({saved:.1f}% saved)")
    print(result.stdout)
else:
    print(f"Failed: {result.stderr}")
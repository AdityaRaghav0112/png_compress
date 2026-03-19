import subprocess
from pathlib import Path

input_file = Path("inputs/input.png")
output_file = Path("outputs/quant_output.png")

# Make sure the outputs folder exists (not the file itself)
output_file.parent.mkdir(parents=True, exist_ok=True)

result = subprocess.run([
    "pngquant",
    "--quality=65-85",
    "--speed", "1",
    "--strip",
    "--skip-if-larger",
    "--force",
    "--output", str(output_file),
    str(input_file)
], capture_output=True, text=True)

if result.returncode == 0:
    original = input_file.stat().st_size / 1024
    compressed = output_file.stat().st_size / 1024
    saved = (1 - compressed / original) * 100
    print(f"{input_file.name}: {original:.1f}KB → {compressed:.1f}KB ({saved:.1f}% saved)")
elif result.returncode == 98:
    print("Skipped — compressed file would be larger than original")
elif result.returncode == 99:
    print("Skipped — couldn't meet quality target")
else:
    print(f"Failed: {result.stderr}")
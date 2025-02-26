from fontTools.ttLib import TTFont
import os
import shutil

input_dir = r"sf-pro-fonts"
output_dir = r"output-fonts"

if not os.path.exists(output_dir):
  os.mkdir(output_dir)

for file in os.listdir(input_dir):
  file_path = os.path.join(input_dir, file)
  if file.endswith(".ttf"):
    shutil.copy(file_path, output_dir)
  else:
    try:
      font = TTFont(file_path)
      output_path = os.path.join(output_dir, file.replace(".otf", ".ttf"))
      # font.save(output_path)
      if os.path.exists(output_path):
        os.remove(output_path)
      font.save(output_path)
    except Exception as e:
      print(f"Errore durante la conversione del file {file}: {e}")

output_files = os.listdir(output_dir)

for file in output_files:
  print(f"{file}")

print("Conversione completata!")

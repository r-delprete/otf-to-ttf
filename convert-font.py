from fontTools.ttLib import TTFont
import os
import shutil

input_dir = r"input-fonts"
output_dir = r"output-fonts"

if not os.path.exists(output_dir):
  os.mkdir(output_dir)

for root, _, files in os.walk(input_dir):
  relative_path = os.path.relpath(root, input_dir)
  output_subdir = os.path.join(output_dir, relative_path)
  
  if not os.path.exists(output_subdir):
    os.makedirs(output_subdir)

  for file in files:
    file_path = os.path.join(root, file)
    output_path = os.path.join(output_subdir, file.replace(".otf", ".ttf"))

    if file.endswith(".ttf"):
      shutil.copy(file_path, os.path.join(output_subdir, file))
    elif file.endswith(".otf"):
      try:
          if not os.path.exists(output_path):
            font = TTFont(file_path)
            font.save(output_path)
      except Exception as e:
          print(f"Error converting file {file}: {e}")

for root, _, files in os.walk(output_dir):
  for file in files:
    print(os.path.join(root, file))

print("Conversion completed!")


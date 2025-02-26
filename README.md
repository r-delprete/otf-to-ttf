# OTF to TTF Converter Script

This script converts all font files in a specified folder from **OTF** to **TTF** format.  
Any existing **TTF** files will be skipped during the conversion process.

## How to Run the Script

1. Add the fonts you want to convert to the **fonts** folder.  
2. Run the following commands based on your operating system:

### Windows
```sh
.venv/Scripts/activate
pip install -r requirements.txt
python convert-fonts.py
```

### Linux/MacOS
```sh
source .venv/bin/activate
pip install -r requirements.txt
python convert-fonts.py
```

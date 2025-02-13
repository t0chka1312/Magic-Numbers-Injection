# Magic-Numbers-Injection
Injects the Magic Numbers of different image formats into any script so that it is recognized as an image during file uploads. Please note that different filters may be applied and the upload might not be allowed.
```bash
git clone https://github.com/t0chka1312/Magic-Numbers-Injection.git
cd Magic-Numbers-Injection
```
These are the accepted formats:
``` bash
Usage: python3 magic_numbers.py <format> <input_file> <output_file>
Example: python magic_numbers.py jpg shell.php shell.jpg

Supported image formats:
  - jpg
  - jpeg
  - png
  - gif
  - bmp
  - webp
  - tiff
  - tif
  - ico
  - psd
  - svg
  - pdf
  - heic
  - avif
  - cr2
  - nef
  - arw
```

Script syntax:
``` bash
python3 magic_numbers.py <format> <input_file> <output_file>
```

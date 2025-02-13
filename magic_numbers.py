#!/usr/bin/env python3
import sys
import os

# Definiciones de colores ANSI
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
RESET   = "\033[0m"

# Magic numbers para diferentes formatos de imagen
MAGIC_NUMBERS = {
    'jpg': b'\xFF\xD8\xFF\xE0',          # JPEG
    'jpeg': b'\xFF\xD8\xFF\xE0',         # JPEG (alternativa)
    'png': b'\x89PNG\r\n\x1a\n',         # PNG
    'gif': b'GIF89a',                    # GIF
    'bmp': b'BM',                        # BMP
    'webp': b'RIFF\x00\x00\x00\x00WEBPVP8',  # WEBP (simplificado)
    'tiff': b'II*\x00',                  # TIFF (little-endian)
    'tif': b'II*\x00',                   # TIFF (alternativa)
    'ico': b'\x00\x00\x01\x00',           # ICO (icono)
    'psd': b'8BPS',                      # PSD (Photoshop)
    'svg': b'<?xml',                     # SVG (texto XML)
    'pdf': b'%PDF-',                     # PDF (no es una imagen, pero común)
    'heic': b'\x00\x00\x00 ftypheic',     # HEIC (formato de imagen moderno)
    'avif': b'\x00\x00\x00 ftypavif',     # AVIF (formato de imagen moderno)
    'cr2': b'II*\x00\x10\x00\x00\x00CR',  # CR2 (RAW de Canon)
    'nef': b'MM\x00\x2A',                # NEF (RAW de Nikon)
    'arw': b'II*\x00\x08\x00\x00\x00',    # ARW (RAW de Sony)
}

def add_magic_numbers(image_format, input_file, output_file):
    # Verificar si el formato es válido
    if image_format not in MAGIC_NUMBERS:
        print(f"{RED}Formato no soportado: {image_format}{RESET}")
        print("Formatos soportados: " + ", ".join(MAGIC_NUMBERS.keys()))
        sys.exit(1)

    # Obtener los magic numbers para el formato seleccionado
    magic_numbers = MAGIC_NUMBERS[image_format]

    # Construir rutas absolutas basadas en el directorio de trabajo actual
    input_path = os.path.abspath(input_file)
    output_path = os.path.abspath(output_file)

    # Leer el contenido del archivo de entrada
    try:
        with open(input_path, 'rb') as f:
            file_content = f.read()
    except Exception as e:
        print(f"{RED}Error al leer {input_path}: {e}{RESET}")
        sys.exit(1)

    # Escribir el archivo de salida con los magic numbers al principio
    try:
        with open(output_path, 'wb') as f:
            f.write(magic_numbers + file_content)
    except Exception as e:
        print(f"{RED}Error al escribir {output_path}: {e}{RESET}")
        sys.exit(1)

    print(f"{GREEN}Archivo generado: {output_path}{RESET}")
    print(f"{CYAN}Magic numbers de {image_format} añadidos al principio del archivo.{RESET}")

def show_help():
    script_name = os.path.basename(sys.argv[0])
    print(f"{YELLOW}Uso: python {script_name} <formato> <archivo_entrada> <archivo_salida>{RESET}")
    print(f"{YELLOW}Ejemplo: python {script_name} jpg shell.php shell.jpg{RESET}")
    print(f"\n{MAGENTA}Formatos de imagen soportados:{RESET}")
    for fmt in MAGIC_NUMBERS.keys():
        print(f"  - {BLUE}{fmt}{RESET}")
    sys.exit(0)

if __name__ == "__main__":
    # Mostrar ayuda si no se proporcionan argumentos o se usa --help
    if len(sys.argv) != 4 or sys.argv[1] == "--help":
        show_help()

    # Obtener los argumentos
    image_format = sys.argv[1].lower()
    input_file   = sys.argv[2]
    output_file  = sys.argv[3]

    # Ejecutar la función principal
    add_magic_numbers(image_format, input_file, output_file)

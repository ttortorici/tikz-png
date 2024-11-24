"""
Running this script will convert all PDF files found in the same directory and any subdirectories
and save them as PNG images in the directory above this script.

Command Line Arguments:
    - DPI: call this script with a number (e.g. `python convert_png.py 600`) to set the DPI.
           Default value (if no DPI is given) is 300.

Requires:
    - PyMuPDF

author: Teddy Tortorici
"""

from pathlib import Path
import fitz     # from PyMuPDF package


def convert_png(filename: Path, path_to_save: Path = None, dpi: int = 300) -> None:
    """
    Convert a PDF to a PNG image.

    :param filename: Path object of PDF file to convert.
    :param path_to_save: Path object of directory to save to. If None, will save in same directory where the PDF is.
    :param dpi: dots per inch to save the image as. 300 as default.
    """
    if path_to_save is None:
        path_to_save = filename.parent
    pdf = fitz.open(filename)
    page = pdf.load_page(0)
    pixmap = page.get_pixmap(dpi=dpi)
    output_filename = filename.stem + ".png"
    pixmap.save(path_to_save / output_filename)
    print(f"Saved image: {output_filename}")


def cleanup(directory: Path) -> None:
    """
    Crawl down directories and remove LaTeX auxilary files

    :param directory: Path object of directory to crawl down.
    """
    file_types_to_remove = [
        "aux",
        "fdb_latexmk",
        "fls",
        "log",
        "gz",
    ]
    for file_type in file_types_to_remove:
        for file in directory.rglob(f"*.{file_type}"):
            file.unlink()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        dpi = int(sys.argv[1])
    else:
        dpi = 300
    
    # Get the file path to the directory this script is in, regardless of where you call it from
    parent_directory = script_path = Path(__file__).resolve().parent

    # Save PNG images in the directory above
    save_directory = parent_directory.parent

    # Convert each PDF file in that directory to a PNG, and save it in the directory above
    for file in directory.rglob("*.pdf"):
        convert_png(file, save_directory, dpi)

    # Delete LaTeX auxilary files to tidy up the directory and subdirectories
    cleanup(parent_directory)

# tikz-png
A simple script for creating TikZ pngs offline. Run the "/images/tikz/convert_png.py" script to convert every PDF file in "/images/tikz" (and all subdirectories) to a PNG that is saved in "/images".

This is meant to be added to any project that intends to utilize TikZ to make PNG images. This is meant to be an alternative to using [Overleaf](https://www.overleaf.com/) and a cloud-based PDF to PNG converter, so that everything can be integrated into a single, offline project workspace.

## Example usage

This will run the script and create PNGs with 300 DPI:

```
python images/tikz/convert_png.py
```

You can set a different DPI by adding it as an argument in the following way (this will save images with 600 DPI):

```
python images/tikz/convert_png.py 600
```
# Dependencies

This uses [PyMuPDF](https://github.com/pymupdf/PyMuPDF), which can be installed with [pip](https://pypi.org/project/PyMuPDF/):

```
pip install PyMuPDF
```

or with [conda](https://anaconda.org/tc06580/pymupdf):

```
conda install tc06580::pymupdf
```

# Compiling TikZ

You need a [LaTeX distribution](https://www.latex-project.org/get/) to compile TeX files.

To use [VS Code](https://code.visualstudio.com/) to compile the TeX files on Windows, you will also need to install [Perl](https://strawberryperl.com/).

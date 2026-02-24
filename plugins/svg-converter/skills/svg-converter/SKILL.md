---
name: SVG Converter
description: This skill should be used when the user asks to "convert to SVG", "vectorise image", "PNG to SVG", "trace image", "raster to vector", "convert PNG to vector", "make an SVG from image", "batch convert images to SVG", or needs to convert raster images (PNG, JPG, WebP) into scalable vector graphics using vtracer.
version: 0.1.0
---

# SVG Converter

Convert raster images to clean, scalable SVGs using [vtracer](https://github.com/nickmqb/vtracer) vectorisation. Ideal for converting AI-generated artwork, logos, illustrations, and icons into resolution-independent vector format.

## Requirements

Install vtracer via pip:

```bash
pip install vtracer
```

Requires Python 3.7+. The `vtracer` package (currently v0.6.12+) provides both a Python API and the underlying Rust vectorisation engine.

## Usage

The conversion script is located at:

```
${PLUGIN_ROOT}/skills/svg-converter/scripts/convert_to_svg.py
```

### Basic conversion

```bash
python3 convert_to_svg.py input.png -o output.svg
```

### Batch conversion

Convert multiple files to an output directory:

```bash
python3 convert_to_svg.py *.png -o ./svgs/
```

### CLI flags

| Flag | Default | Description |
|------|---------|-------------|
| `--colormode` | `color` | Colour mode: `color` or `binary` |
| `--hierarchical` | `stacked` | Layer mode: `stacked` or `cutout` |
| `--mode` | `spline` | Path mode: `spline`, `polygon`, or `none` |
| `--filter-speckle` | `4` | Remove speckles smaller than N pixels |
| `--color-precision` | `6` | Colour quantisation precision (1–8) |
| `--layer-difference` | `16` | Layer differentiation threshold |
| `--corner-threshold` | `60` | Corner detection threshold (degrees) |
| `--length-threshold` | `4.0` | Minimum path segment length |
| `--max-iterations` | `10` | Maximum fitting iterations |
| `--splice-threshold` | `45` | Path splicing threshold (degrees) |
| `--path-precision` | `3` | Decimal precision for path coordinates |

## Common Recipes

### Standard conversion (recommended default)

Best for AI-generated illustrations, character art, and detailed images. These are the tested defaults built into the script:

```bash
python3 convert_to_svg.py input.png -o output.svg
```

### High-detail conversion

For photographs or images requiring maximum colour fidelity:

```bash
python3 convert_to_svg.py input.png -o output.svg \
  --color-precision 8 \
  --filter-speckle 2 \
  --path-precision 5
```

### Minimal / logo style

For simple logos and icons with fewer colours and cleaner paths:

```bash
python3 convert_to_svg.py input.png -o output.svg \
  --filter-speckle 8 \
  --color-precision 4 \
  --corner-threshold 90
```

### Binary (two-tone) conversion

For silhouettes, stamps, or black-and-white artwork:

```bash
python3 convert_to_svg.py input.png -o output.svg --colormode binary
```

## Tips

- **File size**: SVG output size depends heavily on image complexity. Simple illustrations typically produce 100–300 KB SVGs.
- **Speckle filter**: Increase `--filter-speckle` to reduce noise and file size at the cost of fine detail.
- **Colour precision**: Lower values produce fewer colour layers (smaller files), higher values preserve more gradients.
- **Path precision**: Lower values (2–3) produce smaller files; higher values (5–8) preserve more geometric accuracy.
- **Batch processing**: Use glob patterns to convert entire directories efficiently.

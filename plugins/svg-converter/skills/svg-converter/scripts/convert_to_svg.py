#!/usr/bin/env python3
"""Convert raster images (PNG, JPG, WebP) to SVG using vtracer vectorisation."""

import argparse
import glob
import os
import sys

try:
    import vtracer
except ImportError:
    print("Error: vtracer is not installed. Install it with: pip install vtracer", file=sys.stderr)
    sys.exit(1)


def convert_image(input_path, output_path, **kwargs):
    """Convert a single raster image to SVG."""
    if not os.path.isfile(input_path):
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return False

    input_size = os.path.getsize(input_path)

    vtracer.convert_image_to_svg_py(
        input_path,
        output_path,
        colormode=kwargs["colormode"],
        hierarchical=kwargs["hierarchical"],
        mode=kwargs["mode"],
        filter_speckle=kwargs["filter_speckle"],
        color_precision=kwargs["color_precision"],
        layer_difference=kwargs["layer_difference"],
        corner_threshold=kwargs["corner_threshold"],
        length_threshold=kwargs["length_threshold"],
        max_iterations=kwargs["max_iterations"],
        splice_threshold=kwargs["splice_threshold"],
        path_precision=kwargs["path_precision"],
    )

    if os.path.isfile(output_path):
        output_size = os.path.getsize(output_path)
        print(
            f"  {os.path.basename(input_path)} ({format_size(input_size)}) "
            f"-> {os.path.basename(output_path)} ({format_size(output_size)})"
        )
        return True

    print(f"Error: conversion failed for {input_path}", file=sys.stderr)
    return False


def format_size(size_bytes):
    """Format byte count as human-readable string."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def resolve_inputs(patterns):
    """Expand glob patterns and return list of input file paths."""
    files = []
    for pattern in patterns:
        expanded = glob.glob(pattern)
        if expanded:
            files.extend(expanded)
        elif os.path.isfile(pattern):
            files.append(pattern)
        else:
            print(f"Warning: no files matched: {pattern}", file=sys.stderr)
    return sorted(set(files))


def main():
    parser = argparse.ArgumentParser(
        description="Convert raster images to SVG using vtracer vectorisation.",
        epilog="Examples:\n"
        "  %(prog)s input.png -o output.svg\n"
        "  %(prog)s *.png -o ./svgs/\n"
        "  %(prog)s photo.jpg --color-precision 8 --filter-speckle 2\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "inputs",
        nargs="+",
        help="Input image path(s) or glob patterns",
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output SVG path (single file) or output directory (batch)",
    )

    # vtracer parameters
    parser.add_argument("--colormode", default="color", choices=["color", "binary"],
                        help="Colour mode (default: color)")
    parser.add_argument("--hierarchical", default="stacked", choices=["stacked", "cutout"],
                        help="Layer mode (default: stacked)")
    parser.add_argument("--mode", default="spline", choices=["spline", "polygon", "none"],
                        help="Path mode (default: spline)")
    parser.add_argument("--filter-speckle", type=int, default=4,
                        help="Remove speckles smaller than N pixels (default: 4)")
    parser.add_argument("--color-precision", type=int, default=6,
                        help="Colour quantisation precision 1-8 (default: 6)")
    parser.add_argument("--layer-difference", type=int, default=16,
                        help="Layer differentiation threshold (default: 16)")
    parser.add_argument("--corner-threshold", type=int, default=60,
                        help="Corner detection threshold in degrees (default: 60)")
    parser.add_argument("--length-threshold", type=float, default=4.0,
                        help="Minimum path segment length (default: 4.0)")
    parser.add_argument("--max-iterations", type=int, default=10,
                        help="Maximum fitting iterations (default: 10)")
    parser.add_argument("--splice-threshold", type=int, default=45,
                        help="Path splicing threshold in degrees (default: 45)")
    parser.add_argument("--path-precision", type=int, default=3,
                        help="Decimal precision for path coordinates (default: 3)")

    args = parser.parse_args()

    # Resolve input files
    input_files = resolve_inputs(args.inputs)

    if not input_files:
        print("Error: no input files found.", file=sys.stderr)
        sys.exit(1)

    # Build vtracer kwargs
    vtracer_kwargs = {
        "colormode": args.colormode,
        "hierarchical": args.hierarchical,
        "mode": args.mode,
        "filter_speckle": args.filter_speckle,
        "color_precision": args.color_precision,
        "layer_difference": args.layer_difference,
        "corner_threshold": args.corner_threshold,
        "length_threshold": args.length_threshold,
        "max_iterations": args.max_iterations,
        "splice_threshold": args.splice_threshold,
        "path_precision": args.path_precision,
    }

    # Single file mode: one input + output ends with .svg
    if len(input_files) == 1 and args.output and args.output.lower().endswith(".svg"):
        output_path = args.output
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        success = convert_image(input_files[0], output_path, **vtracer_kwargs)
        sys.exit(0 if success else 1)

    # Batch mode
    output_dir = args.output  # treat -o as directory if not a single .svg path

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    print(f"Converting {len(input_files)} image(s)...\n")

    success_count = 0
    for input_path in input_files:
        base = os.path.splitext(os.path.basename(input_path))[0]
        if output_dir:
            output_path = os.path.join(output_dir, f"{base}.svg")
        else:
            output_path = os.path.join(
                os.path.dirname(input_path), f"{base}.svg"
            )

        if convert_image(input_path, output_path, **vtracer_kwargs):
            success_count += 1

    print(f"\nConverted {success_count}/{len(input_files)} file(s).")
    sys.exit(0 if success_count == len(input_files) else 1)


if __name__ == "__main__":
    main()

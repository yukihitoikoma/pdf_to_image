import argparse
from pathlib import Path
from pdf2image import convert_from_path

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file',
        type=str,
        required=True,
        help='pdf file path'
    )
    parser.add_argument(
        '-output',
        type=str,
        required=True,
        help='output directory path'
    )
    args, _ = parser.parse_known_args()
    return args

def pdf_conv(filepath, output):
    pdf_path = Path(filepath)
    img_path = Path(output)
    convert_from_path(pdf_path, output_folder=img_path, fmt='png', output_file=pdf_path.stem)

if __name__ == '__main__':
    args = get_args()
    pdf_conv(args.file, args.output)
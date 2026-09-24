import argparse

parser = argparse.ArgumentParser(description="Enter the path of text to analyse.")
parser.add_argument("--path")
args = parser.parse_args()

if args.path:
    print(args.path)

path = args.path
from argparse import ArgumentParser

# parser = ArgumentParser(usage="ParserDemo_06.py --verbosity VERBOSITY  23")
parser = ArgumentParser()
parser.add_argument('square', help='display a square of a given number', type=int)
parser.add_argument('--verbosity', help='increase output verbosity')

args = parser.parse_args()

if args.verbosity:
    print("verbosity turned on")
print(args.square**2)


from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('square', help='display a square of a given number', type=int)
parser.add_argument('-v', '--verbosity', help='increase output verbosity')

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")

print(args.square**2)


import argparse

from src.PiGenerator import PiGenerator

parser = argparse.ArgumentParser()
parser.add_argument("--method", help="choose the method (normal(n), imparis(i))",
                    type=str, default='n')
parser.add_argument("depth", help="depth of sum",
                    type=int)
args = parser.parse_args()
engine = PiGenerator()
if args.method == 'n':
    print(engine.MethodeSerieInvCarres(args.depth))
elif args.method == 'i':
    print(engine.MethodeSerieInvCarresImparis(args.depth))

import argparse

from src.Graph import Graph
from src.PiGenerator import PiGenerator


def gen_pi(args):
    engine = PiGenerator()
    if args.method == 'n':
        print(engine.MethodeSerieInvCarres(args.depth))
    elif args.method == 'i':
        print(engine.MethodeSerieInvCarresImparis(args.depth))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Generation of pi parse
    genpi = parser.add_subparsers()
    genpi_pars = genpi.add_parser('genpi', help='Generate pi')
    genpi_pars.add_argument("--method", help="Choose the method (normal(n), imparis(i))",
                            type=str, default='n')
    genpi_pars.add_argument("depth", help="Depth of sum",
                            type=int)
    genpi_pars.set_defaults(func=gen_pi)

    args = parser.parse_args()
    args.func(args)

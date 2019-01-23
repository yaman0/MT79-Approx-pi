import argparse
from src.Data import Data
from src.Graph import Graph
from src.PiGenerator import PiGenerator


def gen_pi(args):
    engine = PiGenerator()
    if args.method == 'n':
        print(engine.MethodeSerieInvCarres(args.depth))
    elif args.method == 'i':
        print(engine.MethodeSerieInvCarresImparis(args.depth))

def displayGraphDiffMethods(args):
    engine = PiGenerator()
    view = Graph()
    result_normal = []
    result_imparis = []
    for k in range(0, args.depth):
        result_normal.append(engine.MethodeSerieInvCarres(k) - engine.realPi())
        result_imparis.append(engine.MethodeSerieInvCarresImparis(k) - engine.realPi())
    view.addData(Data(result_normal, label='classic'))\
        .addData(Data(result_imparis, label='imparis'))\
        .showLegend()\
        .view()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Generation of pi parse
    subparser = parser.add_subparsers()
    genpi_pars = subparser.add_parser('genpi', help='Generate pi')
    genpi_pars.add_argument("--method", help="Choose the method (normal(n), imparis(i))",
                            type=str, default='n')
    genpi_pars.add_argument("depth", help="Depth of sum",
                            type=int)
    genpi_pars.set_defaults(func=gen_pi)

    # Generation of diffgraph parse
    diffgraph_pars = subparser.add_parser('diffgraph', help='Generate pi')
    diffgraph_pars.add_argument("depth", help="Depth of sum",
                            type=int)
    diffgraph_pars.set_defaults(func=displayGraphDiffMethods)

    args = parser.parse_args()
    args.func(args)

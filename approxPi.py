import argparse
import math

from src import tools
from src.Data import Data
from src.Graph import Graph
from src.PiGenerator import PiGenerator
from src.Point import Point


def gen_pi(args):
    engine = PiGenerator()
    if args.method == 'n':
        print(engine.MethodeSerieInvCarres(args.depth))
    elif args.method == 'i':
        print(engine.MethodeSerieInvCarresImparis(args.depth))
    elif args.method == 'r':
        print(engine.methodSerieRamanujan(args.depth))
    elif args.method == 'm':
        print(engine.methodMonteCarlo(args.depth))


def displayGraphDiffMethods(args):
    engine = PiGenerator()
    view = Graph()
    result_normal = []
    result_imparis = []
    for k in range(0, args.depth):
        result_normal.append(math.fabs(engine.MethodeSerieInvCarres(k) - engine.realPi()))
        result_imparis.append(math.fabs(engine.MethodeSerieInvCarresImparis(k) - engine.realPi()))
    view.addData(Data(result_normal, label='classic')) \
        .addData(Data(result_imparis, label='imparis')) \
        .showLegend() \
        .view()


def displayGraphDiffMcMethods(args):
    engine = PiGenerator()
    view = Graph()
    result = []
    for k in range(0, args.depth):
        result.append(math.fabs(engine.MethodeSerieInvCarres(k) - engine.realPi()))
    view.addData(Data(result, label='classic', type='point')) \
        .showLegend() \
        .view()

def findpiwithprecision(args):
    engine = PiGenerator()
    pi = engine.realPi()
    pi = tools.roundless(pi, args.precision)
    estimation = 0
    depth = -1
    while not tools.roundless(estimation, args.precision) == pi:
        depth += 1
        if (args.method == 'n'):
            estimation = engine.MethodeSerieInvCarres(depth)
        elif (args.method == 'i'):
            estimation = engine.MethodeSerieInvCarresImparis(depth)
        elif (args.method == 'r'):
            estimation = engine.methodSerieRamanujan(depth)
        elif (args.method == 'm'):
            estimation = engine.methodMonteCarlo(depth)

    print("Result : " + str(depth))


def montecarlo(args):
    engine = PiGenerator()
    coord = engine.tirage(args.n)
    g = Graph()
    points = []
    for p in coord:
        color = 'blue' if pow(p[0], 2) + pow(p[1], 2) < 1 else 'red'
        points.append(Point(p[0], p[1], size=5, color=color))
    g.addPoints(points)
    g.addCircle1()
    g.setrange([0, 1], [0, 1])
    g.view()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Generation of pi parse
    subparser = parser.add_subparsers(dest='cmd')
    subparser.required = True
    genpi_pars = subparser.add_parser('genpi', help='Generate pi')
    genpi_pars.add_argument("--method", help="Choose the method (normal(n), imparis(i), ramanujan(r))",
                            type=str, default='n')
    genpi_pars.add_argument("depth", help="Depth of sum",
                            type=int)
    genpi_pars.set_defaults(func=gen_pi)

    # Generation of diffgraph parse
    diffgraph_pars = subparser.add_parser('diffgraph', help='Generate pi')
    diffgraph_pars.add_argument("depth", help="Depth of sum",
                                type=int)
    diffgraph_pars.set_defaults(func=displayGraphDiffMethods)

    # Generation of diffgraph parse
    diffgraph_pars = subparser.add_parser('diffgraphmc', help='Diffgraph for monte-carlo')
    diffgraph_pars.add_argument("depth", help="Depth of sum",
                                type=int)
    diffgraph_pars.set_defaults(func=displayGraphDiffMcMethods)

    # Generation of findpi parse
    findpi_pars = subparser.add_parser('findpi', help='Find index to have pi with a precision')
    findpi_pars.add_argument("precision", help="Precision of pi",
                             type=int)
    findpi_pars.add_argument("--method",
                             help="Choose the method (normal(n), imparis(i), ramanujan(r), monte-carlo(m)",
                             type=str, default='n')
    findpi_pars.set_defaults(func=findpiwithprecision)

    # monte carlo
    findpi_pars = subparser.add_parser('circle', help='Show circle of monte carlo')
    findpi_pars.add_argument("n", help="Number of point",
                             type=int)
    findpi_pars.set_defaults(func=montecarlo)

    args = parser.parse_args()
    args.func(args)

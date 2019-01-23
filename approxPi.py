import argparse

from src.Data import Data
from src.Graph import Graph
from src.PiGenerator import PiGenerator

parser = argparse.ArgumentParser()
parser.add_argument("--method", help="choose the method (normal(n), imparis(i))",
                    type=str, default='n')
parser.add_argument("depth", help="depth of sum",
                    type=int)
args = parser.parse_args()
engine = PiGenerator()
# if args.method == 'n':
#     print(engine.MethodeSerieInvCarres(args.depth))
# elif args.method == 'i':
#     print(engine.MethodeSerieInvCarresImparis(args.depth))
c = []
i = []
for k in range(0, args.depth + 1):
    c.append(engine.MethodeSerieInvCarres(k) - engine.realPi())
    i.append(engine.MethodeSerieInvCarresImparis(k) - engine.realPi())

Graph().showLegend().addData(Data(c, label='classic')).addData(Data(i, label='imparis')).view()

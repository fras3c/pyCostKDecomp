#!/usr/bin/env python3
'''
Created on 22/giu/2016

@author: Francesco Lupia
'''

VERSION = "0.3"

DESCRIPTION = """
Compute an optimal COST BASED hypertree decomposition of width <= k (if any) otherwise it returns that it doesn't exist.
"""

import argparse
import glob
import os
import sys
import jpype
from Solver import *

def parse():

    global VERSION

    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog="Copyright " +u"\u00A9" + " 2016  Francesco Lupia (francesco.lupia@unical.it)")

    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION, help='print version number')

    parser.add_argument('INPUTFILE', metavar='<input-filename>', type=str, help='it contains the body of a conjunctive query')

    parser.add_argument('-as', '--atom-sizes', metavar='<filename>', type=str, help='for each query atom p it contains the number of tuples of the relation on which p is defined')

    parser.add_argument('-vd', '--variable-domains', metavar='<filename>', type=str, help='for each variable X it contains the number of distinct values of the domain associated with X')

    parser.add_argument('-k', metavar='<integer>', type=int, required = True, help='upper bound of the width')

    parser.add_argument('-c', '--complete', dest= 'completeON', action = "store_true", help='force a complete decomposition')

    parser.add_argument('-o', '--output', metavar='<output>', type=str, help='output in GV (formerly DOT) format. If -o is not specified then the default output file is \"<filename>.gv\"')

    parser.set_defaults(completeON=False)

    args = parser.parse_args()

    if not os.path.exists(args.INPUTFILE):
        parser.error("The file %s does not exist!" % args.INPUTFILE)
        sys.exit()

    return args


#launch the JVM
def start():
    hhome = os.path.expandvars("$HYPERTREE_HOME")
    jars = (":").join(glob.glob(hhome+"/lib/*.jar"))
 #   print("jars " + jars)
    jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path="+jars)
    #jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path="+jars+":"+hhome+"/bin")

#kill the JVM
def stop():
    jpype.shutdownJVM()


if __name__ == "__main__":

    args = parse()

    filename = args.INPUTFILE

    k = args.k
    atomSizes = args.atom_sizes
    variable_domains = args.variable_domains
    output = args.output

    start()

    solver = Solver(filename, k, args.completeON, output, atomSizes, variable_domains)

    htd = solver.computeHypertreeDecomposion()

    #htd = solver.computeTreeDecomposition()

    stop()

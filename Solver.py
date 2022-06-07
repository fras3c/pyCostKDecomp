'''
Created on 22/giu/2016

@author: Francesco Lupia
'''

import jpype

class Solver:

    def __init__(self, filename, k, completeON, outputFileName, atomsSizes, varsDistinctValues):
        self.filename = filename
        self.k = k
        self.atomsSizes = atomsSizes
        self.varDistinctValues = varsDistinctValues
        self.completeON = completeON

        if outputFileName != None:
            self.outputFileName = outputFileName
        else:
            self.outputFileName = filename


    def computeHypertreeDecomposion(self):

        parser = jpype.JPackage("parser")
        costFunction = "GLSCostFunction"

        print("\nParsing input file:\t\"" + self.filename + "\"... ")

        if self.atomsSizes != None and self.varDistinctValues != None:
            dp = parser.DatalogParser(self.filename, self.atomsSizes, self.varDistinctValues, self.completeON)
        else:
            dp = parser.DatalogParser(self.filename, self.completeON)
            costFunction = "StructuralCostFunction"

        parserTime = dp.getTime()

        print("\nParsing input file and hypergraph construction done in:\t" + '{0:.3f}'.format(parserTime) + " secs");

        print("\nComputing an optimal cost based hypertree decomposition of width up to " + str(self.k) + "...")

        solver = jpype.JPackage("solver")

        htd = solver.HypertreeDecomp(costFunction, self.k, dp, self.completeON, self.outputFileName)

        htd.computeHTD()

        root = htd.getRoot()

        solverTime = htd.getTime()

        if root.getWeight() < jpype.java.lang.Double.MAX_VALUE:

            htd.buildDecomp()
            htd.printDecomp()

            print("\nChecking conditions...")
            result = htd.checkHTDConditions()
            print(htd.conditionsResult())

            print("Computation ended in " + '{0:.3f}'.format(solverTime) + " secs")

            if result:
                print("\nOPTIMAL COST BASED HYPERTREE DECOMPOSITION FOUND!")
                print("cost\t\t\t = " + '{0:.3f}'.format(root.getWeight()))
                print("hypertree-width\t\t = " + str(htd.getWidth()))
                print("vertices\t\t = " + str(htd.getNumberOfVertices()))
                print("query atoms\t\t = " + str(dp.noa()))
                print("query variables\t\t = " + str(dp.nov()))

            print("GV output written to:\t" + self.outputFileName+".gv")

        else:
            print("Hypertree of width " + str(self.k) + " not found!")
            print("Please, can you give me a higher upper bound?")

        print()
        print()

# pyCostKDecomp
A simple python script and command line application for computing an optimal COST BASED hypertree decomposition using CostKDecomp as a library.
This script is meant to facilitate the computations of hypertree decompositions and by default it uses a structural cost function, i.e., it exploits only informations about the hypergraph representation.

Please note that we have also built a custom cost function which can be used in contexts like database query answering where we can use other statistics such as size of relations, selectivity of attributes, indexes, etc.
This function can be used by filling the optional arguments as explained in the "Help" section below.

Compute an optimal COST BASED hypertree decomposition of width <= k (if any)
otherwise it returns that it doesn't exist.

    positional arguments:
    <filename>            it contains the body of a conjunctive query

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         print version number
    -as <filename>, --atom-sizes <filename>
                        for each query atom p it contains the number of tuples
                        of the relation on which p is defined
    -vd <filename>, --variable-domains <filename>
                        for each variable X it contains the number of distinct
                        values of the domain associated with X
    -avd <filename>, --atom-variable-domains <filename>
                        for each query atom p and for each variable X in the
                        scope of p it contains the number of distinct values
                        of X projected on the relation on which p is defined
    -k <integer>          upper bound of the width
    -o <output>, --output <output>
                        output in GV (formerly DOT) format. If -o is not
                        specified then the default output file is
                        "<filename>.gv"
    
System requirements <br/>
1. Python (3.x)
2. jpype 0.6.1 (python)
3. Java (1.8.x)
    
    
Setting up the environment <br/> 
The project requires to meet these two dependencies:
    
    export HYPERTREE_HOME = <the root directory of the PyCostkdecomp project>
    export JAVA_HOME=`/usr/libexec/java_home -v 1.8` # Mac Users
    #or 
    export JAVA_HOME=/usr/lib/jvm/java-8-oracle # Linux Users


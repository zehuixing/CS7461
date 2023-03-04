# traveling salesman algorithm implementation in jython
# This also prints the index of the points of the shortest route.
# To make a plot of the route, write the points at these indexes 
# to a file and plot them in your favorite tool.

import sys
import os
import time
import csv

import java.io.FileReader as FileReader
import java.io.File as File
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random

import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import dist.DiscretePermutationDistribution as DiscretePermutationDistribution
import opt.DiscreteChangeOneNeighbor as DiscreteChangeOneNeighbor
import opt.EvaluationFunction as EvaluationFunction
import opt.GenericHillClimbingProblem as GenericHillClimbingProblem
import opt.HillClimbingProblem as HillClimbingProblem
import opt.NeighborFunction as NeighborFunction
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.example.FourPeaksEvaluationFunction as FourPeaksEvaluationFunction
import opt.ga.CrossoverFunction as CrossoverFunction
import opt.ga.SingleCrossOver as SingleCrossOver
import opt.ga.DiscreteChangeOneMutation as DiscreteChangeOneMutation
import opt.ga.GenericGeneticAlgorithmProblem as GenericGeneticAlgorithmProblem
import opt.ga.GeneticAlgorithmProblem as GeneticAlgorithmProblem
import opt.ga.MutationFunction as MutationFunction
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm
import opt.ga.UniformCrossOver as UniformCrossOver
import opt.prob.GenericProbabilisticOptimizationProblem as GenericProbabilisticOptimizationProblem
import opt.prob.MIMIC as MIMIC
import opt.prob.ProbabilisticOptimizationProblem as ProbabilisticOptimizationProblem
import shared.FixedIterationTrainer as FixedIterationTrainer
import opt.example.TravelingSalesmanEvaluationFunction as TravelingSalesmanEvaluationFunction
import opt.example.TravelingSalesmanRouteEvaluationFunction as TravelingSalesmanRouteEvaluationFunction
import opt.SwapNeighbor as SwapNeighbor
import opt.ga.SwapMutation as SwapMutation
import opt.example.TravelingSalesmanCrossOver as TravelingSalesmanCrossOver
import opt.example.TravelingSalesmanSortEvaluationFunction as TravelingSalesmanSortEvaluationFunction
import shared.Instance as Instance
import util.ABAGAILArrays as ABAGAILArrays
import shared.ConvergenceTrainer as ConvergenceTrainer

from array import array

def train(alg_func, alg_name, ef, iters):
    ef.resetFunctionEvaluationCount()
    fit = ConvergenceTrainer(alg_func)
    FILE_NAME=alg_name+"-travelingsalesman.csv"
    OUTPUT_FILE = os.path.join("data", FILE_NAME)
    with open(OUTPUT_FILE, "wb") as results:
        writer= csv.writer(results, delimiter=',')
        writer.writerow(["iters","fevals","fitness"])
        for i in range(iters):
            fit.train()
            #print str(i) + ", " + str(ef.getFunctionEvaluations()) + ", " + str(ef.value(alg_func.getOptimal()))
            writer.writerow([i, ef.getFunctionEvaluations()-i, ef.value(alg_func.getOptimal())])
            
    print alg_name + ": " + str(ef.value(alg_func.getOptimal()))
    print "Function Evaluations: " + str(ef.getFunctionEvaluations()-iters)
    print "Iters: " + str(iters)
    print "####"


"""
Commandline parameter(s):
    none
"""

# set N value.  This is the number of points
N = 50
random = Random()

points = [[0 for x in xrange(2)] for x in xrange(N)]
for i in range(0, len(points)):
    points[i][0] = random.nextDouble()
    points[i][1] = random.nextDouble()

ef = TravelingSalesmanRouteEvaluationFunction(points)
odd = DiscretePermutationDistribution(N)
nf = SwapNeighbor()
mf = SwapMutation()
cf = TravelingSalesmanCrossOver(ef)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)

print("RHC starts at"+str(time.clock()))
rhc = RandomizedHillClimbing(hcp)
'''
fit = FixedIterationTrainer(rhc, 200000)
fit.train()
print "RHC Inverse of Distance: " + str(ef.value(rhc.getOptimal()))
print "Route:"
path = []
for x in range(0,N):
    path.append(rhc.getOptimal().getDiscrete(x))
print path
'''
train(rhc, "RHC", ef, 1000)  ## 200000
print("RHC ends at"+str(time.clock()))

print("SA starts at"+str(time.clock()))
sa = SimulatedAnnealing(1E12, .999, hcp)
'''
fit = FixedIterationTrainer(sa, 200000)
fit.train()
print "SA Inverse of Distance: " + str(ef.value(sa.getOptimal()))
print "Route:"
path = []
for x in range(0,N):
    path.append(sa.getOptimal().getDiscrete(x))
print path
'''
train(sa, "SA", ef, 1000)  ## 200000
print("SA ends at"+str(time.clock()))

print("GA starts at"+str(time.clock()))
ga = StandardGeneticAlgorithm(2000, 1500, 250, gap)
'''
fit = FixedIterationTrainer(ga, 1000)
fit.train()
print "GA Inverse of Distance: " + str(ef.value(ga.getOptimal()))
print "Route:"
path = []
for x in range(0,N):
    path.append(ga.getOptimal().getDiscrete(x))
print path
'''
train(ga, "GA", ef, 1000) ## 1000
print("GA ends at"+str(time.clock()))
# for mimic we use a sort encoding

ef = TravelingSalesmanSortEvaluationFunction(points);
fill = [N] * N
ranges = array('i', fill)
odd = DiscreteUniformDistribution(ranges);
df = DiscreteDependencyTree(.1, ranges); 
pop = GenericProbabilisticOptimizationProblem(ef, odd, df);
print("MIMIC starts at"+str(time.clock()))
mimic = MIMIC(500, 100, pop)
'''
fit = FixedIterationTrainer(mimic, 1000)
fit.train()
print "MIMIC Inverse of Distance: " + str(ef.value(mimic.getOptimal()))
print "Route:"
path = []
optimal = mimic.getOptimal()
fill = [0] * optimal.size()
ddata = array('d', fill)
for i in range(0,len(ddata)):
    ddata[i] = optimal.getContinuous(i)
order = ABAGAILArrays.indices(optimal.size())
ABAGAILArrays.quicksort(ddata, order)
print order
'''
train(mimic,"MIMIC", ef, 1000) ## 1000
print("MIMIC ends at"+str(time.clock()))
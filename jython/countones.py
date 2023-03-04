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
import opt.example.CountOnesEvaluationFunction as CountOnesEvaluationFunction
import shared.ConvergenceTrainer as ConvergenceTrainer

from array import array

## import data to csv files
def train(alg_func, alg_name, ef, iters):
    ef.resetFunctionEvaluationCount()
    fit = ConvergenceTrainer(alg_func)
    FILE_NAME=alg_name+"-countones.csv"
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

N=80
fill = [2] * N
ranges = array('i', fill)

ef = CountOnesEvaluationFunction()
odd = DiscreteUniformDistribution(ranges)
nf = DiscreteChangeOneNeighbor(ranges)
mf = DiscreteChangeOneMutation(ranges)
cf = SingleCrossOver()
df = DiscreteDependencyTree(.1, ranges)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
print("RHC starts at"+str(time.clock()))
rhc = RandomizedHillClimbing(hcp)
## fit = FixedIterationTrainer(rhc, 200)
## fit.train()
## print "RHC: " + str(ef.value(rhc.getOptimal()))
train(rhc, "RHC", ef, 300)
print("RHC ends at"+str(time.clock()))
print("SA starts at"+str(time.clock()))
sa = SimulatedAnnealing(100, .95, hcp)
## fit = FixedIterationTrainer(sa, 200)
## fit.train()
## print "SA: " + str(ef.value(sa.getOptimal()))
train(sa, "SA", ef, 300)
print("SA ends at"+str(time.clock()))
print("GA starts at"+str(time.clock()))
ga = StandardGeneticAlgorithm(20, 20, 0, gap)
## fit = FixedIterationTrainer(ga, 300)
## fit.train()
## print "GA: " + str(ef.value(ga.getOptimal()))
train(ga, "GA", ef, 300)
print("GA ends at"+str(time.clock()))
print("MIMIC starts at"+str(time.clock()))
mimic = MIMIC(50, 10, pop)
## fit = FixedIterationTrainer(mimic, 100)
## fit.train()
## print "MIMIC: " + str(ef.value(mimic.getOptimal()))
train(mimic,"MIMIC", ef, 300)
print("MIMIC ends at"+str(time.clock()))
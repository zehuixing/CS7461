"""
N-Queens Test. Inspired from the Java file.

-Athira Nair
"""
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


import random

import opt.ga.NQueensFitnessFunction as NQueensFitnessFunction
import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscretePermutationDistribution as DiscretePermutationDistribution
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import opt.DiscreteChangeOneNeighbor as DiscreteChangeOneNeighbor
import opt.EvaluationFunction as EvaluationFunction
import opt.GenericHillClimbingProblem as GenericHillClimbingProblem
import opt.HillClimbingProblem as HillClimbingProblem
import opt.NeighborFunction as NeighborFunction
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.SwapNeighbor as SwapNeighbor
from opt.example import *
import opt.ga.CrossoverFunction as CrossoverFunction
import opt.ga.DiscreteChangeOneMutation as DiscreteChangeOneMutation
import opt.ga.SingleCrossOver as SingleCrossOver
import opt.ga.GenericGeneticAlgorithmProblem as GenericGeneticAlgorithmProblem
import opt.ga.GeneticAlgorithmProblem as GeneticAlgorithmProblem
import opt.ga.MutationFunction as MutationFunction
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm
import opt.ga.SwapMutation as SwapMutation
import opt.prob.GenericProbabilisticOptimizationProblem as GenericProbabilisticOptimizationProblem
import opt.prob.MIMIC as MIMIC
import opt.prob.ProbabilisticOptimizationProblem as ProbabilisticOptimizationProblem
import shared.FixedIterationTrainer as FixedIterationTrainer
import shared.ConvergenceTrainer as ConvergenceTrainer


from array import array

## import data to csv files
def train(alg_func, alg_name, ef, iters):
    ef.resetFunctionEvaluationCount()
    fit = ConvergenceTrainer(alg_func)
    FILE_NAME=alg_name+"-nqueens.csv"
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

N = 50

# ranges = [random.randint(1, N) for i in range(N)]
ef = NQueensFitnessFunction()
odd = DiscretePermutationDistribution(N)
nf = SwapNeighbor()
mf = SwapMutation()
cf = SingleCrossOver()
df = DiscreteDependencyTree(.1)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
pop = GenericProbabilisticOptimizationProblem(ef, odd, df)

print("RHC starts at"+str(time.clock()))
rhc = RandomizedHillClimbing(hcp)
## fit = FixedIterationTrainer(rhc, 200000)
## fit.train()
## rhc_opt = ef.value(rhc.getOptimal())
## print "RHC: " + str(rhc_opt)
# print "RHC: Board Position: "
# print(ef.boardPositions())
train(rhc, "RHC", ef, 3000)  ## 200000
print("RHC ends at"+str(time.clock()))
## print("============================")
print("SA starts at"+str(time.clock()))
sa = SimulatedAnnealing(1E1, .1, hcp)
## fit = FixedIterationTrainer(sa, 200000)
## fit.train()
## sa_opt = ef.value(sa.getOptimal())
## print "SA: " + str(sa_opt)
# print("SA: Board Position: ")
# print(ef.boardPositions())
train(sa, "SA", ef, 3000)  ## 200000
## print("============================")
print("SA ends at"+str(time.clock()))
print("GA starts at"+str(time.clock()))
ga = StandardGeneticAlgorithm(200, 0, 10, gap)
## fit = FixedIterationTrainer(ga, 1000)
## fit.train()
## ga_opt = ef.value(ga.getOptimal())
## print "GA: " + str(ga_opt)
# print("GA: Board Position: ")
# print(ef.boardPositions())
train(ga, "GA", ef, 3000) ## 1000
## print("============================")
print("GA ends at"+str(time.clock()))
print("MIMIC starts at"+str(time.clock()))
mimic = MIMIC(200, 10, pop)
## fit = FixedIterationTrainer(mimic, 1000)
## fit.train()
## mimic_opt = ef.value(mimic.getOptimal())
## print "MIMIC: " + str(mimic_opt)
# print("MIMIC: Board Position: ")
# print(ef.boardPositions())
train(mimic,"MIMIC", ef, 3000)
print("MIMIC ends at"+str(time.clock()))
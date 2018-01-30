import sys
from inkml import *
import random
import itertools
import numpy as np
import os

def generateSegment(file_name, nbStrkMax=4, k = 0):
        segName = file_name
        ink = Inkml(file_name) 

        nbs =  len(ink.strokes)
        #print('nbs = ', nbs)
        StrokesList = range(nbs)
        AllHypMatrix=[]
        
        if (nbStrkMax > nbs):
                nbStrkMax =nbs
        for itNbMaxOfStrkPerObj in range(nbStrkMax):
                itNbMaxOfStrkPerObj+=1
                                
                # add all possible segments
                #AllHypMatrix.extend(itertools.combinations(StrokesList,itNbMaxOfStrkPerObj))
                #or add only seg without time jump

                for i in StrokesList:
                        if i + itNbMaxOfStrkPerObj < nbs:
                                r = range(i,i+itNbMaxOfStrkPerObj)
                                #get real id of the strokes (strings)
                                seg = []
                                
                                for s in r:
                                        seg.append(ink.strkOrder[s])
                                #check if it is not a symbol
                                #print str(seg)

                                if not ink.isRightSeg(set(seg)):
                                        #print "JUNK"
                                        AllHypMatrix.append(seg)
                                               
        symb = Inkml()
        #symb.truth = "junk"
        outputGTfile = open(os.path.splitext(file_name)[0] + ".lg",'a')
        for hyp in AllHypMatrix:
                symb.UI = ink.UI + "_" + str(k)
                symb.strokes = {}
                string_empty = ''
                for s in hyp:
                        symb.strokes[s] = ink.strokes[s]
                symb.segments["0"] = Segment("0","", hyp)
                a = symb.getInkML('kk'+file_name + str(k)+ ".inkml"); print(a)
                outputGTfile.write("{},hypo_{},{},{}{}\n".format('*',k,'*',1.0,string_empty))
                k+=1
        outputGTfile.close()
        return k
    
def main() :
    file_name = sys.argv[1]
    c = generateSegment(file_name) 
    
main ()         

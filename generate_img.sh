#!/bin/bash 

python3 convertInkmlToImg.py MasterVICO/DataSymbol_Iso/task2-trainSymb2014/trainingSymbols 28 0 

python3 convertInkmlToImg.py MasterVICO/DataSymbol_Iso/task2-trainSymb2014/trainingJunk 28 0 

python3 convertInkmlToImg.py MasterVICO/DataSymbol_Iso/task2-validation-isolatedTest2013b 28 0 

python3 convertInkmlToImg.py MasterVICO/DataSymbol_Iso/task2-testSymbols2014/testSymbols 28 0

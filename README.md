GenoquantR
==========

It should be obvious, I suppose, that this is an abandoned project. I don't plan to do anything else with it. 

A Python graphical front end for qPCR analysis and report generation using the "qpcR" and "knitr" R language packages; the front end is currently implemented for Windows.

This is a working program but is fairly limited in function at the moment. It will analyze a qPCR data file that is tab or white-space delineated and quantify the results using the MAC2 model of qPCR kinetics. NOTE: as currently written, the columns in the data file must represent individual reactions and rows must represent cycle fluorescence readings. The program will apply a user entered offset to all wells of the run equally and will produce a PDF report with sample ID, MAC2 curve fit and quantification for every well in the inputed qPCR data file.

For this program to function, the R language interpreter needs to be installed and it needs to be synced to one of the R repositories so that missing packages will be downloaded on the fly. It was written for R 3.0 for Windows.

Far more work is needed in this description. A skilled programmer with understanding of qPCR can probably figure it out; sorry everyone else (I realize that is pretty much everyone else), my goal is to get to you with something very easy. 

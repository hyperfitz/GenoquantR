'''
Created on Oct 20, 2014

@author: Benjamin Patterson
'''

###R-script generator for MAK2 analysis of raw qPCR Data.
###This GUI generates 2 scripts for qPCR analysis using the R language.
###The first script is an R-script that imports qPCR data from a tab or 
###whitespace delineated file into an R-environment and then does qPCR 
###analysis on the data. The second script is an Sweave script that is
###executed by the first script to generate a PDF report based on the
###qPCR analysis. 

###These are dependencies that need to be imported
import Tkinter, tkFileDialog 
from Tkinter import * 
from string import Template
import os
import subprocess

###These are the functions for the buttons. NOTE that the "generate" function has multiple sub-annotations to help in deciphering its logic.
###This is in part because it is many hundreds of lines of code long. 
def openFile1():
    z = tkFileDialog.askdirectory(parent=root,title='Choose a folder containing qPCR data')
    custName1.set(z)
    
def openFile2():
    zz = tkFileDialog.asksaveasfilename(parent=root, filetypes=Formats1, defaultextension=".R", title='Save R-script as')
    custName2.set(zz) 
    
def openFile3():
    zzz = tkFileDialog.asksaveasfilename(parent=root,filetypes=Formats2, defaultextension=".Rnw", title='Save Sweave script as')
    custName3.set(zzz)    
    
def generate():
    ###There are 96 of these "if, else" statements; they go through every one of the sample ID entry fields and create a unique list item
    ###for every field that has an entry.
    if entry_field4.get() == '':
        pass
    else:
        L.append(entry_field4.get())
        
    if entry_field5.get() == '':
        pass
    else:
        L.append(entry_field5.get())
            
    if entry_field6.get() == '':
        pass
    else:
        L.append(entry_field6.get())
        
    if entry_field7.get() == '':
        pass
    else:
        L.append(entry_field7.get()) 
          
    if entry_field8.get() == '':
        pass
    else:
        L.append(entry_field8.get())
        
    if entry_field9.get() == '':
        pass
    else:
        L.append(entry_field9.get())  
          
    if entry_field10.get() == '':
        pass
    else:
        L.append(entry_field10.get())
        
    if entry_field11.get() == '':
        pass
    else:
        L.append(entry_field11.get()) 
         
    if entry_field12.get() == '':
        pass
    else:
        L.append(entry_field12.get())
        
    if entry_field13.get() == '':
        pass
    else:
        L.append(entry_field13.get())
            
    if entry_field14.get() == '':
        pass
    else:
        L.append(entry_field14.get())
        
    if entry_field15.get() == '':
        pass
    else:
        L.append(entry_field15.get()) 
      
      
        
    if entry_field16.get() == '':
        pass
    else:
        L.append(entry_field16.get())
        
    if entry_field17.get() == '':
        pass
    else:
        L.append(entry_field17.get())  
          
    if entry_field18.get() == '':
        pass
    else:
        L.append(entry_field18.get())
        
    if entry_field19.get() == '':
        pass
    else:
        L.append(entry_field19.get())
           
    if entry_field20.get() == '':
        pass
    else:
        L.append(entry_field20.get())
        
    if entry_field21.get() == '':
        pass
    else:
        L.append(entry_field21.get()) 
           
    if entry_field22.get() == '':
        pass
    else:
        L.append(entry_field22.get())
        
    if entry_field23.get() == '':
        pass
    else:
        L.append(entry_field23.get())  
        
    if entry_field24.get() == '':
        pass
    else:
        L.append(entry_field24.get())
        
    if entry_field25.get() == '':
        pass
    else:
        L.append(entry_field25.get())
            
    if entry_field26.get() == '':
        pass
    else:
        L.append(entry_field26.get())
        
    if entry_field27.get() == '':
        pass
    else:
        L.append(entry_field27.get()) 
        
      
        
    if entry_field28.get() == '':
        pass
    else:
        L.append(entry_field28.get())
        
    if entry_field29.get() == '':
        pass
    else:
        L.append(entry_field29.get()) 
           
    if entry_field30.get() == '':
        pass
    else:
        L.append(entry_field30.get())
        
    if entry_field31.get() == '':
        pass
    else:
        L.append(entry_field31.get()) 
          
    if entry_field32.get() == '':
        pass
    else:
        L.append(entry_field32.get())
        
    if entry_field33.get() == '':
        pass
    else:
        L.append(entry_field33.get())  
          
    if entry_field34.get() == '':
        pass
    else:
        L.append(entry_field34.get())
        
    if entry_field35.get() == '':
        pass
    else:
        L.append(entry_field35.get())  
        
    if entry_field36.get() == '':
        pass
    else:
        L.append(entry_field36.get())
        
    if entry_field37.get() == '':
        pass
    else:
        L.append(entry_field37.get())
            
    if entry_field38.get() == '':
        pass
    else:
        L.append(entry_field38.get())
        
    if entry_field39.get() == '':
        pass
    else:
        L.append(entry_field39.get()) 
        
  
        
    if entry_field40.get() == '':
        pass
    else:
        L.append(entry_field40.get())
        
    if entry_field41.get() == '':
        pass
    else:
        L.append(entry_field41.get())
            
    if entry_field42.get() == '':
        pass
    else:
        L.append(entry_field42.get())
        
    if entry_field43.get() == '':
        pass
    else:
        L.append(entry_field43.get())
           
    if entry_field44.get() == '':
        pass
    else:
        L.append(entry_field44.get())
        
    if entry_field45.get() == '':
        pass
    else:
        L.append(entry_field45.get()) 
           
    if entry_field46.get() == '':
        pass
    else:
        L.append(entry_field46.get())
        
    if entry_field47.get() == '':
        pass
    else:
        L.append(entry_field47.get())
          
    if entry_field48.get() == '':
        pass
    else:
        L.append(entry_field48.get())
        
    if entry_field49.get() == '':
        pass
    else:
        L.append(entry_field49.get())
            
    if entry_field50.get() == '':
        pass
    else:
        L.append(entry_field50.get())
        
    if entry_field51.get() == '':
        pass
    else:
        L.append(entry_field51.get()) 
  
        
        
    if entry_field52.get() == '':
        pass
    else:
        L.append(entry_field52.get())
        
    if entry_field53.get() == '':
        pass
    else:
        L.append(entry_field53.get())
            
    if entry_field54.get() == '':
        pass
    else:
        L.append(entry_field54.get())
        
    if entry_field55.get() == '':
        pass
    else:
        L.append(entry_field55.get())
           
    if entry_field56.get() == '':
        pass
    else:
        L.append(entry_field56.get())
        
    if entry_field57.get() == '':
        pass
    else:
        L.append(entry_field57.get())  
          
    if entry_field58.get() == '':
        pass
    else:
        L.append(entry_field58.get())
        
    if entry_field59.get() == '':
        pass
    else:
        L.append(entry_field59.get())
          
    if entry_field60.get() == '':
        pass
    else:
        L.append(entry_field60.get())
        
    if entry_field61.get() == '':
        pass
    else:
        L.append(entry_field61.get())
            
    if entry_field62.get() == '':
        pass
    else:
        L.append(entry_field62.get())
        
    if entry_field63.get() == '':
        pass
    else:
        L.append(entry_field63.get()) 
         



    if entry_field64.get() == '':
        pass
    else:
        L.append(entry_field64.get())
        
    if entry_field65.get() == '':
        pass
    else:
        L.append(entry_field65.get())  
          
    if entry_field66.get() == '':
        pass
    else:
        L.append(entry_field66.get())
        
    if entry_field67.get() == '':
        pass
    else:
        L.append(entry_field67.get()) 
          
    if entry_field68.get() == '':
        pass
    else:
        L.append(entry_field68.get())
        
    if entry_field69.get() == '':
        pass
    else:
        L.append(entry_field69.get())
            
    if entry_field70.get() == '':
        pass
    else:
        L.append(entry_field70.get())
        
    if entry_field71.get() == '':
        pass
    else:
        L.append(entry_field71.get()) 
         
    if entry_field72.get() == '':
        pass
    else:
        L.append(entry_field72.get())
        
    if entry_field73.get() == '':
        pass
    else:
        L.append(entry_field73.get())
            
    if entry_field74.get() == '':
        pass
    else:
        L.append(entry_field74.get())
        
    if entry_field75.get() == '':
        pass
    else:
        L.append(entry_field75.get())  



    if entry_field76.get() == '':
        pass
    else:
        L.append(entry_field76.get())
        
    if entry_field77.get() == '':
        pass
    else:
        L.append(entry_field77.get())
            
    if entry_field78.get() == '':
        pass
    else:
        L.append(entry_field78.get())
        
    if entry_field79.get() == '':
        pass
    else:
        L.append(entry_field79.get())
           
    if entry_field80.get() == '':
        pass
    else:
        L.append(entry_field80.get())
        
    if entry_field81.get() == '':
        pass
    else:
        L.append(entry_field81.get()) 
           
    if entry_field82.get() == '':
        pass
    else:
        L.append(entry_field82.get())
        
    if entry_field83.get() == '':
        pass
    else:
        L.append(entry_field83.get())
          
    if entry_field84.get() == '':
        pass
    else:
        L.append(entry_field84.get())
        
    if entry_field85.get() == '':
        pass
    else:
        L.append(entry_field85.get())
            
    if entry_field86.get() == '':
        pass
    else:
        L.append(entry_field86.get())
        
    if entry_field87.get() == '':
        pass
    else:
        L.append(entry_field87.get())  



    if entry_field88.get() == '':
        pass
    else:
        L.append(entry_field88.get())
        
    if entry_field89.get() == '':
        pass
    else:
        L.append(entry_field89.get()) 
           
    if entry_field90.get() == '':
        pass
    else:
        L.append(entry_field90.get())
        
    if entry_field91.get() == '':
        pass
    else:
        L.append(entry_field91.get()) 
          
    if entry_field92.get() == '':
        pass
    else:
        L.append(entry_field92.get())
        
    if entry_field93.get() == '':
        pass
    else:
        L.append(entry_field93.get()) 
           
    if entry_field94.get() == '':
        pass
    else:
        L.append(entry_field94.get())
        
    if entry_field95.get() == '':
        pass
    else:
        L.append(entry_field95.get())
          
    if entry_field96.get() == '':
        pass
    else:
        L.append(entry_field96.get())  
    
    if entry_field97.get() == '':
        pass
    else:
        L.append(entry_field97.get())  
      
    if entry_field98.get() == '':
        pass
    else:
        L.append(entry_field98.get())  
      
    if entry_field99.get() == '':
        pass
    else:
        L.append(entry_field99.get())  
    
    ###This opens the R-script file designated in the "choose a name and location for your R-script" field; it also designates
    ###that this file is to be written to.
    rfilename = entry_field2.get()
    ggg = open(rfilename, 'w')
    
    ###This writes the preamble to the R-script which includes the directory location of the tab or whitespace delineated qPCR data file.
    input_file_directory = entry_field1.get()
    ggg.write(T1.substitute(path=input_file_directory))
    
    ###This writes entries in the R-script for every sample ID field that has an entry. 
    for item in L:
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T4.substitute())
        ggg.write(T8.substitute(rxn=(L.index(item))+2))
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T5.substitute())
        ggg.write(T9.substitute(rxn=(L.index(item))+2))
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T6.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T7.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T10.substitute())
        ggg.write(entry_field1.get())
        ggg.write(T11.substitute())
        ggg.write(T12.substitute(name=(L.index(item) + 1)))
        ggg.write(T13.substitute(name=(L.index(item) + 1)))
        ggg.write(T14.substitute(name=(L.index(item) + 1)))
        ggg.write(T15.substitute(name=(L.index(item) + 1)))
        ggg.write(T16.substitute(path=entry_field1.get()))
        ggg.write(T17.substitute(name=(L.index(item) + 1)))
        ggg.write(T17a.substitute(name=(L.index(item) + 1)))
        ggg.write(T17a2.substitute())
        ggg.write(T18.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T19.substitute())
        ggg.write(entry_field1.get())
        ggg.write(T20.substitute(name=(L.index(item) + 1)))
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T21.substitute())
        ggg.write(entry_field1.get())
        ggg.write(T22.substitute(name=(L.index(item) + 1)))
        ggg.write(T23.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T24.substitute(WA="n"))
        ggg.write(T23.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T24.substitute(WA="n"))
        ggg.write(T23.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T24.substitute(WA="n"))
        ggg.write(T25.substitute(name=item))
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T24.substitute(WA="n"))
        ggg.write(T23.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T24.substitute(WA="n"))
        ggg.write(T26.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T27.substitute())
        ggg.write(T28.substitute(name=(L.index(item) + 1)))
        ggg.write(T29.substitute(name=(L.index(item) + 1)))
        ggg.write(T30.substitute())
        ggg.write(T23.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T24.substitute(WA="n"))
        ggg.write(T31.substitute(name=(L.index(item) + 1)))
        ggg.write(T32.substitute())
        ggg.write(T33.substitute(name=(L.index(item) + 1)))
        ggg.write(T34.substitute(eff="eff2$eff" ,name=(L.index(item) + 1)))
        ggg.write(T32.substitute())
        ggg.write(T23.substitute())
        ggg.write(T3.substitute(name=(L.index(item) + 1)))
        ggg.write(T24.substitute(WA="n"))
        ggg.write(T35.substitute(Ge=entry_field101.get(), name=(L.index(item) + 1)))
        ggg.write(T32.substitute())
        ggg.write(T36.substitute(name=(L.index(item) + 1)))
        ggg.write(T37.substitute(raw="$D0*", offset=entry_field100.get(), name=(L.index(item) + 1)))
        ggg.write(T32.substitute())
        ggg.write(T38.substitute(name=(L.index(item) + 1)))
        ggg.write(T39.substitute())
        
    ###These write entries into the R-script for executing the Sweave script that gets generated below.
    ggg.write(T45.substitute(path=os.path.dirname(entry_field3.get())))       
    ggg.write(T40.substitute(path=entry_field3.get()))
    S = T41.substitute(path=entry_field3.get())
    R = "tex"
    Y = '") \n'
    S = S[0:-10] + R + Y
    ggg.write(S)
    
    ###This finalizes the R-script file.
    ggg.close()


    ###This opens the Sweave file designated in the "choose a name and location for the report file" field; it also designates
    ###that this file is to be written to.
    aaa = open(entry_field3.get(), 'w')
    
    ###This writes the preamble to the Sweave script which includes the title for the report designated in the "choose a title for the report" field.
    aaa.write(T42.substitute(itle="title", egin="begin", En=entry_field102.get()))
    
    ###This writes entries to the Sweave script for every sample ID entry field that has an entry.
    for item in L:
        
        aaa.write(T43.substitute(egin="begin", input="verbatiminput", indent="noindent", path=entry_field1.get(), name=(L.index(item) + 1)))
        
        ###This creates a page break in the report after every three entries.
        if (L.index(item) + 1) % 3 == 0:
            aaa.write(T46.substitute(oday="today", En=entry_field102.get()))
        else:
            pass
    
    ###These finalize the Sweave script. These are also the end of the "generate" function.
    aaa.write(T44.substitute())    
    aaa.close()

    #rfilename is the R file input in the GUI
    #after generating the R script, we use os to execute
    #the script in the shell using the R executable
    #I followed the instructions here to figure out the
    #exact command to use:
    # http://akastrin.wordpress.com/2009/06/18/batch-processing-with-r/
    
    os.system("R --vanilla --slave < " + rfilename)
    #cleanup
    
    #input_file_directory
    #cleanup R-generated files
    for fname in os.listdir(input_file_directory):
        #to make this work for all but pdf files, use this!
        #if not fname.endswith(".pdf"):
        if fname.startswith("R"):
            os.remove(os.path.join(input_file_directory, fname))
        
    
    
###These are the templates that get written into the scripts. 
T1 = Template('library(qpcR) \nlibrary(scales) \nlibrary(knitr) \nsetwd("$path") \nPATHall <- paste("$path", sep = "") \nq1 <- pcrimport(PATHall, sep = "", \ndec = ".", delCol = 0, delRow = 0, \nformat = "col", sampleDat = 0, \nnames = 0, sampleLen = 0, \ncheck = FALSE) \nsetwd("$path")\n')
T3 = Template('R$name')
T4 = Template('_ob <- pcrfit(q1[[1]], 1, ')
T5 = Template('_ob_eff1 <- pcrfit(q1[[1]], 1, ')
T6 = Template('_ob_eff2 <- efficiency(')
T7 = Template('_ob_eff1, plot = FALSE)\n')
T8 = Template('$rxn, mak2)\n')
T9 = Template('$rxn, model = l5)\n')
T10 = Template(' <- file("')
T11 = Template('/')
T12 = Template('R$name", "w")\n')
T13 = Template('capture.output(R$name')
T14 = Template('_ob, file = R$name)\n')
T15 = Template('close(R$name)\n')
T16 = Template('jpeg("$path')
T17 = Template('/R$name.jpg")\n')
T17a = Template('plot(R$name')
T17a2 = Template('_ob)\n')
T18 = Template('dev.off()\n')
T19 = Template('_table <- read.table("')
T20 = Template('/R$name", header = TRUE, nrows = 1, skip = 3, dec = ".")\n')
T21 = Template('_file <- file("')
T22 = Template('/R$name.txt", "w")\n')
T23 = Template('cat(" ", file=')
T24 = Template('_file, append=TRUE, "\$WA")\n')
T25 = Template('cat("  Analysis for sample ID: $name", file=')
T26 = Template('cat("  R squared:  ", file=')
T27 = Template('_file, append=TRUE)\n')
T28 = Template('write.table(signif(Rsq(R$name')
T29 = Template('_ob), digits=3), quote=FALSE, row.names=FALSE, col.names=FALSE, file=R$name')
T30 = Template('_file, append=TRUE)\n')
T31 = Template('cat("  PCR efficiency:  ", file=R$name')
T32 = Template('_file, append=TRUE)\n')
T33 = Template('write.table((percent((R$name')
T34 = Template('_ob_$eff-1))), quote=FALSE, row.names=FALSE, col.names=FALSE, file=R$name')
T35 = Template('cat("  $Ge:  ", file=R$name')
T36 = Template('write.table(R$name')
T37 = Template('_table$raw$offset, row.names=FALSE, col.names=FALSE, file=R$name')
T38 = Template('close(R$name')
T39 = Template('_file)\n')
T40 = Template('knit("$path")\n')
T41 = Template('tools::texi2pdf("$path.tex")\n')
T45 = Template('setwd("$path")\n')


###More templates. These are all for the Sweave script.
T42 = Template('\documentclass[a0,portrait]{a0poster} \n\usepackage{multicol} \n\columnsep=50pt \n\usepackage{subfig} \n\usepackage{graphicx} \n\usepackage[font=Large,labelfont=bf]{caption} \n\usepackage{verbatim} \n\usepackage[margin=2.5in]{geometry} \n\$itle{$En} \n\$egin{document} \n \n')
T43 = Template('\maketitle \n \n\$egin{multicols}{2} \n \n\LARGE\$input{$path/R$name.txt} \n \n  \$indent \n  \$egin{minipage}{\columnwidth} \n    \makeatletter \n    \makeatother \n    \centering \n    {% \n      \includegraphics[width=25cm]{$path/R$name.jpg}% \n      \label{qPCR Curve Fit}% \n    }\qquad% \n \n    qPCR Curve Fit \n \n  \end{minipage} \n \n\end{multicols} \n \n')
T44 = Template('\end{document}')
T46 = Template('\pagebreak[4] \n \n\pagestyle{plain} \n \n\paragraph{} ~\\ \n \n\LARGE\centering{$En}  ~\\ \n \n\large\paragraph{} ~\\ \n \n\large\date{\$oday} \n \n')


###This creates an empty list that gets populated by the "generate" function.
L = []

###These designate the file formats that are available when the browse buttons get pressed.
Formats1 = [('R-Language script file','*.R')]
Formats2 = [('Sweave format script file','*.Rnw')]

###This initiates the GUI window.
root = Tk()

###This defines the title of the window.
root.title("R-Script Generator")

###This defines upper left window icon.
root.iconbitmap('R-Gen.ico')

###These designate objects to be populated with the text of directory locations entered by the GUI user.
custName1 = StringVar()
custName2 = StringVar()
custName3 = StringVar()
custName4 = StringVar()
custName5 = StringVar()

###These are the text for all the labels and explanations in the GUI EXCEPT the numbers that appear next to each sample ID entry field.
lbl_id = Tkinter.Label(text='MAK2 R-Script Generator', 
                       height = 1, font = "Times 16 bold")
lbl_id_sub = Tkinter.Label(text='This R-script generator will take raw quantitative \n PCR data, in the form of a tab or whitespace delineated file \n containing numeric fluorescence intensity values, and generate \n an R-script that will analyze the data using MAK2 analysis and \n produce a PDF file including quantification results for \n each sample analyzed.', font = "Times 12")
lbl_id2 = Tkinter.Label(text='------------------------------------------------------------------------------------------------------------------------------------------')
lbl_id2_sub = Tkinter.Label(text='Select input and output preferences', height = 2, font = "Times 13 bold")
lbl_id3 = Tkinter.Label(text='Choose a folder containing a qPCR data file (tab or whitespace delineated):')
lbl_id3_sub = Tkinter.Label(text='Note: the folder must contain only one file! The file must contain only \nfluorescence data, no column or row names. Also, the data must be organized \nsuch that columns represent PCR reactions and rows represent PCR cycles.', justify=LEFT)
lbl_id4 = Tkinter.Label(text='Choose a name and location for your R-script:')
lbl_id4_supl = Tkinter.Label(text='Choose a title for the report:')
lbl_id6_supl = Tkinter.Label(text='This title will appear at the head of every page of the report that gets \ngenerated by the R-script when it gets run using an R console.', justify=LEFT)
lbl_id4_sub = Tkinter.Label(text='Note: the R-script file must be located in a different folder than the qPCR \ndata file. In order for the qPCR data to be analyzed and a PDF report to be \ngenerated, this R-script must be run in an R console.', justify=LEFT)
lbl_id5 = Tkinter.Label(text='Choose a name and location for the report file:')
lbl_id5_sup = Tkinter.Label(text='   ')
lbl_id6 = Tkinter.Label(text='Note: this program generates an "S-weave" script file with the ".Rnw" extention. \nWhen the R-script generated by this program is run in an R console, it will read \nthe Sweave script and generate a PDF report in the same folder with the \nSweave script.', justify=LEFT)
lbl_id7 = Tkinter.Label(text='------------------------------------------------------------------------------------------------------------------------------------------')
lbl_id8 = Tkinter.Label(text='Enter your sample names', height=2, font = "Times 13 bold")
lbl_id8_sub = Tkinter.Label(text='Note: it is your responsibility to know which columns correspond to which samples in your data set. \nColumns in your data set are interpreted by this program from left to right, the first column being sample "1", \nthe second being sample "2", etc. The information that you enter in the text box next to each sample number will be the only \nidentifying information for that sample on the final report form. Additionally, blank text boxes are excluded from analysis. If \nyou leave a text box blank for a sample that has a data column in your data file, and there are subsequent columns in your data file, \nthen all following reactions will be mis-labeled. Be sure not to omit a label for any reaction that you have data \nfor in your data file unless you are going to omit all the following reactions as well. \nNOTE ADDITIONALLY that sample IDs entered below for non-existent columns in your data file will cause the R-script to throw an error when it is run.  ')
lbl_id9_sup = Tkinter.Label(text='   ')
lbl_id10_sup = Tkinter.Label(text='  ')
lbl_id10 = Tkinter.Label(text='Enter calibration offset:')
lbl_id11 = Tkinter.Label(text='This multiplier must NOT be equal to zero and \ncan be any valid, contiguous mathematical term. \nExamples: 4*8, (2/5), 10e-07, or 1.', justify=LEFT)
lbl_id12 = Tkinter.Label(text='Enter quantification units:')
lbl_id13 = Tkinter.Label(text='This will appear on the report as the \ndescription for units used in quantification. \nExamples: mg/L, gene copies per mL.', justify=LEFT)

###These are the numbers that appear next to each sample ID entry field.
sampleID1 = Tkinter.Label(text='1.')
sampleID2 = Tkinter.Label(text='2.')
sampleID3 = Tkinter.Label(text='3.')
sampleID4 = Tkinter.Label(text='4.')
sampleID5 = Tkinter.Label(text='5.')
sampleID6 = Tkinter.Label(text='6.')
sampleID7 = Tkinter.Label(text='7.')
sampleID8 = Tkinter.Label(text='8.')
sampleID9 = Tkinter.Label(text='9.')
sampleID10 = Tkinter.Label(text='10.')
sampleID11 = Tkinter.Label(text='11.')
sampleID12 = Tkinter.Label(text='12.')

sampleID13 = Tkinter.Label(text='13.')
sampleID14 = Tkinter.Label(text='14.')
sampleID15 = Tkinter.Label(text='15.')
sampleID16 = Tkinter.Label(text='16.')
sampleID17 = Tkinter.Label(text='17.')
sampleID18 = Tkinter.Label(text='18.')
sampleID19 = Tkinter.Label(text='19.')
sampleID20 = Tkinter.Label(text='20.')
sampleID21 = Tkinter.Label(text='21.')
sampleID22 = Tkinter.Label(text='22.')
sampleID23 = Tkinter.Label(text='23.')
sampleID24 = Tkinter.Label(text='24.')

sampleID25 = Tkinter.Label(text='25.')
sampleID26 = Tkinter.Label(text='26.')
sampleID27 = Tkinter.Label(text='27.')
sampleID28 = Tkinter.Label(text='28.')
sampleID29 = Tkinter.Label(text='29.')
sampleID30 = Tkinter.Label(text='30.')
sampleID31 = Tkinter.Label(text='31.')
sampleID32 = Tkinter.Label(text='32.')
sampleID33 = Tkinter.Label(text='33.')
sampleID34 = Tkinter.Label(text='34.')
sampleID35 = Tkinter.Label(text='35.')
sampleID36 = Tkinter.Label(text='36.')

sampleID37 = Tkinter.Label(text='37.')
sampleID38 = Tkinter.Label(text='38.')
sampleID39 = Tkinter.Label(text='39.')
sampleID40 = Tkinter.Label(text='40.')
sampleID41 = Tkinter.Label(text='41.')
sampleID42 = Tkinter.Label(text='42.')
sampleID43 = Tkinter.Label(text='43.')
sampleID44 = Tkinter.Label(text='44.')
sampleID45 = Tkinter.Label(text='45.')
sampleID46 = Tkinter.Label(text='46.')
sampleID47 = Tkinter.Label(text='47.')
sampleID48 = Tkinter.Label(text='48.')

sampleID49 = Tkinter.Label(text='49.')
sampleID50 = Tkinter.Label(text='50.')
sampleID51 = Tkinter.Label(text='51.')
sampleID52 = Tkinter.Label(text='52.')
sampleID53 = Tkinter.Label(text='53.')
sampleID54 = Tkinter.Label(text='54.')
sampleID55 = Tkinter.Label(text='55.')
sampleID56 = Tkinter.Label(text='56.')
sampleID57 = Tkinter.Label(text='57.')
sampleID58 = Tkinter.Label(text='58.')
sampleID59 = Tkinter.Label(text='59.')
sampleID60 = Tkinter.Label(text='60.')

sampleID61 = Tkinter.Label(text='61.')
sampleID62 = Tkinter.Label(text='62.')
sampleID63 = Tkinter.Label(text='63.')
sampleID64 = Tkinter.Label(text='64.')
sampleID65 = Tkinter.Label(text='65.')
sampleID66 = Tkinter.Label(text='66.')
sampleID67 = Tkinter.Label(text='67.')
sampleID68 = Tkinter.Label(text='68.')
sampleID69 = Tkinter.Label(text='69.')
sampleID70 = Tkinter.Label(text='70.')
sampleID71 = Tkinter.Label(text='71.')
sampleID72 = Tkinter.Label(text='72.')

sampleID73 = Tkinter.Label(text='73.')
sampleID74 = Tkinter.Label(text='74.')
sampleID75 = Tkinter.Label(text='75.')
sampleID76 = Tkinter.Label(text='76.')
sampleID77 = Tkinter.Label(text='77.')
sampleID78 = Tkinter.Label(text='78.')
sampleID79 = Tkinter.Label(text='79.')
sampleID80 = Tkinter.Label(text='80.')
sampleID81 = Tkinter.Label(text='81.')
sampleID82 = Tkinter.Label(text='82.')
sampleID83 = Tkinter.Label(text='83.')
sampleID84 = Tkinter.Label(text='84.')

sampleID85 = Tkinter.Label(text='85.')
sampleID86 = Tkinter.Label(text='86.')
sampleID87 = Tkinter.Label(text='87.')
sampleID88 = Tkinter.Label(text='88.')
sampleID89 = Tkinter.Label(text='89.')
sampleID90 = Tkinter.Label(text='90.')
sampleID91 = Tkinter.Label(text='91.')
sampleID92 = Tkinter.Label(text='92.')
sampleID93 = Tkinter.Label(text='93.')
sampleID94 = Tkinter.Label(text='94.')
sampleID95 = Tkinter.Label(text='95.')
sampleID96 = Tkinter.Label(text='96.')

###These define all the entry fields EXCEPT the sample ID entry fields.
entry_field1 = Tkinter.Entry(width=75, textvariable=custName1)
entry_field2 = Tkinter.Entry(width=75, textvariable=custName2)
entry_field3 = Tkinter.Entry(width=75, textvariable=custName3)
entry_field102 = Tkinter.Entry(width=75)
entry_field100 = Tkinter.Entry(width=25)
entry_field101 = Tkinter.Entry(width=25)

###These define the sample ID entry fields. There are 96 of these.
entry_field4 = Tkinter.Entry(width=12)
entry_field5 = Tkinter.Entry(width=12)
entry_field6 = Tkinter.Entry(width=12)
entry_field7 = Tkinter.Entry(width=12)
entry_field8 = Tkinter.Entry(width=12)
entry_field9 = Tkinter.Entry(width=12)
entry_field10 = Tkinter.Entry(width=12)
entry_field11 = Tkinter.Entry(width=12)
entry_field12 = Tkinter.Entry(width=12)
entry_field13 = Tkinter.Entry(width=12)
entry_field14 = Tkinter.Entry(width=12)
entry_field15 = Tkinter.Entry(width=12)

entry_field16 = Tkinter.Entry(width=12)
entry_field17 = Tkinter.Entry(width=12)
entry_field18 = Tkinter.Entry(width=12)
entry_field19 = Tkinter.Entry(width=12)
entry_field20 = Tkinter.Entry(width=12)
entry_field21 = Tkinter.Entry(width=12)
entry_field22 = Tkinter.Entry(width=12)
entry_field23 = Tkinter.Entry(width=12)
entry_field24 = Tkinter.Entry(width=12)
entry_field25 = Tkinter.Entry(width=12)
entry_field26 = Tkinter.Entry(width=12)
entry_field27 = Tkinter.Entry(width=12)

entry_field28 = Tkinter.Entry(width=12)
entry_field29 = Tkinter.Entry(width=12)
entry_field30 = Tkinter.Entry(width=12)
entry_field31 = Tkinter.Entry(width=12)
entry_field32 = Tkinter.Entry(width=12)
entry_field33 = Tkinter.Entry(width=12)
entry_field34 = Tkinter.Entry(width=12)
entry_field35 = Tkinter.Entry(width=12)
entry_field36 = Tkinter.Entry(width=12)
entry_field37 = Tkinter.Entry(width=12)
entry_field38 = Tkinter.Entry(width=12)
entry_field39 = Tkinter.Entry(width=12)

entry_field40 = Tkinter.Entry(width=12)
entry_field41 = Tkinter.Entry(width=12)
entry_field42 = Tkinter.Entry(width=12)
entry_field43 = Tkinter.Entry(width=12)
entry_field44 = Tkinter.Entry(width=12)
entry_field45 = Tkinter.Entry(width=12)
entry_field46 = Tkinter.Entry(width=12)
entry_field47 = Tkinter.Entry(width=12)
entry_field48 = Tkinter.Entry(width=12)
entry_field49 = Tkinter.Entry(width=12)
entry_field50 = Tkinter.Entry(width=12)
entry_field51 = Tkinter.Entry(width=12)

entry_field52 = Tkinter.Entry(width=12)
entry_field53 = Tkinter.Entry(width=12)
entry_field54 = Tkinter.Entry(width=12)
entry_field55 = Tkinter.Entry(width=12)
entry_field56 = Tkinter.Entry(width=12)
entry_field57 = Tkinter.Entry(width=12)
entry_field58 = Tkinter.Entry(width=12)
entry_field59 = Tkinter.Entry(width=12)
entry_field60 = Tkinter.Entry(width=12)
entry_field61 = Tkinter.Entry(width=12)
entry_field62 = Tkinter.Entry(width=12)
entry_field63 = Tkinter.Entry(width=12)

entry_field64 = Tkinter.Entry(width=12)
entry_field65 = Tkinter.Entry(width=12)
entry_field66 = Tkinter.Entry(width=12)
entry_field67 = Tkinter.Entry(width=12)
entry_field68 = Tkinter.Entry(width=12)
entry_field69 = Tkinter.Entry(width=12)
entry_field70 = Tkinter.Entry(width=12)
entry_field71 = Tkinter.Entry(width=12)
entry_field72 = Tkinter.Entry(width=12)
entry_field73 = Tkinter.Entry(width=12)
entry_field74 = Tkinter.Entry(width=12)
entry_field75 = Tkinter.Entry(width=12)

entry_field76 = Tkinter.Entry(width=12)
entry_field77 = Tkinter.Entry(width=12)
entry_field78 = Tkinter.Entry(width=12)
entry_field79 = Tkinter.Entry(width=12)
entry_field80 = Tkinter.Entry(width=12)
entry_field81 = Tkinter.Entry(width=12)
entry_field82 = Tkinter.Entry(width=12)
entry_field83 = Tkinter.Entry(width=12)
entry_field84 = Tkinter.Entry(width=12)
entry_field85 = Tkinter.Entry(width=12)
entry_field86 = Tkinter.Entry(width=12)
entry_field87 = Tkinter.Entry(width=12)

entry_field88 = Tkinter.Entry(width=12)
entry_field89 = Tkinter.Entry(width=12)
entry_field90 = Tkinter.Entry(width=12)
entry_field91 = Tkinter.Entry(width=12)
entry_field92 = Tkinter.Entry(width=12)
entry_field93 = Tkinter.Entry(width=12)
entry_field94 = Tkinter.Entry(width=12)
entry_field95 = Tkinter.Entry(width=12)
entry_field96 = Tkinter.Entry(width=12)
entry_field97 = Tkinter.Entry(width=12)
entry_field98 = Tkinter.Entry(width=12)
entry_field99 = Tkinter.Entry(width=12)

###These generate the buttons.
entry_load1 = Tkinter.Button(text=u'Browse')
entry_load2 = Tkinter.Button(text=u'Browse')
entry_load3 = Tkinter.Button(text=u'Browse')
entry_load4 = Tkinter.Button(text=u'Generate scripts')

###These designate the window locations of all the GUI labels and information EXCEPT the numbers that appear next to the sample ID entry fields.
lbl_id.grid(row=0, column=0, columnspan=24)
lbl_id_sub.grid(row=1, column=0, columnspan=24)
lbl_id2.grid(row=2, column=0, columnspan=24)
lbl_id2_sub.grid(row=3, column=0, columnspan=24)
lbl_id3.grid(row=4, column=1, sticky=W, columnspan=10)
lbl_id3_sub.grid(row=6, column=1, sticky=W, columnspan=10)
lbl_id4.grid(row=4, column=13, sticky=W, columnspan=10)
lbl_id4_supl.grid(row=8, column=13, sticky=W, columnspan=10)
lbl_id6_supl.grid(row=10, column=13, columnspan=10, sticky=N+W)
lbl_id4_sub.grid(row=6, column=13, sticky=W, columnspan=10)
lbl_id5.grid(row=8, column=1, columnspan=10, sticky=S+W)
lbl_id5_sup.grid(row=7, column=1, columnspan=24)
lbl_id6.grid(row=10, column=1, columnspan=10, sticky=S+W)
lbl_id7.grid(row=11, column=0, columnspan=24)
lbl_id8.grid(row=12, column=0, columnspan=24)
lbl_id8_sub.grid(row=13, column=0, columnspan=24)
lbl_id9_sup.grid(row=14, column=1, columnspan=24)
lbl_id10_sup.grid(row=24, column=7, columnspan=4, sticky=W)
lbl_id10.grid(row=25, column=8, columnspan=7, sticky=W, padx=85)
lbl_id11.grid(row=26, column=12, columnspan=8, sticky=W, padx=18)
lbl_id12.grid(row=25, column=2, columnspan=10, sticky=W)
lbl_id13.grid(row=26, column=5, columnspan=6, sticky=W+N, padx=22)

###These designate the window locations of all of the entry fields EXCEPT the sample ID entry fields.
entry_field1.grid(row=5, column=1, columnspan=10, sticky=W, padx=3)
entry_field2.grid(row=5, column=13, columnspan=10, sticky=W, padx=3)
entry_field3.grid(row=9, column=1, columnspan=10, sticky=W, padx=3)
entry_field102.grid(row=9, column=13, columnspan=10, sticky=W, padx=3)
entry_field100.grid(row=25, column=13, columnspan=3, sticky=W)
entry_field101.grid(row=25, column=4, columnspan=6, sticky=W, padx=46)

###These designate the window locations of all of the sample ID entry fields AND the numbers that appear next to them. There are 192 of these.
sampleID1.grid(row=15, column=0, sticky=E)
entry_field4.grid(row=15, column=1, sticky=W)
sampleID2.grid(row=15, column=2, sticky=E)
entry_field5.grid(row=15, column=3, sticky=W)
sampleID3.grid(row=15, column=4, sticky=E)
entry_field6.grid(row=15, column=5, sticky=W)
sampleID4.grid(row=15, column=6, sticky=E)
entry_field7.grid(row=15, column=7, sticky=W)
sampleID5.grid(row=15, column=8, sticky=E)
entry_field8.grid(row=15, column=9, sticky=W)
sampleID6.grid(row=15, column=10, sticky=E)
entry_field9.grid(row=15, column=11, sticky=W)
sampleID7.grid(row=15, column=12, sticky=E)
entry_field10.grid(row=15, column=13, sticky=W)
sampleID8.grid(row=15, column=14, sticky=E)
entry_field11.grid(row=15, column=15, sticky=W)
sampleID9.grid(row=15, column=16, sticky=E)
entry_field12.grid(row=15, column=17, sticky=W)
sampleID10.grid(row=15, column=18, sticky=E)
entry_field13.grid(row=15, column=19, sticky=W)
sampleID11.grid(row=15, column=20, sticky=E)
entry_field14.grid(row=15, column=21, sticky=W)
sampleID12.grid(row=15, column=22, sticky=E)
entry_field15.grid(row=15, column=23, sticky=W)

sampleID13.grid(row=16, column=0, sticky=E)
entry_field16.grid(row=16, column=1, sticky=W)
sampleID14.grid(row=16, column=2, sticky=E)
entry_field17.grid(row=16, column=3, sticky=W)
sampleID15.grid(row=16, column=4, sticky=E)
entry_field18.grid(row=16, column=5, sticky=W)
sampleID16.grid(row=16, column=6, sticky=E)
entry_field19.grid(row=16, column=7, sticky=W)
sampleID17.grid(row=16, column=8, sticky=E)
entry_field20.grid(row=16, column=9, sticky=W)
sampleID18.grid(row=16, column=10, sticky=E)
entry_field21.grid(row=16, column=11, sticky=W)
sampleID19.grid(row=16, column=12, sticky=E)
entry_field22.grid(row=16, column=13, sticky=W)
sampleID20.grid(row=16, column=14, sticky=E)
entry_field23.grid(row=16, column=15, sticky=W)
sampleID21.grid(row=16, column=16, sticky=E)
entry_field24.grid(row=16, column=17, sticky=W)
sampleID22.grid(row=16, column=18, sticky=E)
entry_field25.grid(row=16, column=19, sticky=W)
sampleID23.grid(row=16, column=20, sticky=E)
entry_field26.grid(row=16, column=21, sticky=W)
sampleID24.grid(row=16, column=22, sticky=E)
entry_field27.grid(row=16, column=23, sticky=W)

sampleID25.grid(row=17, column=0, sticky=E)
entry_field28.grid(row=17, column=1, sticky=W)
sampleID26.grid(row=17, column=2, sticky=E)
entry_field29.grid(row=17, column=3, sticky=W)
sampleID27.grid(row=17, column=4, sticky=E)
entry_field30.grid(row=17, column=5, sticky=W)
sampleID28.grid(row=17, column=6, sticky=E)
entry_field31.grid(row=17, column=7, sticky=W)
sampleID29.grid(row=17, column=8, sticky=E)
entry_field32.grid(row=17, column=9, sticky=W)
sampleID30.grid(row=17, column=10, sticky=E)
entry_field33.grid(row=17, column=11, sticky=W)
sampleID31.grid(row=17, column=12, sticky=E)
entry_field34.grid(row=17, column=13, sticky=W)
sampleID32.grid(row=17, column=14, sticky=E)
entry_field35.grid(row=17, column=15, sticky=W)
sampleID33.grid(row=17, column=16, sticky=E)
entry_field36.grid(row=17, column=17, sticky=W)
sampleID34.grid(row=17, column=18, sticky=E)
entry_field37.grid(row=17, column=19, sticky=W)
sampleID35.grid(row=17, column=20, sticky=E)
entry_field38.grid(row=17, column=21, sticky=W)
sampleID36.grid(row=17, column=22, sticky=E)
entry_field39.grid(row=17, column=23, sticky=W)

sampleID37.grid(row=18, column=0, sticky=E)
entry_field40.grid(row=18, column=1, sticky=W)
sampleID38.grid(row=18, column=2, sticky=E)
entry_field41.grid(row=18, column=3, sticky=W)
sampleID39.grid(row=18, column=4, sticky=E)
entry_field42.grid(row=18, column=5, sticky=W)
sampleID40.grid(row=18, column=6, sticky=E)
entry_field43.grid(row=18, column=7, sticky=W)
sampleID41.grid(row=18, column=8, sticky=E)
entry_field44.grid(row=18, column=9, sticky=W)
sampleID42.grid(row=18, column=10, sticky=E)
entry_field45.grid(row=18, column=11, sticky=W)
sampleID43.grid(row=18, column=12, sticky=E)
entry_field46.grid(row=18, column=13, sticky=W)
sampleID44.grid(row=18, column=14, sticky=E)
entry_field47.grid(row=18, column=15, sticky=W)
sampleID45.grid(row=18, column=16, sticky=E)
entry_field48.grid(row=18, column=17, sticky=W)
sampleID46.grid(row=18, column=18, sticky=E)
entry_field49.grid(row=18, column=19, sticky=W)
sampleID47.grid(row=18, column=20, sticky=E)
entry_field50.grid(row=18, column=21, sticky=W)
sampleID48.grid(row=18, column=22, sticky=E)
entry_field51.grid(row=18, column=23, sticky=W)

sampleID49.grid(row=19, column=0, sticky=E)
entry_field52.grid(row=19, column=1, sticky=W)
sampleID50.grid(row=19, column=2, sticky=E)
entry_field53.grid(row=19, column=3, sticky=W)
sampleID51.grid(row=19, column=4, sticky=E)
entry_field54.grid(row=19, column=5, sticky=W)
sampleID52.grid(row=19, column=6, sticky=E)
entry_field55.grid(row=19, column=7, sticky=W)
sampleID53.grid(row=19, column=8, sticky=E)
entry_field56.grid(row=19, column=9, sticky=W)
sampleID54.grid(row=19, column=10, sticky=E)
entry_field57.grid(row=19, column=11, sticky=W)
sampleID55.grid(row=19, column=12, sticky=E)
entry_field58.grid(row=19, column=13, sticky=W)
sampleID56.grid(row=19, column=14, sticky=E)
entry_field59.grid(row=19, column=15, sticky=W)
sampleID57.grid(row=19, column=16, sticky=E)
entry_field60.grid(row=19, column=17, sticky=W)
sampleID58.grid(row=19, column=18, sticky=E)
entry_field61.grid(row=19, column=19, sticky=W)
sampleID59.grid(row=19, column=20, sticky=E)
entry_field62.grid(row=19, column=21, sticky=W)
sampleID60.grid(row=19, column=22, sticky=E)
entry_field63.grid(row=19, column=23, sticky=W)

sampleID61.grid(row=20, column=0, sticky=E)
entry_field64.grid(row=20, column=1, sticky=W)
sampleID62.grid(row=20, column=2, sticky=E)
entry_field65.grid(row=20, column=3, sticky=W)
sampleID63.grid(row=20, column=4, sticky=E)
entry_field66.grid(row=20, column=5, sticky=W)
sampleID64.grid(row=20, column=6, sticky=E)
entry_field67.grid(row=20, column=7, sticky=W)
sampleID65.grid(row=20, column=8, sticky=E)
entry_field68.grid(row=20, column=9, sticky=W)
sampleID66.grid(row=20, column=10, sticky=E)
entry_field69.grid(row=20, column=11, sticky=W)
sampleID67.grid(row=20, column=12, sticky=E)
entry_field70.grid(row=20, column=13, sticky=W)
sampleID68.grid(row=20, column=14, sticky=E)
entry_field71.grid(row=20, column=15, sticky=W)
sampleID69.grid(row=20, column=16, sticky=E)
entry_field72.grid(row=20, column=17, sticky=W)
sampleID70.grid(row=20, column=18, sticky=E)
entry_field73.grid(row=20, column=19, sticky=W)
sampleID71.grid(row=20, column=20, sticky=E)
entry_field74.grid(row=20, column=21, sticky=W)
sampleID72.grid(row=20, column=22, sticky=E)
entry_field75.grid(row=20, column=23, sticky=W)

sampleID73.grid(row=21, column=0, sticky=E)
entry_field76.grid(row=21, column=1, sticky=W)
sampleID74.grid(row=21, column=2, sticky=E)
entry_field77.grid(row=21, column=3, sticky=W)
sampleID75.grid(row=21, column=4, sticky=E)
entry_field78.grid(row=21, column=5, sticky=W)
sampleID76.grid(row=21, column=6, sticky=E)
entry_field79.grid(row=21, column=7, sticky=W)
sampleID77.grid(row=21, column=8, sticky=E)
entry_field80.grid(row=21, column=9, sticky=W)
sampleID78.grid(row=21, column=10, sticky=E)
entry_field81.grid(row=21, column=11, sticky=W)
sampleID79.grid(row=21, column=12, sticky=E)
entry_field82.grid(row=21, column=13, sticky=W)
sampleID80.grid(row=21, column=14, sticky=E)
entry_field83.grid(row=21, column=15, sticky=W)
sampleID81.grid(row=21, column=16, sticky=E)
entry_field84.grid(row=21, column=17, sticky=W)
sampleID82.grid(row=21, column=18, sticky=E)
entry_field85.grid(row=21, column=19, sticky=W)
sampleID83.grid(row=21, column=20, sticky=E)
entry_field86.grid(row=21, column=21, sticky=W)
sampleID84.grid(row=21, column=22, sticky=E)
entry_field87.grid(row=21, column=23, sticky=W)

sampleID85.grid(row=22, column=0, sticky=E)
entry_field88.grid(row=22, column=1, sticky=W)
sampleID86.grid(row=22, column=2, sticky=E)
entry_field89.grid(row=22, column=3, sticky=W)
sampleID87.grid(row=22, column=4, sticky=E)
entry_field90.grid(row=22, column=5, sticky=W)
sampleID88.grid(row=22, column=6, sticky=E)
entry_field91.grid(row=22, column=7, sticky=W)
sampleID89.grid(row=22, column=8, sticky=E)
entry_field92.grid(row=22, column=9, sticky=W)
sampleID90.grid(row=22, column=10, sticky=E)
entry_field93.grid(row=22, column=11, sticky=W)
sampleID91.grid(row=22, column=12, sticky=E)
entry_field94.grid(row=22, column=13, sticky=W)
sampleID92.grid(row=22, column=14, sticky=E)
entry_field95.grid(row=22, column=15, sticky=W)
sampleID93.grid(row=22, column=16, sticky=E)
entry_field96.grid(row=22, column=17, sticky=W)
sampleID94.grid(row=22, column=18, sticky=E)
entry_field97.grid(row=22, column=19, sticky=W)
sampleID95.grid(row=22, column=20, sticky=E)
entry_field98.grid(row=22, column=21, sticky=W)
sampleID96.grid(row=22, column=22, sticky=E)
entry_field99.grid(row=22, column=23, sticky=W)

###These designate the window locations for the buttons.
entry_load1.grid(row=5, column=10, sticky=W, columnspan=2)
entry_load2.grid(row=5, column=22, sticky=W, columnspan=2)
entry_load3.grid(row=9, column=10, columnspan=2, sticky=W)
entry_load4.grid(row=24, column=17, columnspan=7, rowspan=3)

###These bind the buttons to their functions.
entry_load1['command'] = lambda: openFile1()
entry_load2['command'] = lambda: openFile2()
entry_load3['command'] = lambda: openFile3()
entry_load4['command'] = lambda: generate()


###This closes the code for the window. This is also the end of the program.
root.mainloop()

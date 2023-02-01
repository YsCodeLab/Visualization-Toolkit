#Example to draw from tree branches

import os
import ROOT
from lib.draw_scripts import draw_two_histograms, draw_summary

# --0a. Loading variable name in branch/binning desired and unit for each variable here 
from config.branch_names_binning import binning_dict
from util.units import unit_dict as unit

# --0b. Loading data set 1 and set 2 
from config.signal_file_list import signal_list as signal_filelist
from config.bkg_file_list import dec_bkg_file_list as bkg_filelist 

#---1. Set all the variable names you are interested in running in the histogram
#--Branch name can be tree branch or calculation from tree branch E.G.  pT[0]**2+pT[1]**2
branch_names=binning_dict.keys()
print(len(branch_names))
print(branch_names)


#--2. Add in the cut/histogram name in root file
compare_dict={"Mass0.4-Prompt-Cut1": "hist1", # histogram name
	      "Mass0.4-CTau=X-Cut1": "hist2"
}

#--Setting outputdir for the plots
saveDir="plots/compare_testsamples_%s_%s/"

#--Drawing controls
drawLog=True

#---4. What would you like to draw on your plot
compare=["Mass0.4-Prompt-Cut1",
 	 "Mass0.4-CTau=X-Cut1"]

saveDir=saveDir%(compare[0], compare[1])
os.system("mkdir -p %s"%saveDir)

#---5. Draw Multiple  (Different mass points/different cuts etc, you name it)
f1.ROOT.TFile.Open("FILENAME")

hist_list=[]
for name, hist_name in compare_dict:
    if name in compare:
	    hist_list.append(f1.Get(hist_name))

try:
	draw_summary(hist_list, compare_dict.keys(), branchname , saveDir=saveDir, drawLog=drawLog)
except Exception as e:
	print(e)

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

#--2. Selecting the dataset tree
tree=ROOT.TChain("trees_SRDV_")
tree2=ROOT.TChain("trees_SRDV_")

#---Processing input trees
for i_f_name, f_name in enumerate(bkg_filelist): 
    print("f_name: ", f_name)
    tree.Add(f_name)

for i_f_name, f_name in enumerate(signal_filelist): 
    print("f_name: ", f_name)
    tree2.Add(f_name)

#--3. Add in the cuts desired
compare_dict={"nocut": "1",
              "pass_HLT_6j45":"pass_HLT_6j45",
               "SigMC-CR": "DRAW_pass_triggerFlags&&DRAW_pass_DVJETS&&DV_passMaterialVeto&&DV_passFiducialCut&&DV_passChiSqCut&&DV_passDistCut&&DV_z<400 && DV_m<10", 
               "BkgMC-CR": "DRAW_pass_triggerFlags&&DRAW_pass_DVJETS&&DV_passMaterialVeto&&DV_passFiducialCut&&DV_passChiSqCut&&DV_passDistCut&&DV_z<400 &&DV_m<10", 
	       #"CutFlow-step1"
  	       # "CutFlow-step2"
}

#--Setting outputdir for the plots
saveDir="plots/compare_testsamples_%s_%s/"

#-- Drawing compare 2 histogram plots
#--Drawing controls
ratio=True
drawLog=True
doNormalize=False
# if two files, compare 2 different trees, if not compare just different cuts in the first tree
two_files=True

#---4. What would you like to compare? 
compare=["SigMC-CR",
 	 "BkgMC-CR"]


saveDir=saveDir%(compare[0], compare[1])
os.system("mkdir -p %s"%saveDir)

#---5. Draw Multiple  (Different mass points/different cuts etc, you name it)
for branch_name in branch_names:

    hist_list=[]
    hist_list.append(ROOT.TH1D("hist", "hist", binning_dict[branch_name][0], binning_dict[branch_name][1], binning_dict[branch_name][2]))
    hist_list.append(ROOT.TH1D("hist2", "hist", binning_dict[branch_name][0], binning_dict[branch_name][1], binning_dict[branch_name][2]))

# add all histogramsk

    tree.Draw("%s>>%s"%(branch_name, "hist"), compare_dict[compare[0]])
    tree2.Draw("%s>>%s"%(branch_name, "hist2"), compare_dict[compare[1]])
    #try: 
    print("compare: ", compare)
    draw_summary(hist_list, compare, branch_name, saveDir=saveDir)
    #except Exception as e:
	#print(e)
	#print("drawing two historgram for tree with branch name: %s failed. "%branch_name)

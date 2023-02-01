#Example to draw from tree branches

import os
import ROOT
from lib.draw_scripts import draw_two_histograms, draw_summary

#---1. Set all the variable names you are interested in running in the histogram
var_name="pt"
tag=""

#--2. Open rootfile here 
f1.ROOT.TFile.Open("FILENAME")

#--2. Add in the legend of the histogram(key) and the hisogram name from the rootfile
compare_dict={"Mass0.4-Prompt-Cut1": "hist1",
	      "Mass0.4-CTau=X-Cut1": "hist2"
}

#--3. Setting outputdir for the plots
saveDir="plots/%s_summary/"%(tag)
os.system("mkdir -p %s"%saveDir)

#--Drawing controls
drawLog=True

#---5. Draw Multiple  (Different mass points/different cuts etc, you name it)
hist_list=[]
name_list=[]
for name, hist_name in compare_dict:
    if name in compare:
	    hist_list.append(f1.Get(hist_name))

try:
    draw_summary(hist_list, name_list, var_name , saveDir=saveDir, drawLog=drawLog)
except Exception as e:
    print(e)

import ROOT
from lib.draw_scripts import draw_two_histograms, draw_summary, draw_single
from config.branch_name_binning_non_pointing import binning_dict
import os

# 601519
#tree=ROOT.TChain("CollectionTree")
#tree.Add("/nfs/dust/atlas/user/ngyvonne/DisplacedDiphotonFramework2/run/runDHAnalysis_2023.05.14_18.16.28-601519/hist-sample.root")

# 601520
tree2=ROOT.TChain("CollectionTree")
tree2.Add("/nfs/dust/atlas/user/ngyvonne/DisplacedDiphotonFramework2/run/promptsamples/ver4/NTUP_LOOSEBAD_ver3_mc16_13TeV.600745.PhPy8EG_AZNLO_VBFH125_mA4p0_Cyy0p01_Czh1p0.deriv.DAOD_STDM4.e8324_s3126_r10201_p4097/hist-sample.root")

for var in binning_dict:
	#hist=ROOT.TH1D("hist", "hist", binning_dict[var][0], binning_dict[var][1], binning_dict[var][2])
	hist2=ROOT.TH1D("hist2", "hist2", binning_dict[var][0], binning_dict[var][1], binning_dict[var][2])
	#tree.Draw("%s>>%s"%(var, "hist"))
	tree2.Draw("%s>>%s"%(var, "hist2"), "m_weight*wt_mc*1000/219015")
	draw_single(hist2, var, "mass=4.0GeV, cTau=38mm", unit="xxx", saveDir="plots_single_ver3")
	#draw_two_histograms(hist, hist2, var, compare=["601519", "601520"], ratio=True, drawLog=True,saveDir="plot_twohistogramALP_compare")

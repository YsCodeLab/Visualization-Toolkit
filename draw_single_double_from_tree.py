import ROOT
from lib.draw_scripts import draw_two_histograms, draw_summary, draw_single
from config.branch_name_binning_non_pointing import binning_dict
import os

# 601519
tree=ROOT.TChain("CollectionTree")
tree.Add("/nfs/dust/atlas/user/ngyvonne/DisplacedDiphotonFramework2/run/runDHAnalysis_2023.05.14_18.16.28-601519/hist-sample.root")

# 601520
tree2=ROOT.TChain("CollectionTree")
tree2.Add("/nfs/dust/atlas/user/ngyvonne/DisplacedDiphotonFramework2/run/runDHAnalysis_2023.05.15_12.35.02-601520/hist-sample.root")

#Originally making this through cutflow
cutflow_1=["(n_el>=2)||(n_mu>=2)", "(el_q[0]*el_q[1]==-1)||(mu_q[0]*mu_q[1]==-1)", "el_pt[0]>27&&mu_pt[0]>27", "el_pt[1]>20||mu_pt[1]>20", "el[]"]
cutflow_2=[""]


weight="(m_weight*wt_vtx*wt_pu*wt_SF)"

cutflow_1=["("+element+")" for element in cutflow_1]
print("cutflow_1: ", cutflow_1)
final_cutflow="&&".join(cutflow_1)
print("final_cutflow: ", final_cutflow)

calculated_weight=weight+"&&"+cutflow_1[0]

for var in binning_dict:
	hist=ROOT.TH1D("hist", "hist", binning_dict[var][0], binning_dict[var][1], binning_dict[var][2])
	hist2=ROOT.TH1D("hist2", "hist2", binning_dict[var][0], binning_dict[var][1], binning_dict[var][2])
	tree.Draw("%s >> %s"%(var, "hist"), "%s"%calculated_weight)
	tree2.Draw("%s >> %s"%(var, "hist2"), "%s"%calculated_weight)

	draw_single(hist, var, "cut0", "601519", unit="xxx", saveDir="plots_single601519_log")

	#draw_two_histograms(hist, hist2, var, compare=["601519", "601520"], ratio=True, drawLog=True,saveDir="plot_twohistogramALP_compare")

for i, event in enumerate(tree):
	#"(n_el>=2)||(n_mu>=2)", 
	#"(el_q[0]*el_q[1]==-1)||(mu_q[0]*mu_q[1]==-1)"
	if ((event.n_el>=2) || (event.n_mu>=2))	

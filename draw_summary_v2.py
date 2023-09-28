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


#weight="(m_weight*wt_vtx*wt_pu*wt_SF)"
weight="(m_weight*wt_vtx*wt_pu*wt_SF)"

import os
import ROOT

from ext_support.plot import RatioCanvas
from util.nice_colors import nice_colors
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

from lib.draw_utilities import createRatio

#TODO Add axis tool
#TODO draw_2d_histogram(hist, name, xname, yname, ratio=False, drawLog=True, doNormalize=False, SaveDir=os.getcwd(), option="LEGO"):
#TODO def draw_sensitivity()
#TODO def draw_stacked()
#TODO def draw_graph()

def draw_single(hist, branch_name, name="", label="", unit="", drawLog=True, doNormalize=False, saveDir=os.getcwd()):

    saveFile=saveDir+"/%s%s_%s.pdf"%(name,branch_name, label)

    if drawLog:
        saveFile=saveFile[:-4]+"_log.pdf"

    if doNormalize:
        try:
            hist.Scale(1/hist.Integral())
            hist.SetMaximum(hist.GetMaximum()*1.5)
        except ZeroDivisionError:
            print("histogram has no events")
        except Exception as e:
            print(e)

    lumi=ROOT.TLatex()
    lumi.SetTextSize(0.05)
    lumi.SetTextFont(42)
    lumi.SetNDC(1)
    hist.SetTitle("%s; %s"%(branch_name, unit))
    hist.SetFillColorAlpha(ROOT.kRed+1, 0.4)
    hist.SetLineColor(ROOT.kBlack)
    hist.SetLineWidth(3)

    legend=ROOT.TLegend(0.25,0.50,0.90,0.70)
    legend.SetTextSize(0.04)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.AddEntry(hist, label,"f")

    c1=ROOT.TCanvas()
    c1.cd()

    if drawLog:
        c1.SetLogy()
        hist.SetMaximum(hist.GetMaximum()*100)
    else:
        hist.SetMaximum(hist.GetMaximum()*1.2)

	hist.GetXaxis().SetLabelOffset(0.1)

    hist.Draw("hist")
    legend.Draw("same")

    lumi.DrawLatex(0.18,0.85,"#bf{#it{ATLAS}} Internal");
    lumi.DrawLatex(0.18,0.79,"#sqrt{s}=13 TeV, MC ~139 fb-1")

    os.system("mkdir -p %s"%(saveDir)) # saveDir defined in beginning of function 

    c1.SaveAs(saveFile) # saveFile defined in beginning of function 


def draw_two_histograms(hist, hist2, branch_name, compare=["hist1", "hist2"], ratio=True, drawLog=True, doNormalize=False, saveDir=os.getcwd()):

    saveFile=saveDir+"/%s_%svs%s.pdf"%(branch_name, compare[0], compare[1])

    if ratio:
        saveFile=saveFile[:-4]+"ratio.pdf"
    if drawLog:
        saveFile=saveFile[:-4]+"_log.pdf"

    if doNormalize:
        try:
            hist.Scale(1/hist.Integral())
            hist2.Scale(1/hist2.Integral())
            hist.SetMaximum(hist.GetMaximum()*1.5)
            hist2.SetMaximum(hist2.GetMaximum()*1.5)
        except ZeroDivisionError:
            print("histogram has no events")
        except Exception as e:
            print(e)

    lumi=ROOT.TLatex()
    lumi.SetTextSize(0.05)
    lumi.SetTextFont(42)
    lumi.SetNDC(1)

    if ratio: 
        print("making ratio plot")
        c_compare=RatioCanvas("%s_%s vs %s"%(branch_name, compare[0], compare[1]))
        c_compare.upper_pad.cd()
        if drawLog:
            c_compare.canvas.SetLogy()
            c_compare.upper_pad.SetLogy()

        hist.SetTitle("%s %s vs %s "%(branch_name, compare[0], compare[1]))
        #hist.SetFillColorAlpha(nice_colors[1], 0.5)
        hist.SetFillColorAlpha(ROOT.kRed+1, 0.4)
        hist.SetLineColor(ROOT.kBlack)
        hist.SetLineWidth(3)

        hist2.SetLineColor(ROOT.kBlack)
        hist2.SetLineWidth(3)
        hist2.SetFillColorAlpha(ROOT.kBlue+1, 0.4)
        hist.GetXaxis().SetLabelOffset(-999)
        hist2.GetXaxis().SetLabelOffset(-999)
        legend=ROOT.TLegend(0.25,0.50,0.90,0.70)
        legend.SetTextSize(0.04)
        legend.SetFillStyle(0)
        legend.SetBorderSize(0)
        legend.AddEntry(hist, compare[0],"f")
        legend.AddEntry(hist2,compare[1],"f")

        if drawLog:
            hist.SetMaximum(hist2.GetMaximum()*100)
        else:
            hist.SetMaximum(hist2.GetMaximum()*1.2)

        hist.Draw("hist")
        print("histogram integral: ", hist.Integral())
        hist2.Draw("hist same")
        print("histogram integral: ", hist.Integral())
        legend.Draw("same")

        lumi.DrawLatex(0.18,0.85,"#bf{#it{ATLAS}} Internal");
        lumi.DrawLatex(0.18,0.79,"#sqrt{s}=13 TeV, MC ~139 fb-1")

        try:
            c_compare.lower_pad.cd()
            c_compare.lower_pad.SetLogy(False)
            ratio=createRatio(hist2, hist, compare[0], compare[1], branch_name)
            ratio.SetMaximum(ratio.GetMaximum()*1.5)
            ratio.SetMinimum(ratio.GetMinimum()*0.5)
            ratio.GetXaxis().SetLabelOffset(0)
            ratio.GetYaxis().SetTitle("hist Red/hist Blue")	
            ratio.Draw("ep")
            #c1=ROOT.TCanvas()
            #ratio.Draw("ep")
            #c1.SaveAs("Ratio_%s_%svs%s.pdf"%(branch_name, compare[0], compare[1]))

        except Exception as e:
            print(e)
            print("ratio histogram making failed.")
            print("%s, %svs %s"%(branch_name, compare[0], compare[1]))

        os.system("mkdir -p %s"%(saveDir)) # saveDir defined in beginning of function 
        c_compare.canvas.SaveAs(saveFile) # saveFile defined in beginning of function 


def draw_summary(hist_list, hist_names, branch_name, drawLog=True, doFill=False, name_tag="", saveRoot=False, saveDir=os.getcwd()):
    #--- Create Lumi Tag
    lumi=ROOT.TLatex()
    lumi.SetTextSize(0.05)
    lumi.SetTextFont(42)
    lumi.SetNDC(1)

	#--- Create Legend
    legend=ROOT.TLegend(0.75,0.60,0.95,0.90)
    legend.SetTextSize(0.04)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    #make_dir(dist_list[0].output_dir, trigger)
    if saveRoot:
		f1= ROOT.TFile("summary_%s.root"%trigger, "recreate")
    c_total=ROOT.TCanvas()
    c_total.cd()
    if drawLog:
		c_total.SetLogy()
    maximum=0
    for i_hist, hist in enumerate(hist_list):
		hist.SetLineWidth(3)

		hist.SetLineColor(nice_colors[i_hist])
		if (doFill):
			hist.SetFillColorAlpha(nice_colors[i_hist], 0.4)
		else:
			hist.SetFillColor(0)

		hist.SetLabelOffset(0.01)
		hist.SetLabelSize(0.03)

		hist.SetTitle("%s"%(branch_name))
		hist.Sumw2()
		if (hist.GetMaximum()>maximum):
			if (drawLog):
				hist_list[0].SetMaximum(hist.GetMaximum()*5)
			else:
				hist_list[0].SetMaximum(hist.GetMaximum()*1.5)
			maximum=hist.GetMaximum()

    for i_hist, hist in enumerate(hist_list):
		if i_hist==0:
			hist.Draw("hist")
		else:
			hist.Draw("hist same")

		if saveRoot:
			hist.Write()

		lumi.DrawLatex(0.18,0.85,"#bf{#it{ATLAS}} Internal");
		lumi.DrawLatex(0.18,0.79,"#sqrt{s}=13 TeV, 36 fb^{-1}")
		legend.AddEntry(hist,hist_names[i_hist],"f")
		legend.Draw("same")

		os.system("mkdir -p %s"%(saveDir))
		c_total.SaveAs("./%s/summary_%s_%s.pdf"%(saveDir, name_tag, branch_name))

    if saveRoot:
		f1.Write()

import ROOT
from units import unit_dict as unit

def createRatio(h1, h2, tag1, tag2, var=""):
    print("h1 integral: ", h1.Integral())
    print("h2 integral: ", h2.Integral())
    h3 = h1.Clone("h1")
    h3.SetLineColor(ROOT.kBlack)
    h3.SetMarkerStyle(21)
    h3.SetMarkerSize(0.7)
    h3.SetTitle("")
    # Set up plot for markers and errors
    h3.Sumw2()
    h3.SetStats(0)
    h3.Divide(h2)

    h3.SetMinimum(h3.GetMinimum())
    h3.SetMaximum(h3.GetMaximum())

    # Adjust y-axis settings
    y = h3.GetYaxis()
    y.SetTitle("%s/%s "%(tag1, tag2))
    y.SetNdivisions(505)
    y.SetTitleSize(10)
    y.SetTitleFont(43)
    y.SetTitleOffset(1.55)
    y.SetLabelFont(43)
    y.SetLabelSize(15)

    # Adjust x-axis settings
    x = h3.GetXaxis()

    try:
        print(unit[var])
    except:
        unit={var:""}

    x.SetTitle("%s %s"%(var, unit[var]))
    x.SetTitleSize(20)
    x.SetTitleFont(43)
    x.SetTitleOffset(4.0)
    x.SetLabelFont(43)
    x.SetLabelSize(15)
    print("h3 integral: ", h3.Integral())
    return h3

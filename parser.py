from typing import List
from xml.dom import minidom
from xml.dom.minidom import Element

def list_of_layers(src_svg:str):
    xmldoc = minidom.parse(src_svg)
    a = xmldoc.getElementsByTagName("svg")[0]
    b = a.getElementsByTagName("g")

    l = []

    for g in b: # type: Element
        if g.getAttribute("inkscape:groupmode") != "layer":
            continue
        curr_label = g.getAttribute("inkscape:label")
        l.append(curr_label)

    return l


def export_visibles (src_svg: str, dst_xvg: str, visibles: List[str]):

    xmldoc = minidom.parse(src_svg)
    a = xmldoc.getElementsByTagName("svg")[0]
    b = a.getElementsByTagName("g")

    for g in b: # type: Element
        if g.getAttribute("inkscape:groupmode") != "layer":
            continue

        oldStyle = g.getAttribute("style")

        curr_label = g.getAttribute("inkscape:label")

        if curr_label in visibles:
            if oldStyle.find("display:") == -1:
                newStyle = oldStyle + " display:inline;"
            else:
                newStyle = oldStyle.replace("display:none;", "display:inline;")
        else:
            if oldStyle.find("display:") == -1:
                newStyle = oldStyle + " display:none;"
            else:
                newStyle = oldStyle.replace("display:inline;", "display:none;")
                newStyle = newStyle.replace("display:block;", "display:none;")

        g.setAttribute("style", newStyle)

    fout = open(dst_xvg, 'w')
    xmldoc.writexml(fout, "", "   ", "\n")
    fout.close()


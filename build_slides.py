import sys
from copy import copy
from typing import List

from os.path import isfile

from parser import export_visibles, list_of_layers


# List of Slide
# Slide : list of visibles layers
def create_slides(layers: List[str]) -> List[List[str]]:
    # _ignore : always hiddens
    # _slide : visible form slide to next slide or next anim
    # _anim : visible from previous _slide to anim

    slides = []
    curr_slide = []
    for l in layers:
        if l.endswith("_slide"):
            if curr_slide:
                slides.append(curr_slide)
            curr_slide = [l]
        elif l.endswith("_anim"):
            if curr_slide:
                slides.append(copy(curr_slide))
            curr_slide.append(l)
        elif l.endswith("_ignore"):
            continue
        else:
            curr_slide.append(l)

    slides.append(curr_slide)
    return slides

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: build_slides.py [file.svg]")
        sys.exit(-1)

    svg_file = sys.argv[1]

    if not isfile(svg_file):
        print("SVG file not found.")
        sys.exit(-1)

    print("Read ", svg_file)

    layers = list_of_layers(svg_file)

    print("Layers found:")
    for l in layers:
        print(" ", l)

    slides = create_slides(layers)

    slide_num = 1
    for s in slides:
        print("Slide", slide_num, " : " , s)
        export_visibles(svg_file, "out/slide" + str(slide_num).zfill(4) + ".svg", s)
        slide_num+=1

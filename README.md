# PrezInk (en)
Presentations with Inkscape.

Create slides using Inkscape layers.

First: name the layers:
blabla_slide to create a slide
blabla_anim to create animation (superimposed on the previous slide)
blabla_ignore to hide a slide
other layers are superimposed on the last slide/anim.

Example of layers (from high to low)
thx_slide
draft_thx_ignore
slide4_slide
juste_a_layer
slide3_slide
fancy_animation_anim
slide2_slide
cover_slide

For this sequence of layers PrezInk will generates a 6-page PDF with 5 slides and 1 animation.
The 6 pages will be:
 - cover_slide : slide 1
 - slide2_slide : slide 2
 - fency_animation_anim + fency_animation_anim : slide 2 (anim)
 - slide3_slide + just_a_layer : slide 3
 - thx_slide : slide 4

Technical part:
Inkscape: Create the layers with the menu Layer -> Layers and Layer -> Add Layer
PrezInk:
  - a Python script, generating several svg files for each slide.
  - A call to Inkscape to generate PDF from svg files
  - Generation of a Latex file to compile all the slides into a PDF (pdflatex)

Advantages:
  - For presentations with a lot of figures Inkscape is a better drawing software than PowerPoint (PP) or LibreOffice (LO)
  - SVG files often need to be exported into heavy (or bad quality) bitmap before being imported into PP or LO: exhausting!
  - Able to use layer to make slides (very useful)
  - Able to use Align and Distribute function of Inkscape (best function ever)
  
Drawbacks:
  - Inkscape is bad for text...
  - PrezInk is not installed in you Linux distrib.
  - Need to "play" with Show/Hide layer to display the slide you need.

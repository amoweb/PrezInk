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
  
  
# PrezInk (fr)
Créer des présentations avec Inkscape.

Les slides sont créés avec les calques (layers) de Inkscape.

Premièrement: nommer les calques:
blabla_slide pour créer une diapo
blabla_anim pour créer une animation (superposée sur la diapo/animation précédente)
blabla_ignore pour que cette diapo ne soit jamais affichée
les autres calques sont superposés sur la diapo/anim précédente.

Exemple of calques (du supérieur à l'inférieur)
merci_slide
broullon_thx_ignore
dispo4_slide
simple_calque_superposé
diapo3_slide
animation_stylée_anim
diapo2_slide
première_slide

Pour cette séquence de calques, PrezInk génère un PDF de 6 pages avec 5 diapos et une animation.
Les 6 pages sont:
 - première_slide : diapo 1
 - diapo2_slide : diapo 2
 - animation_stylée_anim + animation_stylée_anim : diapo 2 (anim)
 - diapo3_slide + simple_calque_superposé : diapo 3
 - merci_slide : diapo 4

Explications techniques:
Inkscape: pour créer des calques : menu Calque -> Calques et Calque -> Ajouter un calque
PrezInk:
  - un script Python éclate le svg en plusieurs : un fichier svg par page.
  - Utilise Inkscape pour générer des PDF depuis les svg.
  - Génère un fichier LaTex pour compiler tous les slides en un seul fichier PDF (pdflatex)

Avantages:
  - Inkscape est meilleur pour créer des dessins que PowerPoint (PP) et LibreOffice (LO)
  - Les images crées sous Inkscape n'ont pas besoin d'être exporté dans des fichier image lourd (ou compressés) comme JPG ou PNG pour les importer dans LO ou PP.
  - Enfin un logiciel de présentation avec des calques (utile !)
  - Pouvoir utiliser la fonction Aligner et Distribuer de Inkscape (meilleur fonction au monde !)
  
Inconvéniants:
  - Inkscape n'est pas très adaptés pour du texte
  - PrezInk n'est pas dans votre distribution Linux.
  - Besoin de changer Afficher/Masquer les calques tout le temps car Inkscape ne comprend pas _anim et _slide.

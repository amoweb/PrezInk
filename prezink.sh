rm out/*

python3.5 build_slides.py presentation.svg

cp template.tex out/prez.tex

for f in $(find -path "./out/*.svg" | sort)
do
        inkscape -f "$f" --export-pdf=out/$(basename "$f" .svg).pdf
        echo "$f.pdf"
        echo "\\includepdf[pages=1]{$(basename "$f" .svg).pdf}" >> out/prez.tex
done

echo "\\end{document}" >> out/prez.tex

cd out/
pdflatex prez.tex

#\includepdf[pages=1]{cid.pdf}

http://tex.stackexchange.com/questions/24663/how-to-place-a-floating-text-box-at-a-specified-location-in-page-coordinates

echo "Working on presentation $1 \n"

SVG_FILE=$1

if [ ! -e "$SVG_FILE" ]
then
        echo "Usage: ./prezink.sh [file.svg]".
        echo "File not found."
        exit
fi

rm out/*

python3.5 build_slides.py "$SVG_FILE"

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


from pypointgroup.gui.tools import GetIconPath
import os.path as pt
import shutil as sh
import os

__GROUPS = (
    r"1,~~ \left( C_1 \right)",
    r"\bar{1},~~ \left(C_i\right)",
    r"2,~~ \left(C_2\right)",
    r"m,~~ \left(C_s \right)",
    r"2/m,~~ \left(C_{2h}\right)",
    r"222,~~ \left(D_2\right)",
    r"mm2,~~ \left(C_{2v}\right)",
    r"mmm,~~ \left(D_{2h}\right)",
    r"4,~~ \left(C_4 \right)",
    r"\bar{4},~~ \left(S_4\right)",
    r"422,~~ \left( D_2 \right)",
    r"4/m,~~ \left( D_{4h} \right)",
    r"4mm,~~ \left( C_{4v} \right)",
    r"\bar{4}2m, ~~ \left( D_{2d} \right)",
    r"\frac{4}{m}mm, ~~ \left( D_{4h}\right)",
    r"3, ~~ \left( C_3\right)",
    r"\bar{3}, ~~ \left( C_{3i}\right)",
    r"32, ~~ \left( D_3 \right)",
    r"3m, ~~ \left( C_{3v} \right)",
    r"\bar{3}m, ~~ \left( D_{3d}\right)",
    r"6, ~~ \left( C_6 \right)",
    r"\bar{6}, ~~ \left( S_{6}, C_{3h} \right)",
    r"\bar{6}m2, ~~ \left( D_{3h} \right)",
    r"622, ~~ \left( D_{6}  \right)",
    r"6/m, ~~ \left( C_{6h} \right)",
    r"6mm, ~~ \left( C_{6v} \right)",
    r"\frac{6}{m}mm, ~~ \left( D_{6h} \right)",
    r"23, ~~ \left( T\right)",
    r"432, ~~ \left( O\right)",
    r"m\bar{3}, ~~ \left( T_h\right)",
    r"\bar{4}3m, ~~ \left( T_d\right)",
    r"m\bar{3}m, ~~ \left( O_h\right)",
)

IM_CMD = 'magick convert -density 300 -quality 90 "{infile}" "{outfile}"'
LATEX_CMD = 'xelatex -output-directory "{dir}" {infile}'
LATEX_DOC = r"""
\documentclass{standalone}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}

\begin{document}
	$ %s $
\end{document}
"""

IMAGE_PATH = GetIconPath()
TMP_DIR = pt.join(IMAGE_PATH, 'tmp')

def convert_formula(formula, fname):

    texfile = pt.join(TMP_DIR, fname+".tex")
    imgfile = pt.join(IMAGE_PATH, fname+".png")
    pdffile = pt.join(TMP_DIR, fname+".pdf")

    with open(texfile,'wt', encoding='utf8') as f:
        f.write(LATEX_DOC % formula)

    os.system(LATEX_CMD.format(dir=TMP_DIR, infile=texfile))

    os.system(IM_CMD.format(infile=pdffile, outfile=imgfile))

    print("Created IMAG: ", imgfile)

def make_group_images():

    if not pt.exists(TMP_DIR):
        os.mkdir(TMP_DIR)

    for i, frm in enumerate(__GROUPS):
        fname = "pg_img_%d" % (i+1)
        convert_formula(frm, fname)

    sh.rmtree(TMP_DIR)

if __name__ == "__main__":
    make_group_images()
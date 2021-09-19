import pandas as pd
import tabula
import sys
import os

argv = sys.argv

if len(argv) < 3:
  sys.exit(1)

pdf_fname = argv[1]
xlsx_fname = os.path.splitext(pdf_fname)[0]+'.xlsx'
pages = argv[2]

dfs = tabula.read_pdf(pdf_fname, lattice=True, pages = pages)
df = pd.concat(dfs)
df.to_excel(xlsx_fname, index=None)


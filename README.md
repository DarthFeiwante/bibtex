# bibtex
This program is intended for building of the bibtex-file for document written in LaTeX.
It will be useful for building of one small *.bib file, with sources specific for certain article,
from large (and sometimes not one) *.bib files of your bibliography database. Builded bibtex file
can be sent to journal editoral board instead of large origin *.bib file

This program uses following modules:

glob

Input files:
\\begin{itemize}
\item Any number of *.tex files
\item Any number of bibliographic files *.bib (Mendeley is useful tool for building of those files)
\end{itemize}

Output - library_new.bib file, containing bibliographic information about sources used in *.tex files that given as input

Program is executable only
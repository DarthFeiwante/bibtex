#!/usr/bin/env python3
'''
\section{bibtex.py}

\\hyperlink{content}{Content}

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

\\newpage

'''

from glob import glob

if __name__ == '__main__':
    # Building of the citation key's list
    list_of_tex_files = glob('*.tex')
    new_list_of_tex_files = []
    for i in list_of_tex_files: 
        new_list_of_tex_files.append(i[:i.index('.tex')])
    print(new_list_of_tex_files)
    citation_list = []
    for i in new_list_of_tex_files:
        exec('list_'+str(i)+'=[]')
        for line in open(i+'.tex'):
            if '\cite{' in line: 
                l = line.split('\cite')
                for ii in l:
                    if ii[0] == '{':
                        iii = ii[1:ii.index("}")].split(',')
                        iii = [e.replace(' ', '') for e in iii]
                        exec('list_'+i+'+= iii')
                        exec('set_list = set(list_'+i+')')
                        exec('list_'+i+' = list(set_list)')
        exec('citation_list += list_'+i)
    exec('set_citation_list = set(citation_list)')
    exec('citation_list = list(set_citation_list)')
    # Creating of new bibtex
    bibtex_file_list = glob('*.bib')
    bibtex_dict ={}
    for ii in bibtex_file_list:
        f = open(ii)
        l = f.readlines()
        bibtex_dict[ii] = l
        f.close()
    bibtex_list = []
    for i in bibtex_dict:
        bibtex_list += bibtex_dict[i]
    new_bibtex_dict = {}
    for i in bibtex_list:
        if '@' in i:
            ii = 0
            while not bibtex_list[bibtex_list.index(i) + ii] == '}\n': 
                ii += 1
            else: 
                l = bibtex_list[bibtex_list.index(i):bibtex_list.index(i) + ii + 1]
                s = ''
                for iii in l:
                    s += iii
                    new_bibtex_dict[i] = s
    new_bibtex_list = []
    for i in new_bibtex_dict:
        new_bibtex_list.append(new_bibtex_dict[i])
    new_bib = open('library_new.bib', 'w')
    final_bibtex_list = []
    for i in citation_list:
        for ii in new_bibtex_list:
            s = ii.split('\n')[0]
            if i == s[s.index('{') + 1:-1]: final_bibtex_list.append(ii)
    set_final_bibtex_list = set(final_bibtex_list)
    final_bibtex_list = sorted(list(set_final_bibtex_list))
    new_bib.writelines(final_bibtex_list)
    new_bib.close()

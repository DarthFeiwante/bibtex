#!/usr/bin/env python3
'''
\section{bibtex.py}

\\hyperlink{content}{Содержание}

Данная программа использует следующие модули:

glob

Данная программа предназначена для создания bibtex-файла для документа, написанного
в LaTeX-редакторе.

На вход подаются следующие файлы:
\\begin{itemize}
\item Любое количество документов в виде tex-файлов (файлов с расширением .tex)
\item Любое количество файлов библиографии системы BibTeX (файлов с расширением .bib)
Данные файлы автоматически генерируются программой Mendeley (хотя могут создаваться и вручную)
\end{itemize}

На выходе получаем файл library\_new.bib, содержащий библиографическую информацию только о тех
источниках, ссылки на которые делались в документе.

Данная программа только исполняемая

\\newpage

'''

from glob import glob

if __name__ == '__main__':
    # Создание списка ключей цитирования
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
    # Создание нового файла bibtex
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

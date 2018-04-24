#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
author : xiaohai
email : xiaohaijin@outlook.com
"""


import subprocess


def main():
    subprocess.call(('make', 'clean'))
    subprocess.call(('xelatex', 'learnPython.tex'))
    subprocess.call(('bibtex',  'learnPython.aux'))
    subprocess.call(('xelatex', 'learnPython.tex'))
    subprocess.call(('xelatex', 'learnPython.tex'))
    subprocess.call(('evince',  'learnPython.pdf'))

if __name__ == '__main__':
    main()

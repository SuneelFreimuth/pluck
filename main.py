from typing import List, Dict
import re
import optparse
from PyPDF2 import PdfFileReader, PdfFileWriter
from collections import DefaultDict

def main():
    with open('test.pdf', 'rb') as inpf, open('out.pdf', 'wb') as outf:
        inp = PdfFileReader(inpf)
        out = PdfFileWriter()

        out.write(outf)

DocSlice = namedtuple('DocSlice', 'doc pages')

pat_doc_index = re.compile(r'({(?P<doc_index>\d+)})')

def parse_page_range(s: str) -> List[DocSlice]:
    '''
    The range specifier syntax yields numbers as follows:
      1 = {0: [1]}
      1-3 = {0: [1, 2, 3]}
      1,3,5 = {0: [1, 3, 5]}
      1-5,7 = {0: [1, 2, 3, 4, 5, 7]}

    For multiple input files, switch to a document using {n}, where n
    is 0-indexed; {0} will be assumed until stated otherwise:
      1,2{1}3,4 = {0: [1, 2], 1: [3, 4]}
    
    Only positive integers are supported.
    '''
    slices = []
    curr_doc = 0
    for segment in pat_doc_index.split(s):
        m = pat_doc_index.match(segment)
        if m:
            curr_doc = int(m.group('doc_index'))
        else:
            pages = []
            for range_ in segment.split(','):
                if '-' in range_:
                    start, end = range_.split('-')
                    pages.extend(range(int(start), int(end)))
                else:
                    pages.append(int(range_))
            slices.append(DocSlice(curr_doc, pages))
    return slices


is_digit = lambda c: ord('0') <= ord(c) and ord(c) <= ord('9')

# class RangeParser:
#     def __init__(self, specifier):
#         self.s = specifier
#         self.i = 0
#         self.documents
# 
#     def parse():
#         while self.i < len(self.s):
#             if self.s[self.i] == '{':
#                 self._scan_number()
#             elif is_digit(self.s[self.i]):
#                 self._scan_number()
#                 if self.s[self.i] == '
# 
#     def _scan_number():
#         start = self.i
#         while self.i < len(self.s) and is_digit(self.s[self.i]):
            
if __name__ == '__main__'
    main()



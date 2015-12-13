__author__ = 'yingying'
__version__ = "$Revision: 1.0$"
__date__ = "$Date: 2015/12$"

# import jason
import re

# # pre-processing the input file ("refs.txt") to transform each reference in one line
# # and output to "proc.txt"
# outfile=open("proc.txt", "w")
# with open("refs.txt", "r") as infile:
#     for line in infile:
#         nn=-1
#         # print(line)
#         line=line.replace("\n", " ")
#         pattern='\[[0-9]+\]'
#         match=re.match(pattern,line)
#         if match:
#             # print(match.group())
#             line="\n"+line
#         outfile.write(line)

# read each reference from "proc.txt"
ref_idx=[]
ref_txt=[]
ref_author=[]
ref_title=[]
ref_journal=[]
ref_year=[]
ref_url=[]
nn=-1
with open("proc.txt", "r") as proc_file:
    for line in proc_file:
        name_pattern='[A-Z]\. [A-Z][a-z]+|[A-Z]\. [A-Z]\. [A-Z][a-z]+|et al\.|etc\.'
        nn=nn+1
        ref_author.append([])
        for match in re.findall(name_pattern, line):
            ref_author[nn].append(match)
            # print(match)

    # print(ref_idx)
    # print(ref_txt)
    print(ref_author)

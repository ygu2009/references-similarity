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
        ref_flag=0 #detect the correct format refrence for later process
        ref_idx=[]
        pattern_idx=re.compile('\[[0-9]*\]')
        match_idx = re.search(pattern_idx,line)
        pattern_author=re.compile('\s[A-Z]\. [A-Z][a-z]+|\s[A-Z] [A-Z][a-z]+|\s[A-Z]\. [A-Z]\. [A-Z][a-z]+|\set al\.|\setc\.')
        match_author = re.search(pattern_author, line)
        if match_idx and match_author:
            ref_flag=1
        # print line
        if ref_flag==1:
            nn=nn+1
            ref_author.append([])
            for match in pattern_author.finditer(line):
                ref_author[nn].append(match.group().strip(' '))
                pos_end=match.end()
            # print ref_author[nn]
            # print pos_end

            pattern_title=re.compile('\\"(.+)\\"') #assuming that the title is in ""
            for match in pattern_title.findall(line):
                print match
            # print(pattern_title[1])



    # print(ref_idx)
    # print(ref_txt)
    # print(ref_author[0])

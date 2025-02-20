import re

designs = "r, wr, b, g, bwu, rb, gb, br".split(", ")

towels="""brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".splitlines()

from day19_input import designs, towels

def segment_possible(towel_segment,depth=0):
  """Return true if segment can be made from designs"""
  if towel_segment in designs:
    return True
  for x in range(1,len(towel_segment)):
    if segment_possible(towel_segment[:-x],depth+1) and segment_possible(towel_segment[-x:],depth+1):
      return True
  return False

towel=towels[0]
#print(towel)
result={design:[m.start() for m in re.finditer(f'(?={design})', towel)] for design in designs}
#print(result)

#print(result)

#for towel in [towels[0]]:
  #print(f"Towel: {towel} - Possible: {segment_possible(towel)}")
#print(sum(segment_possible(towel) for towel in towels))
from collections import defaultdict
towel_dict=defaultdict(list)
max_len=max(len(design) for design in designs)
print(max_len)
def segment_check(towel_segment):
  print(f'Checking {towel_segment}')
  for i in range(len(towel_segment)):
    for j in range(max_len+1,0,-1):
      if towel_segment[i:i+j] in designs:
        towel_dict[i].append(j)

segment_check(towels[0])
print(towel_dict)
pointer=0

def possible(pointer,target):
  for step in towel_dict[pointer]:
    if pointer+step==target:
      return True
    if not towel_dict[pointer+step]:
      continue
    return possible(pointer+step,target)
        
  return False

print(possible(0,len(towels[0])))
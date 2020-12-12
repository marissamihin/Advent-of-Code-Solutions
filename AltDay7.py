with open('day7input.txt') as f:
    lines = [line.rstrip() for line in f]

bags=0
check=["shiny gold"]
checked=[]

while(check):
  #print check[0]
  for line in lines:
    endloc = line.find("contain")
    if check[0] in line[endloc:]:
      bags+=1
      #print endloc
      container=line[:endloc-1]
      if container[-1:] == "s":
        container = container[:-1]


      if container not in checked:
        check.append(container)
        checked.append(container)
      #print line[endloc:]
      #print check[0]
      #print line[:endloc-1]
  #print bags
  check.pop(0)
  #print check

print(len(checked))

#print checked
print (bags)
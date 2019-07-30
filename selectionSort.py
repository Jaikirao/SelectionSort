#here we do a programe of Selection sort algorithm
def selectionSort(l):
  for start in range (len(l)+1):
    minpos=start
    for i in range(start,len(l)):
      if l[i]<l[minpos]:
        minpos=i
        (l[start],l[minpos])=(l[minpos],l[start]
l=[4,6,3,1,8]
selectionSort(l)
l
output:- [1, 3, 4, 6, 8]
l=list(range(100,1,-1))
selectionSort(l)
l
output :- 
[1,2,3,4,5,6,7,............99,100]

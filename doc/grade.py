'''
n = int(input())
b = list()
for i in range(n):
  b.append(int(input()))
'''

n = 4
b = [60,75,87,88]
cnum,dnum = 0,0
for j in range(n):
  if b[j]>=60:
    cnum += 1
    print('60-'+str(j))
    print(cnum)

  if b[j]>=85:
    dnum += 1
    print('85-'+str(j))
    print(dnum)

jige = int(100*(cnum/n)+0.5)
youxiu = int(100*(dnum/n)+0.5)
print('{}%'.format(jige))
print('{}%'.format(youxiu))

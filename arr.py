import subprocess

arr0 = ["%x[0,0]","%x[-1,0]","%x[1,0]","%x[-2,0]","%x[2,0]","%x[-3,0]","%x[3,0]","%x[-1,0]/%x[0,0]","%x[0,0]/%x[1,0]"]
arr1 = ["%x[0,1]","%x[-1,1]","%x[1,1]","%x[-2,1]","%x[2,1]","%x[-3,1]","%x[3,1]","%x[-1,1]/%x[0,1]","%x[0,1]/%x[1,1]"]
arr2 = ["%x[0,2]","%x[-1,2]","%x[1,2]","%x[-2,2]","%x[2,2]","%x[-3,2]","%x[3,2]","%x[-1,2]/%x[0,2]","%x[0,2]/%x[1,2]"]
arr3 = ["%x[0,3]","%x[-1,3]","%x[1,3]","%x[-2,3]","%x[2,3]","%x[-3,3]","%x[3,3]","%x[-1,3]/%x[0,3]","%x[0,3]/%x[1,3]"]
arr4 = ["%x[0,2]/%x[0,3]","%x[0,3]/%x[0,2]","%x[0,1]/%x[0,3]/%x[0,2]"]
arr5 = ["%x[-1,2]/%x[-1,3]","%x[-1,3]/%x[-1,2]","%x[-1,1]/%x[-1,3]/%x[-1,2]"]
arr6 = ["%x[1,2]/%x[1,3]","%x[1,3]/%x[1,2]","%x[1,1]/%x[1,3]/%x[1,2]"]

def crf(cnt):
  print str(cnt) + '\n'
  tmp = 'tmp'+str(cnt)
  feat = 'feat'+str(cnt)
  feats = 'feats'+str(cnt)
  evln = 'eval'+str(cnt)
  template = open(tmp,'a')
  template.write('\nB')
  template.close() 
  aa = subprocess.Popen("crf_learn "+tmp+" "+feat+" model", shell=True)
  aa.wait()
  ab = subprocess.Popen("crf_test -m model "+feats+" >out", shell=True)
  ab.wait()
  u = subprocess.Popen("perl conlleval.pl -d \"\\t\" <out", stdout=subprocess.PIPE, shell=True)
  uu = u.communicate()[0]
  uuu = uu.split('\n')
  dt = uuu[1].split()
  evaln = open(evln,'a')
  evaln.write(str(i)+'-'+str(cnt)+'\t'+ dt[1]+'\t'+dt[3]+'\t'+dt[5]+'\t'+dt[7]+"\n\n")
  evaln.close()
  ad = subprocess.Popen("rm model", shell=True)
  ad.wait()
  ad = subprocess.Popen("rm out", shell=True)
  ad.wait()
  rem_line(tmp)


def rem_line(templ):
  readFile = open(templ)
  lines = readFile.readlines()
  lines = lines[:-2]
  readFile.close()
  w = open(templ,'w')
  w.writelines([item for item in lines])
  w.close()

def write_tmp(val,cnt):
  i=0
  tmp = 'tmp'+str(cnt)
  vals = val.split('--')
  template = open(tmp,'w') 
  for j in vals: 
   template = open(tmp,'a') 
   if(i==0):
    template.write('\n')
   if(len(j)>5):
    if vals.index(j)<10:
     if('*' in j):
      template.write('\nU0'+str(i)+':'+j[1:]+'\n')
     else:
      template.write('U0'+str(i)+':'+j+'\n')
    else:
     if('*' in j):
      template.write('\nU'+str(i)+':'+j[1:]+'\n')
     else:
      template.write('U'+str(i)+':'+j+'\n')
   i=i+1
   template.close()
  #crf(cnt)
  

c=d=e=f=g = ''
eval0 = open('eval0','w')
eval1 = open('eval1','w')
eval2 = open('eval2','w')
eval3 = open('eval3','w')
i=0
for a in range(0,9):
 print a
 for b in range(0,5):
  if(b==0):
   c=c+arr0[a]+'--'
   write_tmp(c+'*',b)
  elif(b==1):
   d=d+arr1[a]+'--'
   write_tmp(c+'*'+d+'*',b)
  elif(b==2):
   e=e+arr2[a]+'--'
   write_tmp(c+'*'+d+'*'+e+'*',b)
  elif(b==3):
   f=f+arr3[a]+'--'
   write_tmp(c+'*'+d+'*'+e+'*'+f+'*',b)

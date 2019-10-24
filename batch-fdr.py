import sys
import numpy as np
r=open('result','w')
with open ('out1') as infile:
    li=[]
    file=infile.readlines()
    i=0
    while i < len(file):
        if file[i][0]!='I':
            line=file[i].strip().split('\t')
            li.append(line)
        elif file[i][0]=='I' and li:
            zu=np.array(li)
            zu=zu[np.argsort(zu[:,3])]
            print(zu)
            li1=[]
            for k in range(len(zu)):
                fdr=float(zu[k,3])*len(zu)/(k+1)
                li1.append(fdr)
            j=len(li1)-1
            while j:
                if li1[j-1]>li1[j]:
                    li1[j-1]=li1[j]
                j=j-1
            li1=np.array(li1)
            li=np.c_[zu,li1]
            r.write("ID1"+"\t"+"ID2"+"\t"+"pearsonr"+"\t"+"pvalue"+"\t"+"fdr"+"\n")
            for l in range(len(li)):
                r.write('\t'.join(li[l])+"\n")
            li=[]
        i+=1
r.close()
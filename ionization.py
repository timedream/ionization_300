#!/usr/bin/env python3
#from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np
import matplotlib.pyplot as pl
import math
import os


def main():
    path=os.getcwd()
    file_name=os.listdir(path)
    data_name=[name for name in file_name if name.find('.txt')!= -1]
    for name in data_name:
        print name
        data=np.loadtxt(name)
        Qh=0
        ritio=25.4
        Rsun=6.957e10
        c=3.0e18
        k=0
        m=1
        h=4.136e-15
        #number=data[0,3]
        #print number

        #while( k < 2725):
       #data[k,0]=c/data[k,0]
       #print data[k,0]
       #k=k+1
        while(data[m,0] < 912):
          #print data[m,0] 
            m1=m+1
            Qh=Qh+data[m,1]/(h*c/data[m,0])*(data[m1,0]-data[m,0])*6.2415e11
            m=m+1
          # print Qh
        ro=22  
        #ro = data[0,2]
        print Qh
        Q = Qh*(ro**2*Rsun*Rsun*4*3.1415)
        print Q
        fig_name=name.replace('.txt','.jpg')
        fig_title=name.replace('.txt','')
        par_file=open('ionization.txt','a')
        par_file.write(str(name)   +'  '+  str(Qh)+'\n')
        par_file.close()
        pl.figure(figsize=(8, 6))
        pl.plot(data[:,0], np.log10(data[:,1]))
        pl.xlim(0,10000)
        
        pl.xlabel("X/A")
        pl.ylabel("Y/log(fv/erg*s^(-1)*cm^(-2)*A^(-1))")
        pl.title(fig_title)
        pl.savefig(fig_name)



    


if __name__ == '__main__':
    main()

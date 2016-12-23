import numpy as np
import matplotlib.pyplot as pl
def main():
   data=np.loadtxt('ionization_euv.txt')
   pl.figure(figsize=(8, 6))
   pl.plot(data[:,0],np.log10(data[:,1]),'.')
   pl.xlabel("deg")
   pl.ylabel("log(/s)")
   pl.title("ionization luminosity rate")
   pl.savefig("ionization rate.jpg")
def per():
    data=np.loadtxt('ionization_euv.txt')
    pl.figure(figsize=(8, 6))
    pl.plot(data[:,0],np.log10(data[:,2]),'.')
    pl.xlabel("deg")
    pl.ylabel("log(/s/cm^2)")
    pl.title("ionization luminosity rate per square centimetre")
    pl.savefig("ionization rate per.jpg")
if __name__ == '__main__':
    main()
    per()
  

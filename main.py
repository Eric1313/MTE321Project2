from pprint import pprint
import math

class Gear:
    def __init__(self,N,P):
        self.N=N
        self.P=P
        self.d=N/P
        self.F=10/P
        self.Ko=1 
		self.Qv=6 # anything from 1-9 
		self.B=pow(0.25*(12-self.Qv), 2/3) 
		self.A=50+56*(1-self.B)
		self.Kv=pow(((self.A+sqrt(self.V))/self.A),self.B) 
		self.YX=[12,13,14,15,16,17,18,19,20,21,22,24,26,28,30,34,38,43,50,60,75,100,150,300,400]
		self.YY=[0.245,0.261,0.277,0.29,0.296,0.303,0.309,0.314,0.322,0.328,0.331,0.337,0.346,0.353,0.359,0.371,0.384,0.397,0.409,0.422,0.435,0.447,0.46,0.472,0.48]
		self.Y=scipy.interpolate.interp1d(self.YX,self.YY,self.N)
		self.Ks=





class Gear_Mesh:
    def __init__(self, G1, G2):
        self.G1=G1
        self.G2=G2




P12=16
P34=16

G1 = Gear(20,P12)
G2 = Gear(110,P12)
G3 = Gear(20,P34)
G4 = Gear(80,P34)

#https://engines.honda.com/models/model-detail/gx100#PerformanceCurves


G1.w=3600
G2.w=(-1*G1.w*G1.N/G2.N)
G3.w=G2.w
G4.w=(-1*G3.w*G3.N/G4.N)
print("Output speed: "+str(G4.w)+" rpm")

w_max=500/math.pi*1.05;
w_min=500/math.pi*0.95;

if(G4.w<w_max and G4.w>w_min):
    print("Output Speed OK")

r_wheel=3.93701;
ground_clearance=min(r_wheel-(G4.d)/2-1/G1.P,r_wheel-(G2.d)/2+(G3.d+G4.d)/2-1/G3.P)
print("Ground Clearance "+str(ground_clearance)+" in")

T1=4.1*12 #in-lbs
G1.WT=2*T1/G1.d
G2.WT=-1*G1.WT

M12=Gear_Mesh(G1, G2)





Ks34=0.4867+0.2132/P34






print()
pprint(vars(G1))
pprint(vars(G2))
pprint(vars(G3))
pprint(vars(G4))
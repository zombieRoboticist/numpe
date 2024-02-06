"""Module for plotting hw08"""
import numpy as np;
from hw08 import dirac, normal, uniform, displacement, time_to_land, acceleration_from_spin, impact_position ;
import matplotlib.pyplot as plt;

class Serve(object):
	"""class for defining a serve"""

	znet = 42;
	rball = 1.3;
	def __init__(self):

		self.c=np.array([normal(15,4.2,6,22),-6.0,0]);
		self.d=np.array([np.random.normal(.5,3.2),np.random.normal(6.0,2.2),np.random.normal(98.0,.5)]);
		self.p=self.c+self.d;

		self.rpm=normal(1500,60,1200,1600);
		q= np.array([np.random.normal(-.65,.01),np.random.normal(-.25,.01),np.random.normal(.35,0.01)])
		#print("u",u)
		self.q = q/np.linalg.norm(q)

		u= np.array([np.random.normal(-.012,.01),np.random.normal(.95,.012),np.random.normal(-.04,.0125)]);
		self.v = np.random.normal(130,5.4)*17.6;
		self.u=self.v*u/np.linalg.norm(u);

		self.adrag = np.array([0,((-6.E-4)*(self.v**2)),0]);
		self.agrav= np.array([0,0,-386.088583]);
		self.aspin=  acceleration_from_spin(self.q, self.u, self.rpm);
		self.a=self.adrag+self.agrav+self.aspin;
		#print("a", self.a);
		return None;

	def overNet(self):
		"""Determines if the ball makes it over the net

		Inputs: None
		Output: a boolean that states if the ball went over the net"""
		if( impact_position(self.p, self.u, self.a, self.q, self.rpm, (self.znet+self.rball))[1]>= (39*12-self.p[1])):
			return True;
		return False;

	def inBox(self,xmin,xmax,ymin,ymax):
		"""determines if the ball lands in the box

		Input: scalars xmin, xmax, ymin, ymax: the x and y minimum and maximum values for the position of the box
		Output: a bolean value of if the ball landed in the box"""
		temp= impact_position(self.p, self.u, self.a, self.q, self.rpm,self.rball);
		# print(temp);
		# if(temp[0]<xmin or temp[0]>xmax or temp[1]>ymax or temp[1]<ymin):
		if(temp[0]>xmax):
			return False;
		return True;

	def overLine(self, y):
		"""determines if the ball goes over the serve line

		Inputs: y the location of the serve line
		output: a boolean value of if the ball went over the serve line"""
		if ( impact_position(self.p, self.u, self.a, self.q, self.rpm,self.rball)[1] >y):
			return True;
		return False;

	def landTime(self):
		"""returns the time the ball lands at

		Inputs: none
		output: the time the ball takes to land (s)"""
		#print("time", time_to_land(self.rball,self.u[2],self.a[2]));
		return  time_to_land((self.p[2]-self.rball),abs(self.u[2]),abs(self.a[2]));

	def position(self, t):
		"""computes the position of the ball at time t

		inputs: t the time in seconds after initial conditions
		outputs: a 1d 3 len numpy array describing the position of the ball at time t"""
		return  displacement(self.u,self.a,t)+self.p;




n=10000;
fails=np.zeros(3);
serves = np.empty((n), dtype='object');
serveIn=0;
haveServeIn=False;
servePositions = np.zeros((2,n));
for i in range (n):
	serves[i] = Serve();
	servePositions[0][i]=serves[i].position(serves[i].landTime())[0];
	servePositions[1][i]=serves[i].position(serves[i].landTime())[1];
	# print(serves[i].position(serves[i].landTime())[2])
	if  not serves[i].overNet():
		fails[1]+=1;
		# continue;
	elif  serves[i].overLine(720):
		fails[2]+=1;
		# continue;
	elif not serves[i].inBox(-24.0,0.0,660.0,720.0):
		fails[0]+=1;
		# continue;
	elif not haveServeIn:
		haveServeIn=True;
		serveIn=i;
		# continue;
t = np.linspace(0,serves[serveIn].landTime(), 1000);
pos = np.zeros((2,1000));
for i in range(1000):
	temp = serves[serveIn].position(t[i]);
	pos[0][i] = temp[0];
	pos[1][i] = temp [1];

Make_Plot = True
if (Make_Plot):
	plt.figure(1, figsize=(5.5, 8));
	cx,  cy = np.loadtxt("court.dat",  delimiter=' ', unpack=True);
	bx,  by = np.loadtxt("bbox.dat",  delimiter=' ', unpack=True);
	plt.plot(servePositions[0],servePositions[1],"ro", label = "Simulated Landings",markersize = 0.25);
	plt.plot(cx,cy, color = "blue",linewidth = 3);
	plt.plot(bx,by,color="purple", label="Target",linewidth=4);
	#print(pos[1]);
	# print(servePositions[1]);
	plt.plot(pos[0],pos[1],color="yellow", linewidth=3,label="Nominal Trajectory");
	plt.legend(loc=[0.025,0.05]);
	text="Success Percentage =" + str(100*(n-fails.sum())/n)+"\n" + "Total Fails =" + str(fails.sum())+"\n" + "Fails Service Box =" + str(fails[0])+"\n" + "Fails Service Line =" + str(fails[2]);
	plt.text(-150.,800.,text,fontsize=8);
	plt.title("Serve statistics (hamiln)");
	plt.xlabel('x [inches]');
	plt.ylabel('y [inches]');
	plt.show();



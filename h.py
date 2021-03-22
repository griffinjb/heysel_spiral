import matplotlib.pyplot as plt  
import numpy as np

SAMPLERATE = 1000
SUBCANVAS = 100
NSUB = 25 # square natural

def heysel_gen():

	fs = [f for f in np.linspace(1,SAMPLERATE,NSUB)]

	dg = sin_gen(100)

	for img in consolidator([f_spiral_gen(f,dg) for f in fs]):
		plt.imshow(img)
		plt.show(block=False)
		plt.pause(.001)
		plt.cla()


def consolidator(gs):
	while 1:
		canvas = np.zeros([int(np.sqrt(len(gs)))*SUBCANVAS,int(np.sqrt(len(gs)))*SUBCANVAS])
		i = 0
		for g in gs:

			x = i%np.sqrt(NSUB)
			y = np.floor(i/np.sqrt(NSUB))

			canvas[int(x*SUBCANVAS):int((x+1)*SUBCANVAS),
					int(y*SUBCANVAS):int((y+1)*SUBCANVAS)] = g.__next__()
			i += 1
		yield(canvas)


def f_spiral_gen(f,dg):
	phase = 0
	dp = f*2*np.pi/SAMPLERATE
	canvas = np.zeros([SUBCANVAS,SUBCANVAS])
	for d in dg:
		phase += dp

		re = d*np.cos(phase)
		im = -d*np.sin(phase)

		re = np.floor(re*SUBCANVAS/2*.9)
		im = np.floor(im*SUBCANVAS/2*.9)

		canvas[int(re+SUBCANVAS/2),int(im+SUBCANVAS/2)] = 1

		yield(canvas)

def sin_gen(f):
	while 1:
		for t in range(SAMPLERATE):
			yield(np.sin(t/SAMPLERATE*2*np.pi))


if __name__ == '__main__':
	heysel_gen()

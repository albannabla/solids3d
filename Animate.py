from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os

def make_gif(ax,output):
	images = []

	for ii in range(0,360,20):
		ax.view_init(elev=10., azim=ii)
		plt.savefig(str(ii)+".png")

	for ii in range(0,360,20):
		im = Image.open(str(ii)+".png")
		images.append(im)

	images[0].save(output+'.gif',save_all=True, append_images=images[1:], optimize=False, duration=200, loop=0)
	cwd = os.getcwd()
	for file in os.listdir(cwd):
		if file.endswith('.png'):
			os.remove(file) 

	return



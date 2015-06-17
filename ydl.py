#GUI frontend for youtube-dl
#http://github.com/abh15/ydl-gui


import subprocess
from Tkinter import *
root = Tk()
root.title('youtube-dl-gui')
code=[]
res=[]
fmt=[]
resfmt=[]


def SelectResCallback(number):
	cmd="youtube-dl -t -f"+code[number-2]+" "+url.get() #download desired format
	p=subprocess.Popen(cmd.split(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	print cmd
	print p.stdout.readline()	
def Gocallback():
	i=2
	colvar=8  #positioning variables
	rowvar=2
	command="youtube-dl -F "+url.get()  #gets list of formats    # https://www.youtube.com/watch?v=xgakdcEzVwg"
	p=subprocess.Popen(command.split(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	

	for j in xrange(1,6):
		line=p.stdout.readline() #skip first five lines


	while True:
		line=p.stdout.readline()
		if line=='' and p.poll()!=None:  #check for for empty lines
			break
		code.append(line.split()[0])  #get availble fmt codes
		fmt.append(line.split()[1])   #get available formats
		res.append(line.split()[2])   #get available resolutions
	
	for k in xrange(0,len(res)):
		resfmt.append(res[k]+" "+fmt[k])  #merge format & res together for btn text
	for r in resfmt:
		if i%9==0:     #for arranging btns fitting screen,should be more optimal/efficient
			colvar+=1
			rowvar=2
		x=Button(root, text=r,command=lambda x=i:SelectResCallback(x)).grid(row=rowvar, column=colvar, sticky='ew', padx=2,pady=2)
		#create dynamic buttons acc. to avilable resolutions
		i+=1
		rowvar+=1


url=StringVar() # for reading url from input box
Label(root,text="URL:").grid(row=0, column=0, sticky='e')
e=Entry(root,textvariable=url).grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=9)
Button(root, text="Go",command=Gocallback).grid(row=0, column=10, sticky='e', padx=2,pady=2)


root.mainloop()



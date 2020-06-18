from tkinter import *
from tkinter import ttk
import csv
import os

colour1 = '#8cc8e9'
colour2 = '#b2daf0'

window = Tk()
window.resizable(0, 0)
window.configure(bg=colour1)

cablePrefixes = []
perCable = []
startingNo = []
exportCable = []
intervalCount = []
storedArg = " "
fileName = " "

window.title("Cable Labelling App")
window.geometry('400x320')


titleLabel = Label(window, text="Cable Labelling App (.csv writer)", bg=colour1, font=20).grid(column=1, row=0, columnspan=3,
																				 sticky=N + S + E + W)
infoLabel2 = Label(window, text="Written by Max Ellery", bg=colour1).grid(column=1, row=1, columnspan=2)
infoLabel = Label(window, text="For use by Powersystems UK", bg=colour1).grid(column=1, row=2, columnspan=2,
																			  sticky=N + S + E + W)


infoLabel3 = Text(window, height=15, width=25)
infoLabel3.grid(column=3, row=1, rowspan=8)
infoLabel3.insert(END, "How to use the Cable\nLabeler:"
					   "\n1. Set label format."
					   "\n2. Enter:"
					   "\n-Project Name"
					   "\n-Cable Prefix"
					   "\n-No. of first cable"
					   "\n-Last cable no."
					   "\n-Spacing between no.'s"
					   "\n3. Press Next to move on"
					   "\nto next prefixed cable"
					   "\n4. Write to .csv")


infoLabel3.config(state=DISABLED, bg=colour1)

projectNameLabel = Label(window, text="Project Name", bg=colour2).grid(column=1, row=4, sticky=N+S+E+W)
projectNameEntry = Entry(window, width=18, justify=CENTER)
projectNameEntry.grid(column=2, row=4)

prefixLabel = Label(window, text="Cable Prefix", bg=colour2).grid(column=1, row=5, sticky=N+S+E+W)
prefixEntry = Entry(window, width=18, justify=CENTER)
prefixEntry.grid(column=2, row=5)

startingNoLabel = Label(window, text="Starting Number", bg=colour2).grid(column=1, row=6, sticky=N+S+E+W)
startingNoEntry = Entry(window, width=18, justify=CENTER)
startingNoEntry.grid(column=2, row=6)

endNoLabel = Label(window, text="Ending Number", bg=colour2).grid(column=1, row=7, sticky=N+S+E+W)
endNoEntry = Entry(window, width=18, justify=CENTER)
endNoEntry.grid(column=2, row=7)

intervalLabel = Label(window, text="Interval? (Default 1)", bg=colour2).grid(column=1, row=8, sticky=N+S+E+W)
intervalEntry = Entry(window, width=18, justify=CENTER)
intervalEntry.grid(column=2, row=8)

formatLabel = Label(window, text="Label Format", bg=colour2).grid(column=1, row=3, sticky=N+S+E+W)
formatType = ttk.Combobox(window, values=["Cable Reference", "Ferrules"], width=15)
formatType.grid(column=2, row=3)


def nextaction():
	global storedArg, intervalCount

	cablePrefixes.append(prefixEntry.get())
	prefixEntry.delete(0, END)
	
	startingNo.append(int(startingNoEntry.get()))
	startingNoEntry.delete(0, END)
	
	perCable.append(int(endNoEntry.get()))
	endNoEntry.delete(0, END)

	intervalCount.append(intervalEntry.get())
	endNoEntry.delete(0, END)
	
	if formatType.get() == "Cable Reference":
		storedArg = "-cableref"
	elif formatType.get() == "Ferrules":
		storedArg = "-ferrule"


def writetocsv():
	global storedArg, projectName, fileName
	projectName = projectNameEntry.get()
	fileName = projectName + '.csv'

	if storedArg == '-ferrule':
		i = 0
		for i in range(len(cablePrefixes)):
			for j in range(startingNo[i], perCable[i] + 1, int(intervalCount[i])):
				row = list()
				row.append(cablePrefixes[i] + str(j))
				row.append(cablePrefixes[i] + str(j))
				exportCable.append(row)

	if storedArg == '-cableref':
		i = 0
		for i in range(len(cablePrefixes)):
			for j in range(startingNo[i], perCable[i] + 1, int(intervalCount[i])):
				exportCable.append([cablePrefixes[i] + str(j)])
				exportCable.append([cablePrefixes[i] + str(j)])

	# uses csv library to write to .csv
	with open(fileName, 'w+', newline='') as myFile:
		writer = csv.writer(myFile, delimiter=',')
		writer.writerow(['BLANK'])
		writer.writerow([projectName])
		writer.writerows(exportCable)


def reset():
	python = sys.executable
	os.execl(python, python, *sys.argv)


nextButton = Button(window, text="Insert/Next", command=nextaction, bg="#f6b360").grid(column=2, row=9, sticky=N+S+E+W)
finishButton = Button(window, text="Write to .csv", command=writetocsv, bg="#f6b360").grid(column=3, row=9)
resetButton = Button(window, text="Reset", bg="#f6b360", width=10, command=lambda: reset()).grid(column=3, row=10)

window.mainloop()


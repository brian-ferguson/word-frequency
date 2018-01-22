#python3
import operator
import csv
#get input from user to determine read file
filename = input('Enter Filename: ')
#get input from user to determine csv save file
savename = input('Enter Save Filename:')
#if the user inputs nothing (TODO: if the users input does not end .txt)
if len(filename) < 1 : filename = 'read-me.txt'
handle = open(filename)
di = dict()
for line in handle:
	#.strip removes starting and ending white space, rstrip only ending, lstrip only starting
	line = line.rstrip()
	#split the into the words
	wds = line.split()
	
	for w in wds:
		for c in w:
			for ch in ['.',',','>','<','[',']','=','$','(',')','"','+',':','/']:
				if ch in w:
					w = w.replace(ch,'')
					
		#idiom retrieve/create/update key value pair (key=word,value=occurences)
		if w:
			di[w] = di.get(w,0) + 1
	
		#alt to idiom #1 (-99 = key not in dict, +1 = key exists in dict)
		#print('**',w,di.get(w,-99))
		##word has occured
		#if w in di:
		#	di[w] = di[w] + 1
		##word has not occured
		#else:
		#	di[w] = 1
		#print(w, di[w])
		
		##alt to idiom #2
		##(0 = key not in dict, +1 = key exists in dict)
		#oldcount = di.get(w,0)
		#print(w,'old',oldcount)
		#newcount = oldcount + 1
		#di[w] = newcount
		#print(w,'new', newcount)
	
	##convert the dictionary to a list and sort
	sorteddi = sorted(di.items(), key=operator.itemgetter(1))

#create the output csv file
with open(savename+'.csv', 'w', newline='') as outfile:
	for k in sorteddi:
		writer = csv.writer(outfile)
		writer.writerow(k)
	
##print the sorted list
for k,v in sorteddi:
	print(v,k)
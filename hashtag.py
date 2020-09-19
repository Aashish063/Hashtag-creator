loc=input('Enter file location: ')
#root dir where this script is located
fb=open(loc, 'r+')
fdata=fb.read()
f_list=fdata.split()
with open('hash#tag.txt' , 'a+') as hf:
	for i in range(0,len(f_list)):
		while f_list[i]:
				hf.write( '#' + f_list[i] + ' ')
				break
	print('Done ,File is created ')
	print('Go to Root dir. where script is located to view this gen. hashtag file ')
	
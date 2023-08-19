def find_first(my_list,pat,index):
	size=len(my_list)
	if size == 1 :
		return my_list,index
	else:
		if size % 2 == 0:
			s1=size//2
		else :
			if size== 3:
				s1=1
			else:
				s1=size//2 
		left_array = my_list[0:s1]
		left_array,index= find_first(left_array,pat,index)
		right_array = my_list[size//2:]
		right_array,index = find_first(right_array,pat,index)
		sort_array=[]
	while (len(left_array) != 0  and len(right_array) != 0):
		if pat[index] == 'L':
			sort_array.append(left_array[0])
			index = index + 1
			left_array=left_array[1:]
		else:
			sort_array.append(right_array[0])
			index = index + 1
			right_array=right_array[1:]
	left_array.extend(right_array)
	sort_array.extend(left_array)
	return sort_array,index


number = int(input())
pattern = list(input())
list1 = [ str(i) for i in range(1,number+1)]
mat1,mat2=find_first(list1,pattern,0)
k=1
x=[]
dict1={}
for i in mat1:
 	dict1[i] = str(k)
 	k = k + 1
 
for  j in range(1,number+1):
 	x.append(dict1.get(str(j)))

print(" ".join(x))
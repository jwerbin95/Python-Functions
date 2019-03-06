import re
def sum_to(n):
	if n==1:
		return n
	else:
		return n+sum_to(n-1)

def largest(list):
	list.sort(reverse=True)
	return list[0]

def occurances(stn, match):
	return len(re.findall(f"{match}", stn))

def product(*nums):
	if(len(nums)==1):
		return nums[0]
	else:
		return nums[len(nums)-1] * product(*list(nums)[:-1])

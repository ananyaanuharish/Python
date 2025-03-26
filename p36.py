# default arguments as mutable objects
def func(nums,numericlist=[]):
    numericlist.append(nums-1) # (nums+1) can also be used
    print(numericlist)

func(66)
func(34)
func(19)
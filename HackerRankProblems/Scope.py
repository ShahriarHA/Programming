class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
	# Add your code here
    # global maximumDifference
    
    
    def computeDifference(self):
        maxValue = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                maxValue = abs(self.__elements[i] - self.__elements[j])
                if maxValue > self.maximumDifference: self.maximumDifference = maxValue
        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
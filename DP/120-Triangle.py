# 三角形的最小路径和

class Solution(self,triangle):
	if not triangle:return 0

	res = triangle[-1]
	for i in xrange(len(triangle) -2 ,-1,-1):
		for j in xrange(len(triangle[i])):
			res[j] = min(res[j],res[j+1] + triangle[i][j])

	return res[0]
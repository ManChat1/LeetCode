class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse = True)
        val = 0
        length = len(happiness) - 1
        for i in range(k) :
            if happiness[i] - i > 0:
                val += happiness[i] - i
        return val
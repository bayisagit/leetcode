class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mins=float('inf')
        result=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    indexsum=i+j
                    if indexsum<mins:
                        mins=indexsum
                        result=[list1[i]]
                    elif indexsum==mins:
                        result.append(list1[i])
        return result
        
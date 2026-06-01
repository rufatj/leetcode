class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        b=[]
        a=min(cost)
        if 2>=len(cost):
            final=cost[0]+cost[1]
            c=0
            d=0
        else:
            c=sum(cost)
            d=max(cost)
            #a.pop(0)
            cost.remove(d)
            d=max(cost)
            cost.remove(d)
            d=max(cost)
            final=c-d


        return (final)

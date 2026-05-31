class Solution:
    def mirrorDistance(self, n: int) -> int:
        arb=[]
        h=0
        g=0
        if n<10:
            print("h")
        elif n>=100:
            a=str(abs(n))
            arb=list(a)
            arb[1]=int(arb[1])
            b=arb[0]
            n=int(n)
            
            arb[0]=int(arb[2])
            arb[2]=int(b)
            c=100*arb[2]+10*arb[1]+arb[0]
            c=int(c)
            g=abs(c-n)

        else:
            a=str(abs(n))
            arb=list(a)
            b=arb[0]
            arb[0]=int(arb[1])
            arb[1]=int(b)
            c=10*arb[0]+arb[1]
            n=int(n)
            c=int(c)
            g=abs(c-n)
        #arb.append(a[0],a[1])



        return g
        

        
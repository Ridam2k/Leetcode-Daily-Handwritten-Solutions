class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1 = num1
        n2 = num2

        bits_reqd = 0

        while(n2):
            n2 = n2&(n2-1)
            bits_reqd+=1
        
        print(bits_reqd)

        res=0
        #Step1: Unset bits in num1
        for i in range(31,-1,-1):
            if(n1 & (1<<i)):
                bits_reqd-=1
                res+= (1<<i)
                if bits_reqd == 0:
                    return res
        
        #Step2: starting from left, place leftover 1's in num2 wherever they aren't already set
        for i in range(0, 32):
            if (res & (1<<i)):
                continue
            
            res+= (1<<i)
            bits_reqd -=1

            if(bits_reqd==0):
                return res

        return 0


        
#recursivly raise the power if the base item
#recursively multplies result by base and then changes the current value of power
#stops when power becomes 0, subtracts 1 (if the power is positive) or adds 1 (if the pwoer is negative) 
def raise_power(base, power, result=None):
    #check on off cases, if the pwoer is 1, -1, or 0
    #if it isnt one of those  
    if result == None:
        #check if the power is 0
        if power == 0:
            return 1
        #check if the pwoer is 1
        elif power == 1:
            return base
        #check if the pwoer is -1
        elif power == -1:
            return 1/base
        #assign result a valu
        elif power<0:
            result = 1/base
        elif power>0:
            result = base

    #base case
    if power == 1 or power == -1:
        return result
    elif power < 0:
        return raise_power(base, power+1, result*(1/base))
    elif power>0:
        return raise_power(base, power-1, result*base)


print(raise_power(4,2))

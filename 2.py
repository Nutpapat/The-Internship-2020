import sympy
def main():
    """ Main function """
    ans = []
    while True:
        num = input()
        if num == '0.0':
            break
        else: 
            index_float = num.find(".")
            num_int = num[:index_float]
            num_float = num[index_float+1:]
        default = 'FALSE'
        for i in range(len(num_float)):
            if i == 3:
                ans.append(default)
                break
            elif(i == 0):
                if sympy.isprime(int(num_int+num_float[0:1])):
                    default = 'TRUE'
            elif(i == 1):
                if sympy.isprime(int(num_int+num_float[0:2])):
                    default = 'TRUE'
            elif(i == 2):
                if sympy.isprime(int(num_int+num_float[0:3])):
                    default = 'TRUE'            
    print(*ans, sep='\n')
main()
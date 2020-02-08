def main():
    """ Main function """
    ScoreAll, num = 0, input().split(' ')
    falsenum = [] 
    for _ in range(len(num)):
        print('_', end=' ')
    print()    
    for _ in range(5):
        guess, default,  = input(), False
        score = 0
        for i in range(len(num)):
            if num[i] == guess:
                print(num[i], end=' ')
                score +=1
                default = True
            else:
                print('_', end=' ')        
        ScoreAll += score    
        for i in range(len(falsenum)): 
            print(falsenum[i], end = ' ')
        print()
        if not default:
            falsenum.append(guess)
    print(ScoreAll)
main()

def main():
    """ Main function """
    number = int(input())
    country = []
    for _ in range(number):
        country.append(input())
    country_acs = []    
    for country_ans in country:
        country_ac = ''
        word = country_ans.split(' ')
        for letter in word:
            if letter[0].isupper():
                country_ac += letter[0]
        country_acs.append(country_ac)
    country_acs.sort(key=len, reverse=True)
    for i in range(len(country_acs)-1):
        if len(country_acs[i+1]) == len(country_acs[i]):
            if country_acs[i+1] < country_acs[i]:
                country_acsBefore = country_acs[i]
                country_acsAfter = country_acs[i+1]
                country_acs[i+1] = country_acsBefore
                country_acs[i] = country_acsAfter
    for country_ans in country_acs:
        print(country_ans)
main()
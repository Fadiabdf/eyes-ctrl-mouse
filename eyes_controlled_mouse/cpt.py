cpt = 0

mot = [0, 0, 0, 0]
# if mot[0]!=mot[1]!=mot[2]!=mot[3]: not good in that case
excluded_elements = {0, 1, 4, 7, 8, 9}

for mot[0] in range(10):
    for mot[1] in range(10):
        for mot[2] in range(10):
            for mot[3] in range(10):
                # if mot[0]!=mot[1] !=mot[2]!=mot[3] :
                # if 0 not in mot and 9 not in mot and 8 not in mot and 7 not in mot 4 not in mot and 1 not in mot :
                if not set(mot) & excluded_elements:
                    if len(set(mot)) == 4:  # if there are just 4 diffrent digits
                       print("------------")
                       print(mot)
                       print("------------")
                       cpt+=1
                    else:
                       if len(set(mot)) == 3:  # au  moins ya 2 la m chose
                          print("***********")
                          print(mot)
                          print("***********")
                          cpt += 1
                    '''
                    else:
                       print(mot)
                       cpt += 1
                    '''


print(cpt)


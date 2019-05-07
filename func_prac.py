def spy_game(l):
    for i in l:
        if (0 in l) and (7 in l):
            if l.index(0) < l.index(7):
                print("True")
                break
            else:
                print("False")
                break
spy_game([0,1,2,7,2,3,4,5,6,0,1])

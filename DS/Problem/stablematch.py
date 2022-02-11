from pickletools import TAKEN_FROM_ARGUMENT4


preferedranking_man = {
    'ryan': ['lizzy', 'sarah', 'zoey', 'daniella'],
    'josh': ['sarah', 'lizzy', 'daniella', 'zoey'],
    'blake': ['sarah', 'daniella', 'zoey', 'lizzy'],
    'connor': ['lizzy', 'sarah', 'zoey', 'daniella']
}

preferedranking_woman = {
    'lizzy': ['ryan', 'blake', 'josh', 'connor'],
    'sarah': ['ryan', 'blake', 'connor', 'josh'],
    'zoey': ['connor', 'josh', 'ryan', 'blake'],
    'daniella': ['ryan', 'josh', 'connor', 'blake']
}

tetative_engagements = []
free_men = []


def init_free_man():
    for man in preferedranking_man.keys():
        free_men.append(man)


def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)


def begin_matching(man):
    # print('dealing with %s' % (man))
    for woman in preferedranking_man[man]:
        taken_match = [
            couple for couple in tetative_engagements if woman in couple]
        print('taken_match', taken_match)
        if(len(taken_match) == 0):
            tetative_engagements.append([man, woman])
            free_men.remove(man)
            # print('%s is not longer free man now he engaged to %s' % (man, woman))
            break
        elif(len(taken_match) > 0):
            current_guy = preferedranking_woman[woman].index(taken_match[0][0])
            potential_guys = preferedranking_woman[woman].index(man)
            if current_guy < potential_guys:
                print('she is happy with %s..' % (taken_match[0][0]))
            else:
                free_men.remove(man)
                free_men.append(taken_match[0][0])
                taken_match[0][0] = man
                break
        print('taken_match man name', taken_match[0][0])


init_free_man()
stable_matching()
print(tetative_engagements)

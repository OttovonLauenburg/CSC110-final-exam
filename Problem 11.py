def find_vaild_groups(name,p_group,allnext_group):
    group_i = set()
    for pg_memeber in p_group:
        #print(pg_memeber)
        for index_next_group in range(len(allnext_group)):
            if pg_memeber in allnext_group[index_next_group]:
                group_i.add(index_next_group + 1)
    group_index = {1,2,3,4,5}
    non_group_i = group_index.symmetric_difference(group_i)
    for non_group_index in non_group_i:
        print('Group',non_group_index)


roster = [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p'],['t','u','v','w']]

previous = ['e','a','h']

find_vaild_groups('r',previous,roster)
def code(res, key):
    res = "baabccbc"
    key = "abc"
    n = len(res)
    m = len(key)


    res_dict = {i:res[i] for i in range(n)}
    i , j = 0, 0

    while i < n and j < m:
        if res[i] == key[j]:
            res_dict[i] = ''
            j += 1
            i += 1
        else:
            i += 1

    output = "".join([res_dict[i] for i in range(n)])
    return output
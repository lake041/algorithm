def find(num):
    num_bin = format(num, 'b')
    ret = num
    while True:
        ret += 1
        ret_bin = format(ret, 'b')
        num_bin = num_bin.zfill(len(ret_bin))
        diff = [1 for i in range(len(ret_bin)) if ret_bin[i] != num_bin]
        print(ret, sum(diff))
        if sum(diff) <= 2:
            break
    return ret

print(find(7))
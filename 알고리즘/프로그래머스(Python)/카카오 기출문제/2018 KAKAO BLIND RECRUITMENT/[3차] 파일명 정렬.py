def solution(files):
    F = []
    for index, file in enumerate(files):
        HEAD = ''
        NUMBER = ''
        num = False
        for char in file:
            if '0' <= char <= '9':
                num = True
                NUMBER += char
            if not num:
                HEAD += char.lower()
            if num and not ('0' <= char <= '9'):
                break
        F. append((HEAD, int(NUMBER), index, file))
    F.sort(key = lambda x: (x[0], x[1], x[2]))
    
    return [x[3] for x in F]
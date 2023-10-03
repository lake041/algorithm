def solution(sequence, k):
    hap = []
    running_sum = 0
    for num in sequence:
        running_sum += num
        hap.append(running_sum)

    answer = [0, 0]
    for length in range(1, len(sequence)+1):
        stop = False
        for left in range(len(sequence)-length+1):
            right = left + length - 1
            sum_ = hap[right]-hap[left-1] if left!=0 else hap[right]
            if sum_ < k:
                continue
            elif sum_ > k:
                break
            elif sum_ == k:
                stop = True
                answer = [left, right]
                break
        if stop:
            break
            
    return answer
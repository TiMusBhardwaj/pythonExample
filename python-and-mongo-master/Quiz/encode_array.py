
def delta_encode(numbers):
    #prev =0
    res = []
    res.append(numbers[0])

    for index, n in enumerate(numbers[1:]):
        diff = numbers[index] - numbers[index-1]
        if diff >= 127 and diff <= -127:
            res.append(-128)
        res.append(diff)

    return res
if __name__ == '__main__':
    delta_encode([8,25626,25757,24367,24267,16,100,2,7277])
# unfinished as it works with the global chars list. difficulties

def sort_by_speed(chars) :
    for j in range(len(chars) - 1) :
        for i in range(len(chars) - 1) :
            if chars[i].speed < chars[i + 1].speed :
                temp = chars[i]
                chars[i] = chars[i + 1]
                chars[i + 1] = temp
    return chars

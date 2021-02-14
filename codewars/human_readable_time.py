'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

def make_readable(seconds):
    HH = 0
    MM = 0
    SS = seconds
    
    while SS >= 60:
        MM += 1
        SS -= 60
    while MM >= 60:
        HH += 1
        MM -= 60
    if HH < 10:
        HH = ('0'+ str(HH))
    else:
        HH = HH
    if MM < 10:
        MM = ('0'+ str(MM))
    else:
        MM = MM
    if SS < 10:
        SS = ('0'+ str(SS))
    else:
        SS = SS
    print (f'{HH}:{MM}:{SS}')
    output = f'{HH}:{MM}:{SS}'
    return output

if __name__ == "__main__":
    make_readable(0)
    make_readable(5)
    make_readable(60)
    make_readable(86399)
    make_readable(359999)

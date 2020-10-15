def add(x, y):
    if len(x) < len(y):
        x, y = y, x
    y = '0' * (len(x) - len(y)) + y

    res = []
    carry = 0
    for i in range(len(x)):
        i = len(x) - i - 1
        s = int(x[i]) + int(y[i]) + carry
        carry = s // 10
        s = s % 10
        res.append(str(s))
    
    if carry != 0:
        res.append(str(carry))

    return ''.join(reversed(res))


def rec_int_mul(x, y):
    if len(x) == 1 and len(y) ==1 :
        return str(int(x) * int(y))
    else:
        if len(x) < len(y):
            x, y = y, x
        y = '0' * (len(x) - len(y)) + y
   
        x = '0' * (len(x) % 2) + x
        y = '0' * (len(y) % 2) + y
        n = len(x)

        a, b = x[:n//2], x[n//2:]
        c, d = y[:n//2], y[n//2:]
        ac = rec_int_mul(a, c).lstrip('0')
        ad = rec_int_mul(a, d).lstrip('0')
        bc = rec_int_mul(b, c).lstrip('0')
        bd = rec_int_mul(b, d).lstrip('0')
        return add(add(ac + '0' * n, add(ad, bc) + '0' * (n//2)), bd).lstrip('0')

if __name__ == '__main__':
    print(rec_int_mul('1425', '29173'))
    print(1425 * 29173)
d={
    '1234':{'pin':'4567','balance':2350},
    '2345':{'pin':'9876','balance':5350},
    '3456':{'pin':'5678','balance':6350},
    '4567':{'pin':'9876','balance':7350}
    }
for i in d:
    print('account number:',i)
    print('pin number',d[i]['pin'])

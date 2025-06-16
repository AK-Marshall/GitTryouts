rows = 9
for i in range( 1,rows+1):  
    print(' ' * (rows - i ) + ' '.join(map(str,range(1,i+1))))

for i in range( rows,0,-1):  
    print(' ' * (rows - i ) + ' '.join(map(str,range(1,i+1))))
     

    
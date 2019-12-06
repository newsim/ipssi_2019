



import sys



def fn(n):
    N = int(sys.argv[1])
    Y = int(3)
    if n == 0:
        fn(n-1)
        return n*' '+((N-n)*2+1)*'x'
    else:
        if ( Y <= N ):
            return N*' '+'xx'
        else:
            return N*' '+'x'



if __name__ == '__main__':
    print( fn( int(sys.argv[1])) )
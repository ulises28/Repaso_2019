def diamond(n):
    if n % 2 == 0 or n<=0:
        print('Valor no permitido')
    else:
        t = ' '
        s = '*'
        S = int((n+1)/2)
        T = S - 1
        Diamante=''
        Espacios=''
        Asteriscos=''
        count=1
        if(T==0):
            return('*\n')
        else:           
            for x in range (T, -1,-1):
                Espacios = (t * x)
                Asteriscos = Espacios + ( s * count)
                count = count + 2
                Diamante = Diamante + Asteriscos + '\n'
            count = count - 2
            for y in range (1, S):
                count = count - 2
                Espacios = (t * y)
                Asteriscos = Espacios + (s * count)
                Diamante = Diamante + Asteriscos + '\n'
            return(Diamante)


diamond(-4)
diamond(0)
diamond(1)
diamond(3)
diamond(2)
diamond(5)
diamond(9)
diamond(15)

'''
 * 
***
 *    3-2

  * 
 ***
*****
 ***
  *   5-3


   *
  ***
 *****
*******
 *****
  ***
   *  7-4

      9-5

1-1
3-2
7-4
9-5
11-6
13-7
15-8

espacios = (n+1)/2

      *
***********
      *             1
     ***            3
    *****           5
   *******          7
  *********         9
 ***********        11
'''
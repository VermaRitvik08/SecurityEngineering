
# from pydoc import plain
import random


# fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_d(e, z):
    ###################################your code goes here#####################################
    dt = [0, 0] #d and t according to the slide calculations
    r1_s1 = [1, 0] 
    r2_s2 = [0, 1]
    temp = z
    while ((e%z)!= 0): 
        m = e%z; quotient = e//z 
        dt[0]=r1_s1[0]-quotient*r2_s2[0] 
        dt[1]=r1_s1[1]-quotient*r2_s2[1] 
        r1_s1=r2_s2[:] #swapping variables to pass onto next iteration
        r2_s2=dt[:]
        e=z; z=m   #everything is swapped one variable to the left    
        if dt[0] <= 0:  #if d is negative, add z to it
            while dt[0] < 0:    #while d is negative
                dt[0]=dt[0]+temp    #keep adding z to it
    return dt[0]

def is_prime(num):
    if num > 1:

        # Iterate from 2 to n / 2
        for i in range(2, num//2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    n = p*q
    z = (q-1)*(p-1)
    e = random.randrange(1,n)
    while (gcd(e, z)!=1): #to check if e and z are relatively prime
        e = random.randrange(1,n)
    d = get_d(e,z)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    # plaintext is a single character
    # cipher is a decimal number which is the encrypted version of plaintext
    # the pow function is much faster in calculating power compared to the ** symbol !!!
    m = (ord(plaintext)) 
    pk0, pk1 = pk
    cipher = pow(m, pk0, pk1)
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    # ciphertext is a single decimal number
    # the returned value is a character that is the decryption of ciphertext
    pk0, pk1 = pk
    plain = chr((pow(ciphertext, pk0, pk1)))
    return ''.join(plain) 

#testing code
# if __name__ == '__main__':
#     p=1297369
#     q=1297799
#     z = (p-1)*(q-1)
#     xx,xz = generate_keypair(p, q)
#     # inp = input("Enter the message to be encrypted: ")
#     # y = encrypt(xx, 'h')
#     # z = decrypt(xz, y)
#     # gcd = get_d(17, z)
    
#     # print("ans",gcd)
#     print("Answer is: ", xx,xz)

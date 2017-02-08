# create bits->next_bits
bits_dcts = [{} for i in xrange(17)]
for t in xrange(5):
    bits = [1<<i for i in xrange(2**t)]
    bits_dct = bits_dcts[2**t]
    #print bits
    for i in xrange(t):
        new_bits = set([])
        for b1 in bits:
            bits_dct[b1] = []
            for b2 in bits:
                if b1 & b2 == 0:
                    bits_dct[b1].append(b1|b2)
                    new_bits.add(b1|b2)
        bits = new_bits

#print map(bin, bits_dcts[2][0b1])
#print map(bin, bits_dcts[4][0b1])
#print map(bin, bits_dcts[16][0b1])
#print map(bin, bits_dcts[16][0b11001100])

# max ~ 1800*500*16*8 ~ 2^27
def solve(N, M):
    if N == 1:
        return [[1, 1]]
    ans = [[0,(N>>1)+1] for i in xrange(N)]
    for i in xrange(N):
        if sum(M[i]) == N-1:
            ans[i][1] = 1

    marked = [0] * N 

    rank = {16: [9,5,3,2,1], 8:[5,3,2,1], 4:[3,2,1], 2:[2,1]}
    
    dp = {}
    bits = []
    for i in xrange(N):
        dp[1<<i] = [0]*N
        dp[1<<i][i] = 1
        bits += [1<<i]

    c = 1
    #print map(bin, bits)
    while len(bits) > 1:
        new_bits = set([])
        for b1 in bits:
            #print len(bits), len(bits_dcts[N][b1])
            for b2 in bits_dcts[N][b1]: 
                if b2 not in dp:
                    dp[b2] = [0]*N
                for i in xrange(N):
                    for j in xrange(i, N):
                        #print bin(b1), bin(b2^b1), bin(b2)
                        if dp[b1][i] and dp[b2^b1][j]:
                            if M[i][j]:
                                dp[b2][i] = 1
                                ans[i][0] = max(ans[i][0], c)
                            else:
                                dp[b2][j] = 1
                                ans[j][0] = max(ans[j][0], c)
                            new_bits.add(b2)
        bits = new_bits
        c += 1
        #print map(bin,new_bits)
        #print len(bits)
    
    for i in xrange(N):
        ans[i][0] = rank[N][ans[i][0]]
    return ans

f = open('./round1/boomerang_tournament.in')
T = int(f.readline())
for _ in xrange(T):
    N = int(f.readline())
    M = []
    for i in xrange(N):
        M.append(map(int, f.readline().split()))
    print 'Case #%d:' % (_+1)
    a = solve(N, M)
    for i in xrange(N):
        print a[i][0],a[i][1]


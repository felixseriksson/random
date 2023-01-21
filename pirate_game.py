def proposal(N, M):
    """A puzzle for pirates, Ian Stewart
    http://omohundro.files.wordpress.com/2009/03/stewart99_a_puzzle_for_pirates.pdf
    Scientific American, Mathematical Recreations, May 1999
    An instance of the pirate game discussed in detail by Ian Stewart
    and Stephen Omohundro. Given N pirates (1, ..., N) in order of rising seniority,
    and M gold coins, returns an N-tuple of the coin distribution proposed by pirate N.
    Here, (x_1, ..., x_N) denotes that N proposes pirate 1 x_1 coins, and so on.
    A remark on the case N <= 2 * (M + 1) vs the case N >= 2 * (M + 1) + 1:
    When N <= 2 * (M + 1) there is a FIXED strategy (i.e. coin assignment) that 
    is uniquely optimal. When N >= 2 * (M + 1) + 1, there is not, at least not without
    a more in-depth analysis. Briefly, Pirate N = 2 * (M + 1) would like to bribe 
    M other pirates with one coin each (accepting zero coins himself, in order to not get 
    thrown overboard). Pirate N >= 2 * (M + 1) + 1 on the other hand (if he is lucky enough
    to be of a number such that a working strategy exists) would like to bribe M out of at least
    M + 1 pirates. Which M pirates he chooses to bribe is more or less arbitrary (at least in this
    analysis), so we choose to bribe the M first pirates (who are valid recipients, i.e. who are 
    amenable to a bribe in this situation).
    Returns -1 if pirate N cannot ensure his own safety regardless of how he assigns the M coins.
    """
    if N <= 2 * (M + 1):
        if N % 2:
            return tuple(M - (N - 1)//2 if i == N - 1 else (0 if i % 2 else 1) for i in range(N))
        else:
            return tuple(M - (N - 1)//2 if i == N - 1 else (1 if i % 2 else 0) for i in range(N))
    else:
        # if N - 2 * M is a power of 2
        # and at least 2 greater than M (other case caugh in above if statement)
        if not (N - 2 * M) & (N - 2 * M - 1):
            return tuple(list(proposal(2 * M, M)) + [0] * (N - 2 * M))
        else:
            # screwed either way
            return -1

print(proposal(204, 100))
# print(proposal(4, 100))
# print(proposal(5, 100))
# print(proposal(6, 100))
# print(proposal(199, 100))
# print(proposal(200, 100))
# print(proposal(201, 100))
# print(proposal(202, 100))

# 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220
# No  Yes No  No  No  Yes No  No  No  No  No  No  No  Yes
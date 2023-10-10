import pandas as pd
import numpy as np
from collections import defaultdict

# def find_optimal_transport(C, G, P):
#     N = len(C)
#     transportation_plan = []
#     for ind_selling in range(N):
#         for ind_buying in range(N):
#             sell_Q = C[ind_selling][3]
#             sell_price = C[ind_selling][1]
#             buy_Q = C[ind_buying][2]
#             buy_price = C[ind_buying][0]
#             quant = min(buy_Q, sell_Q)
#             if quant > 0:
#                 profit = quant*(buy_price-sell_price-G[ind_selling, ind_buying])
#                 if profit > 0:
#                     transportation_plan += [[ind_selling, ind_buying, quant]]
#                     return np.array(transportation_plan

def find_optimal_transport(C, G, P):
    N = len(C)

    from_i_to_j = defaultdict(int)
    i_to_j = []

    for i in range(N):
        for j in range(N):
            A_sell, A_buy, A_sell_quantity, A_buy_quantity = C[i,:]
            B_sell, B_buy, B_sell_quantity, B_buy_quantity = C[j,:]
            unit_cost = G[i, j]
            success_prob = 1 - P[i, j]
            unit_profit = (B_sell - A_buy - unit_cost) * success_prob
            from_i_to_j[(i, j)] = max(unit_profit, from_i_to_j[(i, j)])
            i_to_j.append((i, j))
    
    i_to_j = sorted(i_to_j, key = lambda x: from_i_to_j[(i, j)])

    instructions = []
    for i, j in i_to_j:
        if from_i_to_j[(i, j)] <= 0:
            break
        quantity = min(C[i, 3], C[j, 2])
        if quantity == 0:
            continue
        instructions.append([i, j, quantity])
        C[i, 3] = C[i, 3] - quantity
        C[j, 2] = C[j, 2] - quantity
    
    return np.array(instructions)

if __name__ == "__main__":
    np.random.seed(2)
    n = 3
    C = np.random.randint(0, 10, (n,4))
    G = np.random.uniform(0, 1, (n,n))
    P = np.random.uniform(0, 1, (n,n))
    C = np.array([[], [], []])

    res = find_optimal_transport(C, G, P)
    print(C)
    print(G)
    print(P)
    print()
    print(res)

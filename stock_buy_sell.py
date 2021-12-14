# Stock buy and sell

# The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

stock = [ 100 , 180 , 260 , 310 , 40 , 535 , 695 ]

profit = []
ans = 0
ans_array = []
new_stock = []

for index in range ( 0 , len ( stock ) - 1 ) :
    max_profit = 0
    selling_price_index = -1
    
    for index2 in range ( index , len ( stock ) ) :
        current_profit = stock [ index2 ] - stock [ index ]
        
        if current_profit > max_profit :
            max_profit = current_profit
            selling_price_index = index2
    
    temp = [ index , selling_price_index ]
    profit .append ( temp )
    
    if ans < max_profit : 
        ans = max_profit
        ans_array = temp
        new_stock = stock [ : index ]

print ( ans , ans_array )
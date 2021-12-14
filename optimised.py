# Stock buy and sell

# The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

stock = [ 100 , 180 , 260 , 310 , 40 , 535 , 695 ]
copy_stock = stock.copy()
index_corrector = 0
a_n_s = []

while len ( stock ) > 1 :

    profit = []
    ans = 0

    ans_array = []
    new_stockA = []
    new_stockB = []

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
            
            new_stockA = stock [ : index ]
            new_stockB = stock [ selling_price_index : ]
            
    if len ( new_stockA ) != 0 and len ( new_stockB ) == 0 :
        stock = new_stockA
        
    elif len ( new_stockA ) == 0 and len ( new_stockB ) != 0 :
        stock = new_stockB
        index_corrector += ans_array [ 1 ]
    
    elif ( len ( new_stockA ) != 0 and len ( new_stockB ) != 0 ) :

        max_A = max ( new_stockA )
        min_A = min ( new_stockA )
        max_B = max ( new_stockB )
        min_B = min ( new_stockB )
    
        if max_A - min_A >= max_B - min_B :
            stock = new_stockA
        else :
            stock = new_stockB
            index_corrector += ans_array [ 1 ]

    temp = [ ans , ans_array ]
    a_n_s .append ( temp )
    
print ( a_n_s )
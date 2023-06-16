# Naive approach Time : O(n^2) Aux Space : O(1)
def stockSpan(stocks):
    stSpan = []
    for i,stock in enumerate(stocks):
        count = 0
        for j in range(i, -1, -1):
            if stocks[j] > stock:
                break
            count += 1
        stSpan.append(count)
    return stSpan

print(stockSpan([30,20,25,28,27,29]))

# Optimized stack based method Time : O(n) Space : O(n)
def stockSpan(stocks):
    stSpan = []
    st = []
    for i, stock in enumerate(stocks):
        while st and stocks[st[-1]] <= stock:
            st.pop()
        if st:
            j = st[-1]
            stSpan.append(i-j)
        else:
            stSpan.append(i+1)
        st.append(i)
    return stSpan

print(stockSpan([30,20,25,28,27,29]))
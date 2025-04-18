def stock_span(prices):
    span = [0] * len(prices)
    stack = []  

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    
    return span

prices = [60, 70, 80, 100, 90, 75, 80, 120]

result = stock_span(prices)
print("Span for each day:", result)

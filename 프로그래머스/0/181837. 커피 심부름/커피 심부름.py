def solution(order):
    total = 0
    
    for item in order:
        if item in ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]:
            total += 4500
        elif item in ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            total += 5000
    return total
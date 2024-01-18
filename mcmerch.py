def main():
    tax = {"ON":0.13}

    price = float(sys.argv[1])
    
    quantity = int(sys.argv[2])

    pre_tax = price*quantity

    print(pre_tax)
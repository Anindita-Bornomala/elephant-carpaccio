
import sys

def main():
    tax = {"ON":0.13, "QC":0.14975, "MB":0.12}

    price = float(sys.argv[1])
    
    quantity = int(sys.argv[2])


    pre_tax = price * quantity

    print("The total cost is: $", pre_tax)


if __name__:
    main()
    
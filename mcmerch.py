
import sys

def main():
    tax = {"ON":0.13, "QC":0.14975, "MB":0.12}

    price = float(sys.argv[1])
    quantity = int(sys.argv[2])

    pre_tax = price * quantity

    tax = sys.argv[3]

    if tax == "ON":
        after_tax = pre_tax + (pre_tax*tax.get("ON"))
    elif tax == "QC":
        after_tax = pre_tax + (pre_tax*tax.get("QC"))
    elif tax == "MB":
        after_tax = pre_tax + (pre_tax*tax.get("MB"))

    print("The total cost is: $", pre_tax)
    print("The total cost after tax is: $", after_tax)


if __name__:
    main()
    
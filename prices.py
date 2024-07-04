# INDIVIDUAL WORK
# Easy level - you will read the data from prices.txt (see additional files),  compute 
# the total price of all items, and count the total number of purchased items. 

def read_prices(filename):
    total_price = 0.0
    item_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            try:
                price = float(line.strip())
                total_price += price
                item_count += 1
            except ValueError:
                continue  # ignores lines that cannot be converted to float
    
    return total_price, item_count

def main():
    filename = 'prices.txt'
    total_price, item_count = read_prices(filename)
    
    print(f"Total number of items: {item_count}")
    print(f"Total price of all items: {total_price:.2f}€")

if __name__ == "__main__":
    main()

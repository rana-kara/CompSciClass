def load_cart():
    try:
        with open("shells\\es1_cart.dat", "r") as file:
            cartdata = file.readlines()
        return cartdata
    except OSError as e:
        exit(f"OSError: {e}")

def load_offers():
    try:
        with open("shells\\es1_offers.dat", "r") as file:
            offerdata = file.readlines()
        return offerdata
    except OSError as e:
        exit(f"OSError: {e}")

def load_prices():
    try:
        with open("shells\\es1_prices.dat", "r") as file:
            pricedata = file.readlines()
        return pricedata
    except OSError as e:
        exit(f"OSError: {e}")

def main():
    cartdata = load_cart()
    offerdata = load_offers()
    pricedata = load_prices()

    inventory = {
        "bought": [],
        "gifts": []
    }

    prices = {}

    for row in pricedata:
        parsed = row.split(":")
        shell, shellprice = parsed[0].strip(), float(parsed[1].strip())
        prices[shell] = shellprice

    possible_offers = {}

    for row in offerdata:
        parsed = row.split(":")
        shells_required, gifted_shell = parsed[0].split(), parsed[1].strip()
        possible_offers[gifted_shell] = shells_required

    totalprice = 0

    for item in cartdata:
        inventory["bought"].append(item.strip())
        totalprice += prices[item.strip()]
        for key, value in possible_offers.items():
            if all(item in inventory["bought"] for item in value) and key not in inventory["gifts"]:
                inventory["gifts"].append(key.strip())
                print(f"As you buy {", ".join(value)}; you got {key} for free")
    print(f"Final Price: {totalprice:.2f}")
main()
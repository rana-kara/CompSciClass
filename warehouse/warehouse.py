import os

def load_warehouse_file():
    try:
        with open("warehouse\warehouse.txt", "r") as file:
            warehousedata = file.readlines()
        return warehousedata
    except OSError as error:
        exit(f"OSError raised: {error}")

def load_movements_file():
    try:
        with open("warehouse\movements.txt", "r") as file:
            movementsdata = file.readlines()
        return movementsdata
    except OSError as error:
        exit(f"OSError raised: {error}")

def main():
    warehouse_data = load_warehouse_file()
    movemenets_data = load_movements_file()

    warehouse_products = {}

    movements_products = {}

    for row in warehouse_data:
        warehouseparts = row.strip().split(",")
        warehouse_product_code, unit_cost, quantity_available = warehouseparts[0], float(warehouseparts[1]), int(warehouseparts[2])
        warehouse_products[warehouse_product_code] = {
            "unit_cost": unit_cost,
            "quantity_available": quantity_available
        }

    for row in movemenets_data:
        movementsparts = row.strip().split(",")
        movements_product_code, variation = movementsparts[0], int(movementsparts[1])

        if movements_product_code not in warehouse_products:
            print(f"Product {movements_product_code} not found in the warehouse database.\n")
            continue

        current_quantity = warehouse_products[movements_product_code]["quantity_available"]

        previous_total_value = current_quantity * warehouse_products[movements_product_code]["unit_cost"]

        if variation < 0 and abs(variation) > current_quantity:
            print(f"Insufficient stock for the product {movements_product_code}: Cannot decrease by {abs(variation)}.\n")
            continue

        elif variation > 0 and current_quantity + variation > 10000:
            print(f"Stock limit exceeded for product {movements_product_code}: Cannot increase by {variation}.\n")
            continue

        warehouse_products[movements_product_code]["quantity_available"] += variation

        new_total_value = warehouse_products[movements_product_code]["quantity_available"] * warehouse_products[movements_product_code]["unit_cost"]

        if variation > 0:
            print(f"Increasing the stocks of {movements_product_code} by {variation}.")
        else:
            print(f"Decreasing the stocks of {movements_product_code} by {abs(variation)}.")

        print(f"Previous total value: {previous_total_value:.2f}€")
        print(f"New total value: {new_total_value:.2f}€")
        print()


    output_path = "warehouse/warehouse2.txt"
    with open(output_path, "w") as file:
        for warehouse_product_code, details in warehouse_products.items():
            file.write(f"{warehouse_product_code},{details["unit_cost"]:.2f},{details["quantity_available"]}\n")

    print(f"Updated warehouse data has been suceessfully saved to {output_path}.")

main()
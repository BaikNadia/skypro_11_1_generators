def filter_orders_by_cost(file_iter, cost):
    row_head = next(file_iter)

    rows = [row.split(",") for row in file_iter]
    clients = [float(row[0].rstrip()) for row in rows]
    orders = [float(row[1].rstrip()) for row in rows]
    orders_costs = [float(row[2].rstrip()) for row in rows]

    indexes = [i for i, x in enumerate(orders_costs)]
    indexes = list(filter(lambda x: orders_costs[x] >= cost, indexes))

    return [f"{clients[i]}, {orders[i]}, {orders_costs[i]}" for i in indexes]

if __name__ == "__main__":
    with open("orders.csv", "r") as f:
        result = filter_orders_by_cost(f, 20)

    print(result)
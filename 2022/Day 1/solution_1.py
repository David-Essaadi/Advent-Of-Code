with open('input.txt') as file:
    inventories = map(lambda inventory: sum(map(int, inventory.splitlines())), file.read().strip().split('\n\n'))
    print(max(inventories))
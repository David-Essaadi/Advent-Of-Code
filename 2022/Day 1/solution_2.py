with open('input.txt') as file:
    inventories = sorted(list(map(lambda inventory: sum(map(int, inventory.splitlines())), file.read().strip().split('\n\n'))), reverse=True)
    print(inventories[0] + inventories[1] + inventories[2])
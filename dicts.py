def create_inventory(liston):
    seton = set(liston)
    inventory = dict()
    for e in seton:
        lego = liston.count(e)
        inventory[e] = lego
    return inventory


def add_items(mapon, liston):
    lestat = list()
    if mapon != {}:
        for key in mapon.keys():
            cant = mapon[key]
            for i in range(0,cant):
                lestat.append(key)
        return create_inventory(lestat + liston)
    else:
        return create_inventory(liston)


def decrement_items(mapon, liston):
    dic = dict()
    inventory = create_inventory(liston)
    for key in inventory.keys():
        num = mapon[key] - inventory[key]
        if num < 0: num = 0
        dic[key] = num
    return dic


def remove_item(mapet, str):
    if str in mapet.keys():
        del mapet[str]
    return mapet


def list_inventory(inventory):
    tuple_list = list()
    for key in inventory.keys():
        if inventory[key] > 0:
            tuple_list.append((key, inventory[key]))
    return tuple_list



WAGER_TYPES = {
    'LOTTO_WAGER': 'Lucky Numbers',
    'WAGER': 'Sports',
    'LIVE_WAGER': 'Live Sports',
    'BETGAMES_WAGER': 'Betgames',
    'EVOLUTION_WAGER': 'Evolution Games',
    'EZUGI_WAGER': 'Ezugi Games',
    'PRAGMATIC_WAGER': 'Pragmatic Play Games'
}

PURCHASE_SETTINGS_ORDER = [
    'LOTTO_WAGER',
    'WAGER',
    'LIVE_WAGER',
    'BETGAMES_WAGER',
    'EVOLUTION_WAGER',
    'EZUGI_WAGER',
    'PRAGMATIC_WAGER'
]

purchase_settings = [
    {
        'wagerType': 'PRAGMATIC_WAGER',
        'minTotalOdds': '',
        'wageredPercent': '15',
        'sameEventAllowed': True
    },
    {
        'wagerType': 'BETGAMES_WAGER',
        'minTotalOdds': '2',
        'wageredPercent': '100',
        'sameEventAllowed': True
    },
    {
        'wagerType': 'LIVE_WAGER',
        'minTotalOdds': '3',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
    {
        'wagerType': 'LOTTO_WAGER',
        'minTotalOdds': '4',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
    {
        'wagerType': 'WAGER',
        'minTotalOdds': '',
        'wageredPercent': '100',
        'sameEventAllowed': False
    },
]

result = [
    'Lucky Numbers',
    'Sports',
    'Live Sports',
    'Betgames',
    'Pragmatic Play Games'
]

list1 = []
for item in purchase_settings:
    list1.append(item["wagerType"])

list2 = []
for purchase_type in PURCHASE_SETTINGS_ORDER:
    if purchase_type in list1:
        list2.append(WAGER_TYPES.get(purchase_type))


example = [WAGER_TYPES.get(purchase_type)
           for purchase_type in PURCHASE_SETTINGS_ORDER
           if purchase_type in
           [item["wagerType"] for item in purchase_settings]]

print(list1)
print(list2)
print(example)
print(list2==example)

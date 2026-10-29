rates = {
    'local':         {'up_to_1kg': 8000,  'from_1_to_5kg': 15000},
    'national':      {'up_to_1kg': 15000, 'from_1_to_5kg': 28000},
    'international': {'up_to_1kg': 60000, 'from_1_to_5kg': 120000}
}

print(rates['national']['from_1_to_5kg'])
print(rates['international']['from_1_to_5kg'])
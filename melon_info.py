"""Print out all the melons in our inventory."""

# Setup the underlying files by creating a dict within a dict for easy assess the attributes
# For each attribute, use the import function to bring it in. In this case, there's only one item in the underlying file > a dict

from melons import items

def print_melon(items):
    """Print each melon with corresponding attribute information."""
    # Iterate over the dicts from the underlying file
    for name in items.keys():
        # Use unpacking to assign variables (In this case, seedless and price)
        seedless, price = items[name]['seedless'], items[name]['price']
        # Setup word phrases to complete the sentense at the end
        have_or_have_not = 'have'
        if seedless:
            have_or_have_not = 'do not have'
        # print the output of the fuction
        print(f'{name} {have_or_have_not} seeds and are ${price:.2f}')
        print("-------")

print_melon(items)
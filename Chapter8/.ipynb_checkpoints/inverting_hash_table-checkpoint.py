def hash_table_creation(hash_table, key, value):
    """
    Building a hash table
    parameters: 
        hash_table
        key: hash_table key
        value: hash_table key value
    Returns:
        hash_table / Dict
    """
    if key in hash_table:
        hash_table[key].append(value)
    else:
        hash_table[key] = [value]
    
def invert_it(inverted):
    """
    inverting the hash table
    parameters: 
        inverted table/dict
    Returns:
        inverted table/dict
    """
    hash_table_creation(hash_table, key, value)
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]
        return inverted
        
hash_table = {}
inverted = {}
data_set = [('Name', 'Fatma'), ('Age', '20')]
for key, value in data_set:
    hash_table_creation(hash_table, key, value)
print(hash_table)

for key, value in data_set:
    invert_it(inverted)
print(inverted)
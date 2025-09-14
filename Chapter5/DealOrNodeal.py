def cases_handling(n, first_case):
    if not (1 <= first_case <= n):
        return "Invalid case number!"
    else:
        cases_list = []
        if first_case not in cases_list:
            cases_list.append(first_case) 
        i = 1
        while i < n:
            New_Cases = int(input())
            if not (1 < New_Cases <= n):
                return "Invalid case number!"
            else:
                cases_list.append(New_Cases)
            i += 1
        return cases_list
    
def dealOrnot(n, cases, deal):
    """
    determining a decision in the game
    Args:
        n: number of opened cases
        cases: our cases, must be equal to n
        deal: offered deal -> int 
    Returns: 
        Decision -> a string
    """
    if not (n <= 10) and not (deal > 10):
        return "invalid number of available cases AND unaccepted offer!"
    else:
        total_gained_amount = 0
        total_amount = 0
        Amounst_hash_table = {1: 100, 2: 500, 3: 1000, 4: 5000, 5: 10000, 6: 25000, 7:50000, 8:100000, 9: 500000, 10: 1000000}
        for case in cases:
            if case in Amounst_hash_table:
                total_gained_amount = total_gained_amount + Amounst_hash_table[case]
        for key, value in Amounst_hash_table.items():
            total_amount = total_amount + value 
        remaining_unopened_cases_amount = total_amount - total_gained_amount
        if remaining_unopened_cases_amount > deal:
            return "no deal"
        else:
            return "deal"
            
n = int(input())
first_case = int(input())
cases = cases_handling(n, first_case)
deal = int(input())
print(dealOrnot(n, cases, deal))

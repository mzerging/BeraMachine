

def get_account_and_priv_key_list():
    acc_list = []
    priv_list = []
    with open('data/accounts.txt', 'r') as f:
         for line in f:
            line = line.strip().split(',')
            account = line[0]
            priv_key = line[1]
            acc_list.append(account)
            priv_list.append(priv_key)
    
    return acc_list, priv_list

    
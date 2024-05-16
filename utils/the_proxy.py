

def get_proxies_list():
    
    with open('data/proxies.txt', 'r') as f:
        proxies = f.readlines()
    
    print(proxies)

    return proxies

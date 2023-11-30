response = requests.get(url)

if response.status_code == 200:
        data = response.json()
        print(f'Network:', data['result']['node_info']['network'])
        print(f'version:', data['result']['node_info']['version'])
        print(f'latest_block_height:', data['result']['sync_info']['latest_block_height'])
        print(f'latest_block_time:', data['result']['sync_info']['latest_block_time'])
        
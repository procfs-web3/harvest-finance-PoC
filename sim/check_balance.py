from web3 import HTTPProvider, Web3

def sendTx(fcall, account, value=0):
    tx = fcall.build_transaction(
        {
            'from': account['address'],
            'nonce': web3.eth.get_transaction_count(account['address']),
            'value': Web3.toWei(value, "ether")
        }
    )
    stx = web3.eth.account.sign_transaction(tx, private_key=account["privKey"])
    tx_hash = web3.eth.send_raw_transaction(stx.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def check_balance():
    rpcUrl = "https://realworld.chainlight.io/da-rw1/rpc/da-rw1_2111_a7076ac760d14b3c10c3e00b38a68366915e29b32b464c537fb557d36b2eff3d"
    privKey = "0x16c22a7571b57b4b5e46ddbbd3b4bd6d698db267073b4765ee25cda3b2d30789"
    account = {"privKey": privKey, "address": "0xc943eDB4Bb4439d65B81f2f60Bc698411e910B14"}

    exploitAddress = "0x2EBB06c0683f62873B76714FF51bBD2bC245Fa1C"
    web3 = Web3(HTTPProvider(rpcUrl))
    return web3.eth.get_balance(account["address"]) / Web3.toWei(1, "ether")

if __name__ == "__main__":
    
    '''
    with open("ExploitWrapper.abi", "r") as f:
        exploitAbi = f.read()
    with open("Level.abi", "r") as f:
        levelAbi = f.read()
    exploitContract = web3.eth.contract(address=exploitAddress, abi=exploitAbi)
    sendTx(exploitContract.functions.fire(), account)
    
    '''
    print("hi")
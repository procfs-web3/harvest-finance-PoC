class EmuYCurveVault:
    '''
    function investedUnderlyingBalance() public view returns (uint256) {
    uint256 shares = IERC20(ycrvVault).balanceOf(address(this));
    uint256 price = IVault(ycrvVault).getPricePerFullShare();
    // the price is in yCRV units, because this is a yCRV vault
    // the multiplication doubles the number of decimals for shares, so we need to divide
    // the precision is always 10 ** 18 as the yCRV vault has 18 decimals
    uint256 precision = 10 ** 18;
    uint256 ycrvBalance = shares.mul(price).div(precision);
    // now we can convert the balance to the token amount
    uint256 ycrvValue = underlyingValueFromYCrv(ycrvBalance);
    return ycrvValue.add(IERC20(underlying).balanceOf(address(this)));
  }

   function underlyingValueFromYCrv(uint256 ycrvBalance) public view returns (uint256) {
    return IPriceConvertor(convertor).yCrvToUnderlying(ycrvBalance, uint256(tokenIndex));
  }

'''
    def __init__(self):
        self.tokens = dict()

    def getPricePerFullShare(self):
        return 0
    
    def balanceOf(self, address):
        if address in self.tokens:
            return self.tokens[address]
        else:
            return 0 


class EmuVault:
    def __init__(self):
        self.totalSupply = 112452070124349
        self.underlyingBalance = 52674539857280
        self.tokens = dict()
        self.adress = 0x11112222

    def deposit(self, msg_sender, amount):
        yvault = self.ycurveVault
        share = yvault.balanceOf(self.address)
        price = yvault.getPricePerFullShare()
        mintAmount = amount * self.totalSupply // self.underlyingBalance
        mintAmount += share * price // 10**18
        self._mint(msg_sender, mintAmount)
        self.underlyingBalance += amount

    def balanceOf(self, address):
        if address in self.tokens:
            return self.tokens[address]
        else:
            return 0 

    def _mint(self, owner, amount):
        if owner in self.tokens:
            self.tokens[owner] += amount
        else:
            self.tokens[owner] = amount

if __name__ == "__main__":
    vault = EmuVault()
    attacker = 0xcc
    vault.deposit(attacker, 50000000 * 10**6 - 100000 * 10**6) #106528852732436
    print(vault.balanceOf(attacker))
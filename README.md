# ethtoken.py

This is a tiny library leveraging web3.py to make an interface for
working with [EIP20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md)
tokens on Ethereum. (formerly ERC20)

**It is currently in Pre-alpha, with 0 automated tests**

## Usage

### Install

```sh
virtualenv -p python3 venv
. venv/bin/activate
pip install --pre ethtoken
```

### Initialize

```py
from ethtoken import token

# Use the ENS name that points to your token contract here:
omg = token("omg.thetoken.eth")
```

### Use standard EIP20 methods

Most EIP20 methods are optional. `ethtoken` makes no attempt to
verify which methods are implemented by a token contract.

Here's an example with all the read functions working:

```py
>>> omg.name()
'OMGToken'

>>> omg.symbol()
'OMG'

>>> omg.decimals()
18

>>> omg.totalSupply()
140245398245132780789239631

# Use the ENS name of the owner address here:
>>> omg.balanceOf('ethereumfoundation.eth')
308744633639977714804

```

### Custom methods

`ethtoken` has a single custom method not in the EIP20 spec: `token_balance`.

```py
>>> omg.token_balance("ethereumfoundation.eth")
Decimal('308.744633639977714804')
```

It returns the balance of an address, with the decimal point shifted according
to the `decimals()` value on the contract. In other words,
it is the human-readable number of tokens that the given address owns.

### Completely Untested: Transfers

In theory, you could use this to send a token. I haven't
even tried it once yet. Just don't use it. If you're going
to ignore me, don't blame me if you lose tokens
or ether.

This should theoretically transfer 1 giga units from 0x0 to 0xdead.
(That's 1 nanotoken, at 18 decimals). Of course, this won't
work if you don't control the 0x0 address. (hint: you don't)

```py
from web3 import Web3

>>> omg.transfer(
  '0x000000000000000000000000000000000000dEaD',
  10 ** 9,
  transact={
    'from': '0x0000000000000000000000000000000000000000',
    'gasPrice': Web3.toWei('0.1', 'gwei'),
  },
)
```

### Ownership Disclosure

I own some OmiseGo tokens, because anyone
who had some ether during their airdrop got some. I don't
have any opinions on the company or token.

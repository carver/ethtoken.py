# ethtoken.py Project

This is a tiny library leveraging web3.py to make an interface for
working with EIP20 (formerly ERC20) tokens on Ethereum.

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

omg = token("omg.thetoken.eth")

omg.token_balance("ethereumfoundation.eth")
```


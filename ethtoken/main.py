
from decimal import Decimal

from cytoolz import curry
from web3.contract import ConciseContract

from ethtoken.abi import EIP20_ABI


@curry
def eip20_tokenBalanceOf(token, address):
    return Decimal(token.balanceOf(address)) / (10 ** token.decimals())


def eip20_token(address, w3=None, **kwargs):
    '''
    :param address: `EIP20
        <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md>`_
        token contract
    :type address: ENS name or hex str
    :param `Web3 <http://web3py.readthedocs.io/en/latest/quickstart.html#using-web3>`_ w3:
        for connection, will autodetect if missing
    '''
    if w3 is None:
        from web3.auto import w3
        if w3 is None:
            raise RuntimeError("Could not auto-detect web3 connection, please supply it as arg w3")

    if 'abi' in kwargs:
        abi = kwargs['abi']
    else:
        abi = EIP20_ABI

    if 'ContractFactoryClass' in kwargs:
        Factory = kwargs['ContractFactoryClass']
    else:
        Factory = ConciseContract

    contract = w3.eth.contract(address, abi=abi, ContractFactoryClass=Factory, **kwargs)
    contract.token_balance = eip20_tokenBalanceOf(contract)
    return contract

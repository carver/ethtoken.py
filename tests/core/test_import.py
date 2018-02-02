

def test_import():
    from ethtoken import token
    from ethtoken.abi import EIP20_ABI

    assert token is not None
    assert EIP20_ABI is not None

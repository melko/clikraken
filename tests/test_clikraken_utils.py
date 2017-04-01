from clikraken import clikraken_utils


def test_asset_pair_short():
    assert 'ETHEUR' == clikraken_utils.asset_pair_short('XETHZEUR')


def test_quote_currency_from_asset_pair():
    assert 'EUR' == clikraken_utils.quote_currency_from_asset_pair('XETHZEUR')

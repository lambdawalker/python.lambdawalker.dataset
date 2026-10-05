def test_smoke():
    from lambdawalker.dataset.DataProvider import DataProvider
    from lambdawalker.dataset.Dataset import Dataset
    assert DataProvider is not None
    assert Dataset is not None
    print("dataset OK")

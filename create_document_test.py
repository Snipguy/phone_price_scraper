import main



def test_normalize_price():
    result = main.normalize_price("۱۲۳۴۵۶۷")

    assert result == "1234567"

def test_create_document(tmp_path):

    phone_models = ["iPhone 16", "Samsung A07"]
    d_prices = ["1000", "500"]
    t_prices = ["1100", "550"]
    urls_len = 2
    output_path = tmp_path / "prices.docx"

    main.create_document(
        phone_models,
        d_prices,
        t_prices,
        output_path
    )

    assert (tmp_path / "prices.pdf").exists()
    assert not (tmp_path / "prices.docx").exists()
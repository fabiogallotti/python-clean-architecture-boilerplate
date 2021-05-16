from types import SimpleNamespace


def test_service_is_created(configs):
    # import inside test so env vars monkeypatch is applied first
    from main import handlers

    assert isinstance(handlers, SimpleNamespace)

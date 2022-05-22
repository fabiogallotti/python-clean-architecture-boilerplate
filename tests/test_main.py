from types import SimpleNamespace

from fastapi import FastAPI


def test_service_is_created(configs):
    # import inside test so env vars monkeypatch is applied first
    from main import handlers

    assert isinstance(handlers, SimpleNamespace)
    assert isinstance(handlers.api, FastAPI)

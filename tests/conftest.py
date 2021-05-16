import pytest

from application import config


@pytest.fixture(scope="session")
def monkeypatch_session():
    """Fixture to create manually a session scoped monkeypatch object."""
    # see https://github.com/pytest-dev/pytest/issues/1872#issuecomment-375108891
    from _pytest.monkeypatch import MonkeyPatch

    m = MonkeyPatch()
    yield m
    m.undo


@pytest.fixture(scope="session")
def configs(monkeypatch_session):
    monkeypatch_session.setenv("ENV", "test")
    return config.load()


def pytest_addoption(parser):
    """
    Registers new pytest command line options.
        - `--rununit`: when passed, only unit tests are run
    """
    parser.addoption("--rununit", action="store_true", default=False, help="run only unit tests")

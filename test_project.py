import csv
import pytest
from project import checkweek



@pytest.fixture
def mock_open_file(monkeypatch):
    def mock_open(filename, *args, **kwargs):
        return open(filename, *args, **kwargs)

    monkeypatch.setattr("builtins.open", mock_open)

def test_empty_file(mock_open_file):
    assert checkweek() == "Week 1"

def test_week_2(mock_open_file):

    assert checkweek() == "Week 2"


def test_week_3(mock_open_file):

    assert checkweek() == "Week 3"

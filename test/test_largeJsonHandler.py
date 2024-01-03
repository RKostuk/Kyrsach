import json
from unittest.mock import mock_open, patch

from app.services.structure import LargeJsonHandler


# Test for initialization
def test_initialization():
    mock_data = '{"key": "value"}'
    with patch('builtins.open', mock_open(read_data=mock_data)):
        handler = LargeJsonHandler()
        assert handler.data == json.loads(mock_data)


# Test for load_data method
def test_load_data():
    mock_data = '{"key": "value"}'
    with patch('builtins.open', mock_open(read_data=mock_data)) as mock_file:
        handler = LargeJsonHandler()
        handler.load_data()
        mock_file.assert_called_with('inverted_index.json', 'r')
        assert handler.data == json.loads(mock_data)


# Test for write_json static method
def test_write_json():
    test_data = {"key": "value"}
    with patch('builtins.open', mock_open()) as mock_file:
        LargeJsonHandler.write_json(test_data)
        mock_file.assert_called_with('inverted_index.json', 'w')
        mock_file().write.assert_called()


# Test for get_value method
def test_get_value():
    handler = LargeJsonHandler()
    handler.data = {"key1": "value1", "key2": "value2"}
    assert handler.get_value("key1") == "value1"
    assert handler.get_value("key3") is None

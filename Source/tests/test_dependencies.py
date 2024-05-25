import pytest
import os
import pathlib
from app.dependenciesloader import DependenciesLoader

def test_load_dependencies_not_called():
    with pytest.raises(Exception):
        dl = DependenciesLoader()
        dl.get_num_dependencies()

def test_file_not_found():
    with pytest.raises(FileExistsError):
        dl = DependenciesLoader()
        dl.load_dependencies("not a file path")
    
def test_load_data():
    test_file_path = pathlib.Path(__file__).parent.resolve()
    path = os.path.join(test_file_path, "test_load_data.json")
    dl = DependenciesLoader()
    dl.load_dependencies(path)
    assert dl._data == {'age': 30, 'city': 'New York', 'name': 'John'}


def test_get_num_dependencies():
    test_file_path = pathlib.Path(__file__).parent.resolve()
    path = os.path.join(test_file_path, "test_dependencies.json")
    dl = DependenciesLoader()
    dl.load_dependencies(path)
    assert dl.get_num_dependencies() == 3
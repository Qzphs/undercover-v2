import pytest

from game.file import File


def test_file_words():
    file = File("tests/mock_file.txt")
    assert file.n_pairs == 2
    assert file.get() == ("bell", "salmon")
    assert file.get() == ("angry", "red face")


def test_file_words_empty():
    file = File("tests/mock_file_empty.txt")
    assert file.n_pairs == 0
    assert file.get() is None


def test_file_nonexistent():
    with pytest.raises(FileNotFoundError):
        File("tests/mock_file_nonexistent.txt")


def test_used_words_commented_out():
    file = File("tests/mock_file.txt")
    assert "bell, salmon" in file.lines
    file.get()
    assert "bell, salmon" not in file.lines
    assert "# bell, salmon" in file.lines

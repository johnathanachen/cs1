import pytest
from logger import Logger

def setup_for_test():
    file_name = "newfile"
    logger = Logger(file_name)
    return logger

def test_setup():
    logger = setup_for_test()
    assert logger.file_name == "newfile"

def test_write_metadata():
    logger = setup_for_test()
    pop_size = 1000
    vacc_percentage = .25
    virus_name = "Ebola"
    mortality_rate = 1
    basic_repro_num = .30
    assert metadata == [1000, .25, "Ebloa", 1, .30]
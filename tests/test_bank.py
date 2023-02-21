"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank


@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_create_account_raises_error_if_name_blank(bank: Bank):
    # This means: assert an exception is raised during the following block
    with pytest.raises(Exception):
        bank.create_account('')

def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0

def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'

def test_get_account_raises_error_if_no_account_matches(bank: Bank):
    bank.create_account('Name 1')

    # This means: assert an exception is raised during the following block
    with pytest.raises(ValueError):
        bank.get_account('Name 2')

def test_add_funds_into_account_positive_amount(bank: Bank):

    # testing values
    account_name = 'Guillem_test'
    account_amount = 750

    # setup
    bank.create_account(account_name)
    value_before_addition= bank.get_account(account_name).balance

    # action to test
    bank.add_funds(account_name,account_amount)

    # analyse output
    value_after_addition = bank.get_account(account_name).balance

    assert((value_after_addition - value_before_addition) == account_amount)

def test_add_funds_into_account_negative_amount(bank: Bank):

    # testing values
    account_name = 'Guillem_test'
    account_amount = -1750

    # setup
    bank.create_account(account_name)
    value_before_addition= bank.get_account(account_name).balance

    # action to test
    bank.add_funds(account_name,account_amount)

    # analyse output
    value_after_addition = bank.get_account(account_name).balance

    assert((value_after_addition - value_before_addition) == account_amount)


def test_add_funds_into_account_positive_negative_multiple_amounts_accounts(bank: Bank):

    # testing values
    account_name1 = 'Guillem_test'
    account_amount1 = -1750
    account_name2 = 'Pep_test'
    account_amount2 = 3250

    # setup
    bank.create_account(account_name1)
    value_before_addition1= bank.get_account(account_name1).balance
    bank.create_account(account_name2)
    value_before_addition2= bank.get_account(account_name2).balance

    # action to test 1
    bank.add_funds(account_name1,account_amount1)
    bank.add_funds(account_name2,account_amount2)

    # analyse output
    value_after_addition1 = bank.get_account(account_name1).balance
    value_after_addition2 = bank.get_account(account_name2).balance

    assert((value_after_addition1 - value_before_addition1) == account_amount1)
    assert((value_after_addition2 - value_before_addition2) == account_amount2)

    


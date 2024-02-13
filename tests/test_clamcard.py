class BankAccountSpy:
    def __init__(self):
        self.charged = 0

    def charge(self, amount: float) -> None:
        self.charged = amount


class ClamCard:
    def __init__(self, bank_account: BankAccountSpy) -> None:
        bank_account.charge(0.01)


def test__clam_card_linked_to_a_bank_account__charges_a_cent_for_verification() -> None:
    bank_account = BankAccountSpy()
    _ = ClamCard(bank_account)

    assert bank_account.charged == 0.01

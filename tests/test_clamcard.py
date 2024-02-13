class BankAccountSpy:
    def __init__(self):
        self.charged = 0

    def charge(self, amount: float) -> None:
        self.charged += amount


class ClamCard:
    def __init__(self, bank_account: BankAccountSpy) -> None:
        self._bank_account = bank_account
        bank_account.charge(0.01)

    def pass_gate(self, station: str) -> None:
        if station == "Amersham":
            self._bank_account.charge(2.5)


def test__clam_card_linked_to_a_bank_account__charges_a_cent_for_verification() -> None:
    bank_account = BankAccountSpy()

    _ = ClamCard(bank_account)

    assert bank_account.charged == 0.01


def test__single_journey_in_zone_A__charges_additonal_zone_A_price() -> None:
    bank_account = BankAccountSpy()
    sut = ClamCard(bank_account)

    sut.pass_gate("Asterisk")
    sut.pass_gate("Amersham")

    assert bank_account.charged == 2.51

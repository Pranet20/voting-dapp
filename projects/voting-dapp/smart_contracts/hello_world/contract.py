from algopy import ARC4Contract, UInt64, arc4


class VotingContract(ARC4Contract):
    """
    Simple Voting Smart Contract
    """

    def __init__(self) -> None:
        self.option_a = UInt64(0)
        self.option_b = UInt64(0)

    @arc4.abimethod()
    def vote_a(self) -> None:
        self.option_a += UInt64(1)

    @arc4.abimethod()
    def vote_b(self) -> None:
        self.option_b += UInt64(1)

    @arc4.abimethod(readonly=True)
    def get_results(self) -> tuple[UInt64, UInt64]:
        return self.option_a, self.option_b

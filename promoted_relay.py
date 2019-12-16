import shield
import relay


class PromotedRelay(shield.Shield):
    """
    Class that pepresents a promotedRelay piece.
    """
    def __init__(self, lowerSide):
        self.origin = relay.Relay
        self.lowerSide = lowerSide
        self.ID = id(PromotedRelay)
        self.canPromote = False

    def __repr__(self):
        if self.lowerSide:
            return "+r"
        else:
            return "+R"



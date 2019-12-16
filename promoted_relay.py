import shield
import relay


class PromotedRelay(shield.Shield):
    def __init__(self, lowerSide):
        self.promoted = True
        self.origin = relay.Relay
        self.lowerSide = lowerSide

    def __repr__(self):
        if self.lowerSide:
            return "+r"
        else:
            return "+R"



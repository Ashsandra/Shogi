from shield import Shield
from relay import Relay


class PromotedPreview(Shield):
    def __init__(self):
        self.promoted = True
        self.origin = Relay(Shield.isLower())

    def __repr__(self):
        if self.lowerSide:
            return "+r"
        else:
            return "+R"



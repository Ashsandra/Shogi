import shield
import preview


class PromotedPreview(shield.Shield):
    def __init__(self, lowerSide):
        self.promoted = True
        self.origin = preview.Preview
        self.lowerSide = lowerSide

    def __repr__(self):
        if self.lowerSide:
            return "+p"
        else:
            return "+P"


import shield
import preview


class PromotedPreview(shield.Shield):
    def __init__(self, lowerSide):
        self.canPromote = False
        self.promoted = True
        self.origin = preview.Preview
        self.lowerSide = lowerSide
        self.ID = id(PromotedPreview)

    def __repr__(self):
        if self.lowerSide:
            return "+p"
        else:
            return "+P"


from shield import Shield
from preview import Preview


class PromotedPreview(Shield):
    def __init__(self):
        self.promoted = True
        self.origin = Preview(Shield.isLower())

    def __repr__(self):
        if self.lowerSide:
            return "+p"
        else:
            return "+P"


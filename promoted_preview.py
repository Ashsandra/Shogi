from shield import Shield
from preview import Preview


class PromotedPreview(Shield):
    def __init__(self):
        self.promoted = True
        self.origin = Preview(Shield.isLower())


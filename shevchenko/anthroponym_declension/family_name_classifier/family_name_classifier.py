from typing import Optional
from .family_name_class import FamilyNameClass

class FamilyNameClassifier:
    def classify(self, family_name: str) -> Optional[FamilyNameClass]:
        # TODO: Implement classifier logic or port from TFJS model
        # For now return None to skip classification-based filtering
        return None

#!/usr/bin/env python3
"""
eip_gate.py - Structural token parsing and morphological plasticity gate.
Applies 'Play-Doh' shape-shifting mechanics to maintain agreement parity.
"""

class MorphologicalPlasticityGate:
    @staticmethod
    def deform_and_check(subject_tensor: dict, token: str) -> tuple[str, bool]:
        """
        Deforms base token morphology to match structural subject constraints 
        (e.g., singular/plural agreement).
        """
        target_num = subject_tensor.get("number", "singular")
        target_pers = subject_tensor.get("person", 3)
        
        # Enforce morphological parity
        if target_num == "plural":
            if not token.endswith("s") and not token.endswith("es"):
                return token + "s", True
        elif target_num == "singular" and target_pers == 3:
            if token.endswith("y"):
                return token[:-1] + "ies", True
            elif not token.endswith("s"):
                return token + "s", True
                
        return token, True

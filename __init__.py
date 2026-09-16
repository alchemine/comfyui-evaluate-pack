"""Custom nodes mappings."""

from .nodes.evaluate import Evaluate, Evaluates


NODE_CLASS_MAPPINGS = {
    # EvaluatePack/Evaluate ##########################################################
    "Evaluate": Evaluate,
    "Evaluates": Evaluates,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # EvaluatePack/Evaluate ##########################################################
    "Evaluate": "Evaluate",
    "Evaluates": "Evaluates",
}

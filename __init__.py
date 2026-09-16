"""Custom nodes mappings."""

from .nodes.evaluate import Evaluate


NODE_CLASS_MAPPINGS = {
    # EvaluatePack/Evaluate ##########################################################
    "Evaluate": Evaluate,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # EvaluatePack/Evaluate ##########################################################
    "Evaluate": "Evaluate",
}

"""Nodes in EvaluatePack/Evaluate."""

from .lib.utils import exception_handler


#################################################################
# Nodes
#################################################################
_DEFAULT_EVALUATE_CODE = """def main(tag: str) -> str:
    tags = [t.strip() for t in tag.split(",") if t.strip()]
    return ", ".join(sorted(tags))
"""


class Evaluate:
    """Run user Python code defining main(tag: str) -> str."""

    INPUT_TYPES = lambda: {
        "required": {
            "tag": ("STRING", {"forceInput": True}),
            "code": (
                "STRING",
                {
                    "default": _DEFAULT_EVALUATE_CODE,
                    "multiline": True,
                    "dynamicPrompts": False,
                },
            ),
        },
    }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("tag",)
    FUNCTION = "execute"
    CATEGORY = "EvaluatePack/Evaluate"

    @classmethod
    @exception_handler
    def execute(cls, tag: str, code: str) -> tuple[str]:
        ns: dict = {}
        exec(compile(code, "<evaluate_code>", "exec"), ns)
        main = ns.get("main")
        if not callable(main):
            raise TypeError("code must define a callable main(tag: str) -> str")
        out = main(tag)
        if not isinstance(out, str):
            raise TypeError(f"main must return str, got {type(out).__name__}")
        return (out,)

    @classmethod
    def IS_CHANGED(cls, tag: str, code: str) -> tuple:
        return (tag, code)


_DEFAULT_EVALUATES_CODE = """def main(tags: list[str]) -> str:
    return ", ".join(tags)
"""


class Evaluates:
    """Run user Python code defining main(tags: list[str]) -> str."""

    INPUT_IS_LIST = True

    INPUT_TYPES = lambda: {
        "required": {
            "tags": ("STRING", {"forceInput": True}),
            "code": (
                "STRING",
                {
                    "default": _DEFAULT_EVALUATES_CODE,
                    "multiline": True,
                    "dynamicPrompts": False,
                },
            ),
        },
    }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("tag",)
    FUNCTION = "execute"
    CATEGORY = "EvaluatePack/Evaluate"

    @classmethod
    @exception_handler
    def execute(cls, tags: list[str], code: list[str]) -> tuple[str]:
        # INPUT_IS_LIST hands every input over as a list; `code` is one widget.
        ns: dict = {}
        exec(compile(code[0], "<evaluates_code>", "exec"), ns)
        main = ns.get("main")
        if not callable(main):
            raise TypeError("code must define a callable main(tags: list[str]) -> str")
        out = main(list(tags))
        if not isinstance(out, str):
            raise TypeError(f"main must return str, got {type(out).__name__}")
        return (out,)

    @classmethod
    def IS_CHANGED(cls, tags: list[str], code: list[str]) -> tuple:
        return (tuple(tags), tuple(code))

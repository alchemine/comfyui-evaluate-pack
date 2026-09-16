# ComfyUI-Evaluate-Pack

[English](README.md) | [한국어](README_ko.md)

Transforms a string by dynamically evaluating Python code written in the node.

## Usage

Feed a string into **Evaluate**, write a `main(tag: str) -> str` in the `code` widget, read the return value out of `tag`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tag` | STRING | (required) | Input string passed to `main(tag)` |
| `code` | STRING (multiline) | sort-tags snippet | Python source that must define `def main(tag: str) -> str` |

| Output | Description |
|--------|-------------|
| `tag` | The string returned by `main(tag)` |

The default code sorts comma-separated tags alphabetically:

```python
def main(tag: str) -> str:
    tags = [t.strip() for t in tag.split(",") if t.strip()]
    return ", ".join(sorted(tags))
```

> [!WARNING]
> `Evaluate` and `Evaluates` execute arbitrary Python via `exec()`. Only use them with code you trust.

**Evaluates** does the same over a list of strings: connect a string list to `tags`, and the whole
list is handed to one `main(tags: list[str]) -> str` call.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `tags` | STRING (list) | (required) | Input strings passed to `main(tags)` |
| `code` | STRING (multiline) | join snippet | Python source that must define `def main(tags: list[str]) -> str` |

| Output | Description |
|--------|-------------|
| `tag` | The string returned by `main(tags)` |

The default code joins the strings with commas:

```python
def main(tags: list[str]) -> str:
    return ", ".join(tags)
```

## Installation

Search for **ComfyUI-Evaluate-Pack** in ComfyUI Manager, or:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/alchemine/comfyui-evaluate-pack
```

## Nodes (`EvaluatePack/Evaluate`)

**Evaluate** — runs user-defined Python code against an input string and returns the transformed result.

**Evaluates** — the same over a list of strings, reduced to one output string.

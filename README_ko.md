# ComfyUI-Evaluate-Pack

[English](README.md) | [한국어](README_ko.md)

워크플로우 안에서 사용자 정의 Python 함수를 문자열에 적용합니다.

## 사용법

문자열을 **Evaluate**에 넣고, `code` 위젯에 `main(tag: str) -> str`을 작성하면 반환값이 `tag`로 나옵니다.

| 파라미터 | 타입 | 기본값 | 설명 |
|----------|------|--------|------|
| `tag` | STRING | (필수) | `main(tag)`에 전달될 입력 문자열 |
| `code` | STRING (multiline) | 태그 정렬 스니펫 | `def main(tag: str) -> str`을 정의해야 하는 Python 코드 |

| 출력 | 설명 |
|------|------|
| `tag` | `main(tag)`의 반환값 |

기본 코드는 쉼표로 구분된 태그를 알파벳순으로 정렬합니다:

```python
def main(tag: str) -> str:
    tags = [t.strip() for t in tag.split(",") if t.strip()]
    return ", ".join(sorted(tags))
```

> [!WARNING]
> `Evaluate`는 `exec()`로 임의의 Python 코드를 실행합니다. 신뢰할 수 있는 코드만 사용하세요.

## 설치

ComfyUI Manager에서 **ComfyUI-Evaluate-Pack**을 검색하거나:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/alchemine/comfyui-evaluate-pack
```

## 노드 (`EvaluatePack/Evaluate`)

**Evaluate** — 사용자 정의 Python 코드를 입력 문자열에 적용해 변환된 결과를 반환합니다.

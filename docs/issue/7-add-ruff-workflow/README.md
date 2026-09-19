# #7 Add ruff workflow

## 이슈
- GitHub Actions에 ruff 검사가 없다.
- `pyproject.toml`에 의존성 선언이 남아 있다.

## 해결책
- `.github/workflows/ruff.yml`을 추가한다. `ruff check .`와 `ruff format --check .`를 실행한다.
- `pyproject.toml`에 `[tool.ruff]` 설정을 추가한다.
- `pyproject.toml`에서 `dependencies`를 지운다. 의존성은 `requirements.txt`에만 적는다.
- `exec`는 노드의 기능이므로 해당 줄에 `# noqa: S102`를 붙인다. `ruff format`으로 1개 파일의 형식을 맞춘다.
- 버전을 1.0.1로 올린다.

## 테스트 계획
| 테스트 | 기대 결과 |
|---|---|
| `ruff check .` | `All checks passed!` |
| `ruff format --check .` | 다시 형식을 맞출 파일이 없다 |

## 테스트 결과
### 수정 전
```
nodes/evaluate.py:40:9: S102 Use of `exec` detected
nodes/evaluate.py:87:9: S102 Use of `exec` detected
Found 2 errors.
Would reformat: nodes/lib/utils.py
1 file would be reformatted, 7 files already formatted
```

### 수정 후
```
All checks passed!
8 files already formatted
```

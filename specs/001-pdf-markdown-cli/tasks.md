# Tasks: PDF to Markdown CLI Tool

**Input**: Design documents from `/specs/001-pdf-markdown-cli/`
**Prerequisites**: plan.md (required), research.md, data-model.md, quickstart.md

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root

## Phase 3.1: Setup
- [ ] T001 Create project structure: `src/` and `tests/` directories in the repository root.
- [ ] T002 Initialize Python project: Create `requirements.txt` and add `markitdown`, `click`, `google-generativeai`, and `pytest`.
- [ ] T003 [P] Configure linting: Set up `flake8` with a `.flake8` file and `black` via `pyproject.toml`.

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T004 [P] Create failing test for PDF conversion in `tests/test_converter.py`. It should assert that a PDF is converted to a raw Markdown string.
- [ ] T005 [P] Create failing test for Gemini post-processing in `tests/test_post_processor.py`. It should assert that a raw Markdown string is refined.
- [ ] T006 [P] Create failing end-to-end CLI test in `tests/test_cli.py`. It should check if a PDF input produces a refined Markdown file.

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T007 Implement core conversion logic in `src/converter.py` using the `markitdown` library to convert a PDF path to a raw Markdown string.
- [ ] T008 Implement Gemini post-processing in `src/post_processor.py` to take a raw Markdown string and return a refined version.
- [ ] T009 Implement the CLI entry point in `src/main.py` using `click` to orchestrate the conversion and post-processing.

## Phase 3.4: Integration
- [ ] T010 Ensure `src/main.py` correctly handles file I/O and module orchestration.

## Phase 3.5: Polish
- [ ] T011 [P] Add unit tests for any utility functions and edge cases.
- [ ] T012 [P] Add comprehensive docstrings to all functions and modules.
- [ ] T013 Create a `README.md` with installation and usage instructions.

## Dependencies
- T001, T002, T003 must be done first.
- Tests (T004-T006) must be completed before implementation (T007-T009).
- T007 is a dependency for T009.
- T008 is a dependency for T009.

## Parallel Example
```
# The following test creation tasks can run in parallel:
/execute_task T004
/execute_task T005
/execute_task T006
```

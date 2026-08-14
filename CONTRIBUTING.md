# Contributing Guidelines

Thanks for contributing to this repository 🎉  
To keep collaboration smooth and code quality high, please follow these guidelines.

## Branching & Pull Requests

- Do **not** commit directly to `main`.
- Create a feature/fix/docs branch from `main`, for example:
  - `feature/<short-description>`
  - `fix/<short-description>`
  - `docs/<short-description>`
- Open a Pull Request (PR) into `main`.
- PRs must be reviewed and approved before merge (as enforced by branch protection).

## Commit Messages

Use clear, descriptive commit messages. Conventional-style prefixes are recommended:

- `feat: add binary search challenge`
- `fix: correct edge case in palindrome solution`
- `docs: update setup instructions`
- `test: add unit tests for sorting utility`
- `chore: clean up lint config`

## Code Quality Expectations

Before requesting review:

- Keep PRs focused and reasonably small.
- Add or update tests for behavior changes.
- Update documentation when behavior, setup, or usage changes.
- Remove dead/commented-out code.
- Ensure code is readable and consistent with existing style.

## Pull Request Checklist

Before marking PR as ready for review, confirm:

- [ ] I rebased/updated my branch from `main`
- [ ] I tested my changes locally
- [ ] I added or updated tests where needed
- [ ] I updated docs where needed
- [ ] I linked the related issue (`Closes #<issue-number>` when applicable)
- [ ] I completed the PR template

## Suggested Workflow

1. Sync latest `main`
2. Create a new branch
3. Commit incremental, meaningful changes
4. Push branch and open PR
5. Request review / wait for CODEOWNERS review
6. Address feedback
7. Merge after approval and required checks pass

## Need Help?

If you are unsure about implementation details, open a **Draft PR** early and ask for feedback.

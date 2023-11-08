# Description

Please include a summary of the changes and features. Please also include relevant motivation and context. List any dependencies that are required for this change.

If you have not checked any of the lists below explain why here.

## Type of change

Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Technical Enhancements

# Checklist:

If any of these are not completed, please explain why in the notes.

## **Definition of Done**
**Code and merges**

- [ ] Code to be commented on where applicable 
- [ ] Documentation updated where required 
- [ ] Have considered non-functional requirements such as Security, Performance, Scalability, and Fault Tolerance
- [ ] I have linted the code

**Testing**

- [ ] All levels of acceptance test are passing (automated, integration, manual, accessibility, etc.)
- [ ] I have run the behave command to check the selenium behaviour tests pass locally
- [ ] Acceptance criteria met

**Other Checks**
- [ ] I have performed a self-review of my own code
- [ ] I have checked for spelling errors
- [ ] I have commented on my code, particularly in hard-to-understand areas
- [ ] My changes don't break anything unexpected
- [ ] I have checked and updated the security.txt file where required
- [ ] Up to date with the main branch
- [ ] I have a commit with the fix:, feat or BREAKING_CHANGE: tags (or other relevant tag) and will copy this commit message to the squash
commit message

Note when merging, squash commit must begin with one of the following tags:
"BREAKING CHANGE", "feat", "fix", "perf", "build", "chore", "ci", "docs", "style", "refactor", "test"

Usage

build: Changes that affect the build system or external dependencies (e.g Pyproject)

ci: Changes to our CI configuration files and scripts (Concourse)

docs: Documentation only changes

feat: A new feature
    E.G feat: adding method x to future methods table

fix: A bug fix
    E.G fix: amending page for method x to show correct release version

perf: A code change that improves performance
    E.G perf: amending issue on page x which impacted load times

BREAKING CHANGE: any change that breaks current functionality and may cause compatibility errors to users upgrading
    E.G BREAKING CHANGE: refactored method x to take variable y as input (changed from variable z)

refactor: A code change that neither fixes a bug nor adds a feature

test: Adding missing tests or correcting existing tests

chore: A task that has to be done on a regular basis that may or may not be automated, (E.G AXE test reports)

style: A change to amend code styling (black, pylint, flake8)

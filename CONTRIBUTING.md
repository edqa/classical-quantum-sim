
**3. `CONTRIBUTING.md`**

This file provides guidelines for potential contributors.

**File:** `classical_quantum_sim_project/CONTRIBUTING.md`

```markdown
# Contributing to Classical Quantum Simulation

First off, thank you for considering contributing! This project is experimental, and community involvement is crucial for exploring its potential and limitations.

We welcome contributions of all kinds, from reporting bugs and suggesting features to writing code, tests, and documentation.

## How Can I Contribute?

### Reporting Bugs

*   **Check Existing Issues:** Before submitting a new bug report, please check the [GitHub Issues](https://github.com/edqa/classical-quantum-sim/issues) to see if the problem has already been reported.
*   **Provide Details:** If you find a new bug, please open an issue and include:
    *   A clear and descriptive title.
    *   Steps to reproduce the bug.
    *   What you expected to happen.
    *   What actually happened (including any error messages or tracebacks).
    *   Your environment details (Python version, OS).

### Suggesting Enhancements or Features

*   Open an issue on the [GitHub Issues](https://github.com/edqa/classical-quantum-sim/issues) tracker.
*   Provide a clear description of the proposed feature and explain why it would be valuable.
*   Discuss potential implementation ideas if you have them.

### Contributing Code

1.  **Fork the Repository:** Click the "Fork" button on the [main repository page](https://github.com/edqa/classical-quantum-sim). This creates your own copy of the project.
2.  **Clone Your Fork:** Clone your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/classical-quantum-sim.git
    cd classical-quantum-sim
    ```
3.  **Install for Development:** Install the package in editable mode, preferably in a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
    pip install -e .[dev] # Installs package + dev tools like pytest, black (if defined in pyproject.toml)
    ```
4.  **Create a Branch:** Create a new branch for your changes, naming it descriptively (e.g., `feat/add-cnot-gate`, `fix/measurement-bug`):
    ```bash
    git checkout -b name-of-your-branch
    ```
5.  **Make Your Changes:** Write your code, tests, and documentation.
    *   **Code Style:** Try to follow PEP 8 guidelines. Consider using a formatter like `black` (`black .`) for consistency.
    *   **Tests:** Add unit tests for new functionality in the `tests/` directory using `pytest`. Ensure existing tests pass (`pytest`).
    *   **Documentation:** Update the README or add docstrings if necessary.
6.  **Commit Your Changes:** Make small, logical commits with clear messages:
    ```bash
    git add .
    git commit -m "FEAT: Implement simulated CNOT gate"
    ```
7.  **Push to Your Fork:** Push your changes to your forked repository on GitHub:
    ```bash
    git push origin name-of-your-branch
    ```
8.  **Submit a Pull Request (PR):**
    *   Go to your fork on GitHub.
    *   Click the "Compare & pull request" button for your new branch.
    *   Provide a clear title and description for your PR, explaining the changes you made. Reference any relevant issues (e.g., "Closes #12").
    *   Submit the PR. Project maintainers will review your changes.

## Development Setup Notes

*   Using a virtual environment is highly recommended.
*   Install development dependencies using `pip install -e .[dev]` if the `[project.optional-dependencies]` section is defined in `pyproject.toml`.
*   Run tests using `pytest` from the project root directory.

Thank you again for your interest in contributing!
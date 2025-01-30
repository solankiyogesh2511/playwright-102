# playwright-python-framework

Created Playwright Framework using (Python, playwright, PyTest, HTML Reports)
Please follow below steps for framework understanding
https://www.lambdatest.com/support/docs/python-with-playwright/

## Features
- URL :  https://www.lambdatest.com/selenium-playground p
- test_Scenario1 : Test to validate interaction with Simple Form Demo on LambdaTest Playground.
- test_Scenario2 2: Test to Drag & Drop Sliders on LambdaTest Playground.
- test_Scenario3 3: Test to validate Input Form Submit on LambdaTest Playground.

## Installation

### Prerequisites
- Python 3.x
- Poetry
- Pytest
- Playwright

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/solankiyogesh2511/Playwright-lambda-101
   cd project
   ```

2. Install dependencies using Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   export PATH="$HOME/.local/bin:$PATH"
   poetry install
   ```

3. Install Pytest:
   ```bash
   poetry add pytest
   ```

4. Install additional Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up Playwright:
   ```bash
   playwright install-deps
   playwright install
   ```

## Usage

### Run Tests
Run Python tests using Poetry:
```bash
poetry run pytest
```

Run Playwright tests:
```bash
pytest
```
Run Parallel Playwright tests:
```bash
pytest --numprocesses 3
```
## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

## License

This project is licensed under the yogesh solanki License. See the `LICENSE` file for details.

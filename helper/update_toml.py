import toml

def update_pyproject_from_requirements(pyproject_path, requirements_path):
    # Read `requirements.txt`
    with open(requirements_path, 'r') as req_file:
        requirements = req_file.readlines()
    
    dependencies = {}
    for line in requirements:
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # Skip empty lines and comments
        if "==" in line:
            pkg, version = line.split("==")
            dependencies[pkg] = version
        else:
            dependencies[line] = "*"

    # Load `pyproject.toml`
    with open(pyproject_path, 'r') as py_file:
        pyproject = toml.load(py_file)
    
    # Update dependencies in `pyproject.toml`
    if "tool" not in pyproject:
        pyproject["tool"] = {}
    if "poetry" not in pyproject["tool"]:
        pyproject["tool"]["poetry"] = {}
    if "dependencies" not in pyproject["tool"]["poetry"]:
        pyproject["tool"]["poetry"]["dependencies"] = {}

    pyproject["tool"]["poetry"]["dependencies"].update(dependencies)

    # Write back the updated `pyproject.toml`
    with open(pyproject_path, 'w') as py_file:
        toml.dump(pyproject, py_file)

    print("Dependencies updated in pyproject.toml!")

# Example usage
update_pyproject_from_requirements("pyproject.toml", "requirements.txt")

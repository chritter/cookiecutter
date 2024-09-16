

import os

# Conditional File/Directory Removal:

REMOVE_PATHS = [
    '{% if cookiecutter.mode == "module_a" %}docs/module_b{% endif %}',
    '{% if cookiecutter.mode == "module_b" %}docs/module_a{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
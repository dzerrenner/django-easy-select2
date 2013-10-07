import os

from setuptools import setup, find_packages


data_files = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)


# this for cycle took from django-registration setup.py script
for dirpath, dirnames, filenames in os.walk('easy_select2'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if filenames:
        prefix = dirpath[13:] # Strip "easy_select2/" or "easy_select2\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(
    name = "django-easy-select2",
    version = "1.0.0",
    packages = find_packages(),
    author = "asyncee",
    description = "Django select2 theme for select input widgets.",
    license = "MIT",
    keywords = "django select2",

    package_dir={'easy_select2': 'easy_select2'},
    package_data={'easy_select2': data_files},
)
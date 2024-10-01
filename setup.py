from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in amr_library_management/__init__.py
from amr_library_management import __version__ as version

setup(
	name="amr_library_management",
	version=version,
	description="test",
	author="amr atef",
	author_email="amr@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

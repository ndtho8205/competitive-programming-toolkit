from pathlib import Path

from setuptools import setup

CURRENT_DIR = Path(__file__).parent

DESCRIPTION = "A simple toolkit to test your codes on a Competitive Programming."
README = (CURRENT_DIR / "README.md").read_text(encoding="utf-8")
VERSION = "0.1.0"

setup(
    name="cptool",
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author="Tho Nguyen",
    url="https://github.com/ndtho8205/competitive-programming-toolkit",
    python_requires=">=3.6.0",
    package_dir={"": "."},
    include_package_data=True,
    packages=["cptool", "cptool.*"],
    install_requires=["beautifulsoup4>=4.9.0", "ruamel.yaml>=0.16.10"],
    entry_points={"console_scripts": ["cptool = cptool.cli:main"]},
    zip_safe=False,
)

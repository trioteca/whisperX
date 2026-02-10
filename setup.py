import os
import platform

from setuptools import find_packages, setup

# Leer requirements.txt sin pkg_resources (obsoleto)
def parse_requirements(filename):
    """Lee el archivo requirements.txt y devuelve una lista de dependencias."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="whisperx",
    py_modules=["whisperx"],
    version="3.2.1",
    description="Time-Accurate Automatic Speech Recognition using Whisper.",
    readme="README.md",
    python_requires=">=3.8",
    author="Max Bain",
    url="https://github.com/m-bain/whisperx",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=parse_requirements("requirements.txt") + ["pyannote.audio==3.2.1"],
    entry_points={
        "console_scripts": ["whisperx=whisperx.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
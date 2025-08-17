#!/usr/bin/env python3
"""
UCP Package Setup - Ultra-Compressed Communication Protocol
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ucp-protocol",
    version="1.0.0",
    author="UCP Collective",
    author_email="contact@ucp-protocol.org", 
    description="AI reasoning enhancement through bias elimination and communication compression",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ucp-collective/ucp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research", 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies - pure Python implementation
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.910",
        ],
    },
    entry_points={
        "console_scripts": [
            "ucp=ucp_system:main",
            "ucp-demo=ucp_system:demonstrate_capability",
        ],
    },
    keywords="ai artificial-intelligence communication protocol bias-elimination reasoning-enhancement",
    project_urls={
        "Bug Reports": "https://github.com/ucp-collective/ucp/issues",
        "Source": "https://github.com/ucp-collective/ucp",
        "Documentation": "https://ucp-protocol.readthedocs.io",
        "Research": "https://arxiv.org/abs/xxxx.xxxxx",
    },
)
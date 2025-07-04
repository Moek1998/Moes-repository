from setuptools import setup, find_packages

setup(
    name="claude-code-squad",
    version="0.1.0",
    description="Claude Code and Claude Squad - Tools for working with Claude AI",
    author="Moe",
    author_email="moe@example.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "click>=8.0.0",
        "pydantic>=2.0.0",
        "anthropic>=0.7.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "claude-code=claude_code.cli:main",
            "claude-squad=claude_squad.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
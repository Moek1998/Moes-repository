#!/usr/bin/env python3
"""Initialize a project for LLM-based workflows."""
import argparse
import os
from pathlib import Path

TEMPLATE_REQUIREMENTS = [
    "boto3",
    "google-cloud-storage",
    "openai",
    "requests",
    "transformers",
    "torch",
]

PROJECT_DIRS = ["src", "workflows", "config", "db"]

CONFIG_TEMPLATE = """# Example configuration\nAWS_PROFILE=default\nGCP_PROJECT=your-project\nOPENAI_API_KEY=\n"""


def init_project():
    for d in PROJECT_DIRS:
        Path(d).mkdir(exist_ok=True)
    # requirements
    req_path = Path("requirements.txt")
    if not req_path.exists():
        req_path.write_text("\n".join(TEMPLATE_REQUIREMENTS) + "\n")
    # config template
    cfg = Path("config/.env.example")
    if not cfg.exists():
        cfg.write_text(CONFIG_TEMPLATE)
    print("Project initialized.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--init", action="store_true", help="create default project files")
    args = parser.parse_args()

    if args.init:
        init_project()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

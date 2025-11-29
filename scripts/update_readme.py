#!/usr/bin/env python3
"""
Minimal script to update README.md with dynamic GitHub stats.
Fetches basic stats using GitHub API and inserts them into README.
"""

import os
import re
from datetime import datetime

def update_readme_stats():
    """Update README with current timestamp and stats placeholders."""
    
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print(f"README.md not found at {readme_path}")
        return
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Add last updated timestamp (optional enhancement)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    
    # Insert or update a comment with last update time
    update_marker = f"<!-- Last updated: {timestamp} -->"
    
    # Check if marker exists, if so replace it
    if "<!-- Last updated:" in content:
        content = re.sub(
            r"<!-- Last updated:.*?-->",
            update_marker,
            content
        )
    else:
        # Add marker at the end
        content += f"\n\n{update_marker}\n"
    
    # Write updated content
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"README updated at {timestamp}")

if __name__ == "__main__":
    # GitHub token is automatically available in Actions via GITHUB_TOKEN
    # For advanced stats, use PyGithub:
    # from github import Github
    # g = Github(os.getenv('GITHUB_TOKEN'))
    # user = g.get_user('PrathmeshKushwaha')
    # repos = user.get_repos()
    # Process stats and insert into README
    
    update_readme_stats()

# vcs_integration.py
import subprocess

class VCSIntegration:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path

    def run_git_command(self, command):
        """
        Runs a git command in the specified repository.
        """
        try:
            result = subprocess.run(
                command.split(),
                cwd=self.repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if result.returncode == 0:
                return result.stdout.decode("utf-8")
            else:
                return result.stderr.decode("utf-8")
        except Exception as e:
            return str(e)

    def commit_changes(self, message="Auto-commit from AI assistant"):
        """
        Commits all changes in the repository with a message.
        """
        self.run_git_command("git add .")
        return self.run_git_command(f"git commit -m \"{message}\"")

    def create_branch(self, branch_name):
        """
        Creates a new Git branch.
        """
        return self.run_git_command(f"git checkout -b {branch_name}")

    def merge_branch(self, branch_name):
        """
        Merges the specified branch into the current branch.
        """
        return self.run_git_command(f"git merge {branch_name}")

    def push_changes(self, remote="origin", branch="main"):
        """
        Pushes the changes to the remote repository.
        """
        return self.run_git_command(f"git push {remote} {branch}")

    def pull_changes(self, remote="origin", branch="main"):
        """
        Pulls the latest changes from the remote repository.
        """
        return self.run_git_command(f"git pull {remote} {branch}")

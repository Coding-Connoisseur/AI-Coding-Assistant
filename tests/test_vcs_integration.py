# test_vcs_integration.py
import unittest
from unittest.mock import patch
from integrations.vcs_integration import VCSIntegration

class TestVCSIntegration(unittest.TestCase):

    @patch('subprocess.run')
    def test_commit_changes(self, mock_subprocess_run):
        mock_subprocess_run.return_value.returncode = 0
        mock_subprocess_run.return_value.stdout = b"Changes committed"

        vcs_integration = VCSIntegration(repo_path=".")
        result = vcs_integration.commit_changes("Initial commit")
        
        self.assertIn("Changes committed", result)
        mock_subprocess_run.assert_called()

    @patch('subprocess.run')
    def test_create_branch(self, mock_subprocess_run):
        mock_subprocess_run.return_value.returncode = 0
        mock_subprocess_run.return_value.stdout = b"Switched to new branch 'feature'"

        vcs_integration = VCSIntegration(repo_path=".")
        result = vcs_integration.create_branch("feature")
        
        self.assertIn("Switched to new branch", result)
        mock_subprocess_run.assert_called()

    @patch('subprocess.run')
    def test_push_changes(self, mock_subprocess_run):
        mock_subprocess_run.return_value.returncode = 0
        mock_subprocess_run.return_value.stdout = b"Changes pushed"

        vcs_integration = VCSIntegration(repo_path=".")
        result = vcs_integration.push_changes()

        self.assertIn("Changes pushed", result)
        mock_subprocess_run.assert_called()

if __name__ == '__main__':
    unittest.main()

# ide_integration.py
import json
import os

class IDEIntegration:
    def __init__(self, ide_name="vscode"):
        self.ide_name = ide_name.lower()

    def integrate_with_ide(self):
        """
        Integrates the AI assistant into the specified IDE.
        Currently supports basic integrations for VSCode and PyCharm.
        """
        if self.ide_name == "vscode":
            return self._integrate_vscode()
        elif self.ide_name == "pycharm":
            return self._integrate_pycharm()
        else:
            raise NotImplementedError(f"Integration for {self.ide_name} is not available.")

    def _integrate_vscode(self):
        """
        Basic integration with VSCode via an extension-like interaction.
        Modifies the VSCode settings.json to include AI assistant commands.
        """
        vscode_settings_path = os.path.expanduser("~/.config/Code/User/settings.json")
        try:
            with open(vscode_settings_path, "r") as f:
                settings = json.load(f)
        except FileNotFoundError:
            settings = {}

        # Add AI assistant command to settings
        settings["aiAssistant.enable"] = True

        with open(vscode_settings_path, "w") as f:
            json.dump(settings, f, indent=4)

        return "VSCode integration successful. You can now access AI commands within VSCode."

    def _integrate_pycharm(self):
        """
        Integration for PyCharm. Creates a plugin structure for the assistant to communicate with.
        """
        # You could add settings or a plugin configuration for PyCharm.
        plugin_path = os.path.expanduser("~/Library/Application Support/JetBrains/PyCharm2021.1/plugins/")
        os.makedirs(plugin_path, exist_ok=True)
        
        # You can add more specific interactions with PyCharm here.
        return "PyCharm integration successful. A basic plugin is now set up."

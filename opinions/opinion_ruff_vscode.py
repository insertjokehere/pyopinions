from . import Opinion

class RuffVSCodeOpinion(Opinion):
    def apply_changes(self):
        vscode_settings = self.project.get_json_file(".vscode/settings.json")
        
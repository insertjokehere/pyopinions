from . import Opinion


class RuffOpinion(Opinion):
    def apply_changes(self):
        ruff_tool = self.project.pyproject.get_or_create_table("tool", "ruff", is_super=True)
        ruff_tool["line-length"] = 120

        if "select" not in ruff_tool:
            ruff_tool["select"] = []

        for lint_rule in [
            "E4",
            "E7",
            "E9",
            "F",
            "UP",
            "S",
            "A",
            "I",
        ]:
            if lint_rule not in ruff_tool["select"]:
                ruff_tool["select"].append(lint_rule)

        self.project.pyproject.add_pytest_opt("--ruff")
        self.project.pyproject.add_pytest_opt("--ruff-format")

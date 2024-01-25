import os
from  pathlib import Path

from opinions import OpinionatedProject

def main():
    project = OpinionatedProject(Path(os.getcwd()))
    for opinion in project.opinions:
        opinion.apply_changes()
    result = project.finalize()
    if result:
        print("Project configured!")
    else:
        print("Nothing to do")
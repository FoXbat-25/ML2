from dataclasses import dataclass
import os

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    tested_file_path:str
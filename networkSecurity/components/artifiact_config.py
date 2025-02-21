from dataclasses import dataclass
import os

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    tested_file_path:str
@dataclass
class DataValidationArtifact:
    validationStatus:bool
    valid_train_data_path:str
    valid_test_data_path:str
    invalid_train_data_path:str
    invalid_test_data_path:str
    drift_report_path:str
    
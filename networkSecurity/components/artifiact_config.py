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
    
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str

@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float

@dataclass
class ModelTrainerArtifact:
    trained_model_path:str
    train_metric_artifact:ClassificationMetricArtifact
    test_metric_artifact:ClassificationMetricArtifact
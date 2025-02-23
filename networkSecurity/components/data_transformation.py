import sys
import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networkSecurity.components.constants import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS
from networkSecurity.components.config import DataTransformationConfg
from networkSecurity.components.artifiact_config import DataTransformationArtifact, DataValidationArtifact
from networkSecurity.components.exception import customException
from networkSecurity.utils.utils import *


class DataTransformation:
    def __init__(self, data_validation_artifact:DataValidationArtifact, data_transformation_confg:DataTransformationConfg):
        try:
            self.data_validation_artifact=data_validation_artifact
            self.data_transformation_confg=data_transformation_confg
        except Exception as e:
            raise customException(e,sys)

    def get_data_transformer_obj(cls)->Pipeline:
        try:
            imputer:KNNImputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            processor:Pipeline=Pipeline([('Imputer', imputer)])
            return processor
        except Exception as e:
            raise customException(e,sys)        

    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            train_df=pd.DataFrame(pd.read_csv(self.data_validation_artifact.valid_train_data_path))
            test_df=pd.DataFrame(pd.read_csv(self.data_validation_artifact.valid_test_data_path))

            input_train_features_df=train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_train_feature_df=train_df[TARGET_COLUMN]
            target_train_feature_df=target_train_feature_df.replace(-1, 0)

            input_test_features_df=test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_test_feature_df=test_df[TARGET_COLUMN]
            target_test_feature_df=target_test_feature_df.replace(-1, 0)

            preprocessor=self.get_data_transformer_obj()
            preprocessor_obj=preprocessor.fit(input_train_features_df)
            transformed_input_trained_feature=preprocessor_obj.transform(input_train_features_df)
            transformed_input_test_feature=preprocessor_obj.transform(input_test_features_df)

            train_arr=np.c_[transformed_input_trained_feature, np.array(target_train_feature_df)]
            test_arr=np.c_[transformed_input_test_feature, np.array(target_test_feature_df)]

            save_numpy_arr(self.data_transformation_confg.transformed_train_file_path, array=train_arr,)
            save_numpy_arr(self.data_transformation_confg.transformed_test_file_path, array=test_arr,)
            save_obj(self.data_transformation_confg.transformed_obj_file_path, preprocessor_obj,)

            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_confg.transformed_obj_file_path,
                transformed_train_file_path=self.data_transformation_confg.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_confg.transformed_test_file_path
            )
            return data_transformation_artifact
        except Exception as e:
            raise customException (e,sys)            



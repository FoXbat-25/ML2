import os
import sys
from networkSecurity.components.exception import customException
from networkSecurity.components.artifiact_config import DataTransformationArtifact, ModelTrainerArtifact
from networkSecurity.components.config import ModelTrainerConfg
from networkSecurity.utils.estimator import NetworkModel
from networkSecurity.utils.metrics import get_classification_score
from networkSecurity.utils.utils import save_obj, load_numpy_arr, load_obj, evaluate_models
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

class ModelTrainer:
    def __init__(self, model_trainer_confg:ModelTrainerConfg, data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_confg=model_trainer_confg
            self.data_transformation_artifact=data_transformation_artifact
        except Exception as e:
            raise customException(e, sys)

    def train_model(self, x_train, y_train, x_test, y_test):
        models={
            "Random Forest":RandomForestClassifier(verbose=1),
            "Decision Tree":DecisionTreeClassifier(),
            "Gradient Boosting":GradientBoostingClassifier(verbose=1),
            "Logistic Regression":LogisticRegression(verbose=1),
            "Adaboost":AdaBoostClassifier(),
            "KNN":KNeighborsClassifier(),
            "XGBoost":XGBClassifier()
        }
        params={
            "Decision Tree":{
                'criterion':['gini', 'entropy', 'log_loss']
            },
            "Random Forest":{'n_estimators':[8,16,32,64,128,256]},
            "Gradient Boosting":{'learning_rate':[0.1, 0.01, 0.05, 0.001],
                                 'n_estimators':[8,16,32,64,128,256]},
            "Logistic Regression":{},
            "Adaboost":{
                'learning_rate':[0.1 ,0.01, 0.05, 0.001],
                'n_estimators':[8,16,32,64,128,256]
            },
            "KNN":{},
            "XGBoost":{}
        }
        
        model_report:dict=evaluate_models(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test, models=models, params=params)
        best_model_score=max(sorted(model_report.values()))

        best_model_name=list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]

        best_model=models[best_model_name]
        y_train_pred=best_model.predict(x_train)

        classification_train_metric=get_classification_score(y_true=y_train, y_pred=y_train_pred)

        y_test_pred=best_model.predict(x_test)
        classification_test_metric=get_classification_score(y_true=y_test, y_pred=y_test_pred)

        preprocessor=load_obj(file_path=self.data_transformation_artifact.transformed_object_file_path)

        model_dir_path=os.path.dirname(self.model_trainer_confg.trained_model_path)
        os.makedirs(model_dir_path, exist_ok=True)

        Network_Model=NetworkModel(preprocessor=preprocessor, model=best_model)
        save_obj(self.model_trainer_confg.trained_model_path, obj=NetworkModel)

        model_trainer_artifact=ModelTrainerArtifact(trained_model_path=self.model_trainer_confg.trained_model_path, 
                                                    train_metric_artifact=classification_train_metric, 
                                                    test_metric_artifact=classification_test_metric)
        return model_trainer_artifact

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            train_file_path=self.data_transformation_artifact.transformed_train_file_path
            test_file_path=self.data_transformation_artifact.transformed_test_file_path
            train_arr=load_numpy_arr(train_file_path)
            test_arr=load_numpy_arr(test_file_path)

            x_train, y_train, x_test, y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            model_trainer_artifact=self.train_model(x_train, y_train, x_test, y_test)
            return model_trainer_artifact   
        
        except Exception as e:
            raise customException(e, sys)
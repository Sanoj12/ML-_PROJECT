import os
import sys

from dataclasses import dataclass

from catboost import CatBoostRegressor

from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)



from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score

from sklearn.neighbors import KNeighborsRegressor

from sklearn.tree import DecisionTreeRegressor

from xgboost import XGBRFRegressor


from src.exception import CustomException

from src.logger import logging



from src.utils import save_object,evaluate_model



@dataclass
class ModelTrainerConfig:

    trained_model_file_path = os.path.join('datasets',"model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    

    def initiate_model_trainer(self,train_array, test_array):


        try:

            logging.info("spliting training and test input data")


            X_train ,y_train ,X_test ,y_test = (
                
               train_array[:,:-1],
               train_array[:,-1],
               test_array[:,:-1],
               test_array[:,-1]
               
            
            )
        
            models = {
                "Random Forest":RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Linear Regresssion":LinearRegression(),
                "K-nieghbors classifier":KNeighborsRegressor(),
                "XGBclassifier":XGBRFRegressor(),
                "CatBoosting Classiifer":CatBoostRegressor(),
                "AdaBoost Regressor":AdaBoostRegressor(),

            }



            model_report =evaluate_model(X_train=X_train, y_train=y_train,
                                             
                             X_test=X_test,y_test= y_test, models=models)
            
            ##get  best model score from the dict using max- sorted method
            best_model_score = max(model_report.values())

            best_model_name = max(model_report,key=model_report.get)
            
            best_model = models[best_model_name]
            ##to get best model name from the dict

       

           

            if best_model_score < 0.6:
                raise CustomException("no best model found")
            
            logging.info(f" bestmodel found on both train and test data")

            

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )



            predicted = best_model.predict(X_test)

            r2_sqaure_score = r2_score(y_test,predicted)

            
            print(f"R2 Score: {r2_sqaure_score}")

            return r2_sqaure_score
     
     
        except Exception as e:

            raise CustomException (e,sys)
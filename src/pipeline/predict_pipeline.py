

import sys



import pandas as pd

from src.exception import CustomException

from src.utils import load_object



class PredictPipeline:
    def __init__(self):
        pass


    def predict(self,features):
       try:
          
          model_path = 'datasets/model.pkl'
          preprocessor_path = 'datasets/preprocessor.pkl'

          model = load_object(file_path = model_path)

          preprocessor = load_object(file_path = preprocessor_path)

          data_scaled = preprocessor.transform(features)

          pred =model.predict(data_scaled)


          return pred    
       
       except Exception as e:
        raise CustomException(e,sys)

class CustomData:
    def __init__(self,
                 Hours_Studied:int,
                 Previous_Scores:int,
                 Extracurricular_Activities:str,
                 Sleep_Hours:int,
                Sample_Question_Papers_Practiced:int
                ):
        
       self.Hours_Studied = Hours_Studied
       self.Previous_Scores = Previous_Scores

       self.Extracurricular_Activities = Extracurricular_Activities

       self.Sleep_Hours =Sleep_Hours
       self.Sample_Question_Papers_Practiced = Sample_Question_Papers_Practiced



       def get_data_as_dataframe(self):
             

          try: 
             custom_data_input_dict = {
                    "Hours Studied" : [self.Hours_Studied],
                  "Previous Scores" : [self.Previous_Scores],
                   "Extracurricular Activities" : [self.Extracurricular_Activities],
                  "Sleep Hours"  :  [self.Sleep_Hours],
                  "Sample Question PapersPracticed" : [self.Sample_Question_Papers_Practiced],
            }

             return pd.DataFrame(custom_data_input_dict)
          
          except Exception as e:
            raise CustomException(e,sys)

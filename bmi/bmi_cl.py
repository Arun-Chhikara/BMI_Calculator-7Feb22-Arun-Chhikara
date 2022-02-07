
import pandas as pd
class BMI:
    '''
    To find out the BMI of a person given its Gender, Hight and Weight:-
    a>. Use profile_bmi method to calculate the BMI of persons and also count of overweight persons
    b>. profile_bmi ouputs a tuble of a pandas dataframe and an integer. 
        i). Dataframe includes 3 new columns. One for BMI, second for risk and third for weight category
        ii). Integer is the number of overwight persion in the provided data
    c>. Use input_data attribute of instanciated BMI class to acccess the original data provided as input
    
    '''
    def __init__(self, data, height_col_name = 'HeightCm', weight_col_name = 'WeightKg'):
        self.input_data = pd.DataFrame(data)
        self.height_col_name = 'HeightCm'
        self.weight_col_name = 'WeightKg'
        self.bmi_profiles = pd.DataFrame({'BMI_Category':['Underweight','Normal Weight','Overweight','Moderately Obese','Severely Obese','Very Severely Obese'],'BMI-Lower-Range':[0,18.5,25,30,35,40],'BMI-Upper-Range':[18.4,24.9,29.9,34.9,39.9,1000],'Health Risk':['Malnutrion Risk','Low Risk','Enhanced Risk','Medium Risk','High Risk','Very High Risk']})

    def _bmi_(self,w,h):
        return w/((h/100)**2)
    
    def _profile_(self,bmi,bmi_profile_data):
        bmi['index'],bmi_profile_data['index'] = 1,1
        temp = bmi.merge(bmi_profile_data)
        temp['mask'] = temp.apply(lambda x: x['bmi'] >= x['BMI-Lower-Range'] and x['bmi'] <= x['BMI-Upper-Range'], axis = 1)
        return temp[temp['mask']].reset_index(drop = True).drop(columns = ['index','mask','BMI-Lower-Range','BMI-Upper-Range'])
    
    def _count_overweight_profiles_(self,profiled_bmi):
         try:
            count = profiled_bmi['BMI_Category'].value_counts()['Overweight']
            return count
         except KeyError:
            count = 0
            return count
    
    def profile_bmi(self):
        self.bmi_data_ = self.input_data.copy()
        self.bmi_data_['bmi'] = self.bmi_data_[[self.height_col_name,self.weight_col_name]].apply(lambda x: self._bmi_(x[self.weight_col_name],x[self.height_col_name]), axis = 1)
        profiled_bmi = self._profile_(self.bmi_data_, self.bmi_profiles)
        self.bmi_data_.drop(columns = 'index', inplace = True)
        overweights = self._count_overweight_profiles_(profiled_bmi)
        return profiled_bmi, overweights



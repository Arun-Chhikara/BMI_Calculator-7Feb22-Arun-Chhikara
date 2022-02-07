
import pandas as pd
from bmi import bmi_cl

data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

#data = pd.DataFrame(data)

bmi = bmi_cl.BMI(data)
profiles_data, cnt_overweight = bmi.profile_bmi()

if __name__ == "__main__":
    assert cnt_overweight == 1
    print('test ran successfully')


ranges1={
    "Glucose":{"Unit":"mg/dL","Min":70.0,"Max":100.0},
    "Cholesterol":{"Unit":"mg/dL","Min":125.0,"Max":200.0},
    "Hemoglobin":{"Unit":"g/dL","Min":13.5,"Max":17.5}, 
    "Creatinine":{"Unit":"mg/dL","Min":0.74,"Max":1.35},
    "TSH":{"Unit":"mIU/L","Min":0.5,"Max":4.5},
    "AST":{"Unit":"U/L","Min":10.0,"Max":40.0},
    "Vitamin D":{"Unit":"ng/mL","Min":30.0,"Max":100.0}}
advice1={
    "Glucose":{
        "High": "Reduce sugars and refined carbs, and increase physical activity. Consult your doctor.",
        "Low": "Eat small, regular meals with quick-absorbing sugars. Consult your doctor.",
        "Normal": "Maintain your healthy and balanced diet and exercise regularly."},
    "Cholesterol":{
        "High": "Avoid saturated and trans fats. Increase fiber intake (oats, legumes). Exercise regularly.",
        "Low": "Consult your doctor to evaluate the need for increasing healthy fats.",
        "Normal": "Continue your healthy lifestyle."},
    "Hemoglobin":{
        "High": "Increase water intake and consult your doctor to determine the cause.",
        "Low": "Eat iron-rich foods (red meat, spinach) and Vitamin C.",
        "Normal": "Excellent results! Maintain a varied diet."},
    "Creatinine":{
        "High": "Drink more water and reduce excessive animal protein intake. Consult your doctor.",
        "Low": "Usually not a concern, but consult a doctor to assess kidney function.",
        "Normal": "Kidney function is within normal limits. Stay hydrated."},
    "TSH":{  
        "High": "May indicate hypothyroidism. See an endocrinologist.",
        "Low": "May indicate hyperthyroidism. See an endocrinologist.",
        "Normal": "Thyroid function is good. Continue your healthy lifestyle."},
    "AST":{   
        "High": "Avoid alcohol and review medications. Consult your doctor to assess the cause of elevated liver enzymes.",
        "Low": "Low AST is generally not a concern.",
        "Normal": "Initial liver function is within the normal range."},
    "Vitamin D":{
        "High": "Stop supplements temporarily and check with your doctor. Very high levels can be harmful.",
        "Low": "Increase safe sun exposure and consider supplements after consulting your doctor.",
        "Normal": "Maintain your level with diet and sun exposure."}}

def loaddata():
    d={}
    for x,y in ranges1.items():
        d[x]=LabTestRef(x,y["Unit"],y["Min"],y["Max"])
    return d

class LabTestRef: 
    def __init__(self, n, u, minv, maxv):
        self.name=n
        self.unit=u
        self.minlimit=minv
        self.maxlimit=maxv

    def get_dict(self): 
        r={} 
        r["Test Name"]=self.name
        r["Unit"]= self.unit
        r["Min Limit"]= self.minlimit
        r["Max Limit"]= self.maxlimit
        return r

class TestResult:
    def __init__(self, test1: LabTestRef, v1: float):
        self.ref= test1
        self.value= v1

    def check(self): 
        v=self.value 
        m=self.ref.minlimit 
        x= self.ref.maxlimit 
        if v < m:
            s="low"
        elif v > x:
            s="high"
        else:
            s="normal"
        return s

    def mesage(self):
        s = self.check()
        if s== "normal":
            m = "The result is normal."
        elif s== "low":
            m= f"The result is below the minimum limit ({self.ref.minlimit} {self.ref.unit})." 
        else:
            m= f"The result is above the maximum limit ({self.ref.maxlimit} {self.ref.unit})."
        return m

    def advice(self):
        s=self.check()
        return advice1.get(self.ref.name, {}).get(s, "Consult your doctor.")

    def finalres(self):
        s=self.check()
        finalres ={}
        finalres["Test Name"]=self.ref.name
        finalres["Input Value"]=f"{self.value} {self.ref.unit}"
        finalres["Status"]= s
        finalres["Analysis"]=self.mesage()
        finalres["Advice"]=self.advice() 
        return finalres
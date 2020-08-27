# dictionaries

CustomerData={
    'Name': 'SAM', 'AGE':15,'ADDRESS':'Falastine St'
}

CustomerData['Name']='Ameer'
CustomerData['AGE']=17
CustomerData['ADDRESS']='Al-Mansour'
print(CustomerData.get('ADDRESS','ADDRESS Not Found'))
print(CustomerData.get('Name','Name Not Found'))
print(CustomerData.get('AGE','AGE Not Found'))

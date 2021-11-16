import pandas as pd 

my_dataset={
    'cars':["BMW","Ford","Volvo"],
    'passings':[3,7,2]
}

x=pd.DataFrame(my_dataset)

print(x)
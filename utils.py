from ucimlrepo import fetch_ucirepo


def load_data(target=None):
    # fetch dataset 
    data = fetch_ucirepo(id=242) 

    # data (as pandas dataframes) 
    X = data.data.features 
    y = data.data.targets 

    # replace feature and target names with descriptive names
    descriptive_feature_names = {}
    descriptive_target_names = {}

    for _, (name, role, descr) in data.variables[['name', 'role', 'description']].iterrows():
        if role == 'Feature':
            descriptive_feature_names[name] = descr.replace(" ", "_")
        if role == 'Target':
            descriptive_target_names[name] = descr.replace(" ", "_")

    X = X.rename(columns=descriptive_feature_names)
    y = y.rename(columns=descriptive_target_names)  
    
    # return dataset based on specified target
    if not target:
        return X, y
    
    if target == 'Heating_Load':
        y_heat = y.drop(columns='Cooling_Load')
        return X, y_heat
    
    if target == 'Cooling_Load':
        y_cool = y.drop(columns='Heating_Load')
        return X, y_cool
    
    if target not in ['Heating_Load', 'Cooling_Load']:
        print("No target found! Maybe a typo?")
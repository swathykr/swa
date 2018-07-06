people = {'John':3546,'Marie':38629,'gayathri':38539,'snophy':3887909,'sruthy':27389629}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])

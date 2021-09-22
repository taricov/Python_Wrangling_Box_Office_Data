import pandas as pd

box_office = pd.read_csv("box_office.csv", encoding='latin-1')

def wrangler(box_office):
    #drop duplicates:
    box_office = box_office.drop_duplicates()
    #rename box_office col:
    box_office = box_office.rename(columns={'box_office':'earnings'})
    #filter out the NA values:
    box_office = box_office[~ box_office['earnings'].isna()]
    #filter by year:
    box_office = box_office[box_office['year_release'] >= 1990]
    #change data type:
    box_office[['country', 'type_of_subject']] = box_office[['country', 'type_of_subject']].astype('category')
    #creating new col:
    box_office.loc[box_office['lead_actor_actress'] == box_office['lead_actor_actress'].isna(), 'lead_actor_actress_known'] = 'Flase'  
    box_office.loc[box_office['lead_actor_actress'] != box_office['lead_actor_actress'].isna(), 'lead_actor_actress_known'] = 'True'  
    #earnings processing:
    box_office['earnings'] = box_office['earnings']/1000
    #select important cols:
    box_office = box_office[['title', 'year_release', 'earnings', 'country', 'type_of_subject', 'lead_actor_actress', 'lead_actor_actress_known']]
    #sorting:
    box_office = box_office.sort_values(by='earnings', ascending=False)
    # displaying final results:
    display(box_office)

wrangler(box_office)
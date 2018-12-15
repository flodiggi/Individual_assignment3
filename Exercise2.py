#%%
#Using Github’s API, create a function that:
#• takes all repositories from your account
#• prints a short description of each repository, with its name, number
#of stars, main language, and url

#%%
import requests

def get_flo_repos():
    response = requests.get("https://api.github.com/users/flodiggi/repos")
    repos = response.json()
    dicti_description = {}
    for i in repos:
        description = "The repo " + str(i['name']) +  " has " + str(i['stargazers_count']) + " star(s), is mainly written in " + str(i['language']) +  " and can be found on: "+ str(i['html_url'])
        dicti_description[str(i['name'])] = description
    return dicti_description
#%%

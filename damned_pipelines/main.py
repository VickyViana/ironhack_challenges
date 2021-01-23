from modules.module import *


API_TOKEN = 'b4323de1f3d9b8b4a183db1fd598184dfd7524b1'  # API TOKEN (REMEMBER: do not push these to your repo)
USERNAME = 'VickyViana'  # USERNAME
BASE_URL = 'https://api.github.com/'
KEY = 'repos/'
OWNER = 'ta-data-mad/'
REPO = 'dataptmad1120/'
SEARCH = 'search/issues?q=repo:'+OWNER+REPO+'+type:pr+state:{}'
PULLS = 'pulls?page={}&per_page=100&state={}'
COMMITS = 'pulls/{}/commits'
STATE = 'open'


def main():
    pages(BASE_URL, SEARCH, STATE, USERNAME, API_TOKEN)
    df_pulls = get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    df_status1 = df_status(df_pulls, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)
    create_csv(df_status1, field_sort1, field_name1)



    #create_csv()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

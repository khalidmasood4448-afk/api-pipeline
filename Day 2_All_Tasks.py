import pandas as pd
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_api_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

try:

    # Task 1:

    posts = get_api_data(
    "https://jsonplaceholder.typicode.com/posts"
    )


    users = get_api_data(
    "https://jsonplaceholder.typicode.com/users"
    )


    # Convert data into DataFrames

    posts_df = pd.DataFrame(posts)
    users_df = pd.DataFrame(users)


    # Task 2: 

    merged_df = posts_df.merge(
        users_df[["id", "name", "email"]],
        left_on="userId",
        right_on="id",
        how="left"
    )


    # Task 3: 

    merged_df.to_csv("posts_with_authors.csv", index=False)

    print("Successfully saved posts_with_authors.csv")
    print(merged_df.head())


except Exception as e:

    # Task 4: 

    print("Error:", e)
    print("File was not saved.")
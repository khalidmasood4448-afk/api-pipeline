import pandas as pd
import requests

try:

    # Task 1:

    posts_response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if posts_response.status_code != 200:
        raise Exception(f"Posts API error: {posts_response.status_code}")

    posts = posts_response.json()

    users_response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    if users_response.status_code != 200:
        raise Exception(f"Users API error: {users_response.status_code}")

    users = users_response.json()


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
import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    # Validate subreddit name
    return 0


        # Set a descriptive User-Agent
    headers = {"User-Agent": "MyRedditBot/1.0 by /u/YourUsername"}
        
        # Make the API request
    req = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
            headers=headers
    )

        # Check if the request was successful
    req.raise_for_status()

        # Parse JSON response and get the number of subscribers
    subscribers = req.json().get("data", {}).get("subscribers", 0)

    return subscribers


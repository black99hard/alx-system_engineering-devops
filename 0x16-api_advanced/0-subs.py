import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    # Validate subreddit name
    if not isinstance(subreddit, str) or ' ' in subreddit:
        return 0

    try:
        # Set a custom User-Agent
        headers = {"User-Agent": "MyRedditBot/1.0 by /u/YourUsername"}

        # Make the API request
        req = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers=headers,
            allow_redirects=False  # Ensure not following redirects
        )

        # Check if the request was successful
        req.raise_for_status()

        # Parse JSON response and get the number of subscribers
        subscribers = req.json().get("data", {}).get("subscribers", 0)

        return subscribers

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., network issues)
        print(f"Error: {e}")
        return 0

    except (ValueError, KeyError):
        # Handle JSON parsing errors or missing keys
        print("Error parsing JSON response")
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(f"Number of subscribers for {subreddit}: {number_of_subscribers(subreddit)}")

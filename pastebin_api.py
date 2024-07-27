import requests

def create_paste(title, body_text, expiration='1M', public=False):
    """
    Creates a new PasteBin paste.

    Parameters:
    title (str): The title of the paste.
    body_text (str): The body text of the paste.
    expiration (str): Expiration period (e.g., '10M', '1H', '1D', '1W', '2W', '1M', '6M', '1Y', 'N').
    public (bool): Whether the paste is publicly listed.

    Returns:
    str: URL of the newly created paste if successful, None otherwise.
    """
    print("Creating a new PasteBin paste...")

    api_dev_key = 'fdd4mm5YI9wSsyfhQJgoiiGanuHi7a5l'  # Replace with your PasteBin API developer key
    api_paste_code = body_text
    api_paste_private = '0' if public else '1'
    api_paste_name = title
    api_paste_expire_date = expiration

    url = 'https://pastebin.com/api/api_post.php'
    data = {
        'api_dev_key': api_dev_key,
        'api_option': 'paste',
        'api_paste_code': api_paste_code,
        'api_paste_private': api_paste_private,
        'api_paste_name': api_paste_name,
        'api_paste_expire_date': api_paste_expire_date
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Paste created successfully.")
        return response.text
    else:
        print(f"Failed to create paste. Response code: {response.status_code}")
        return None

# Test the function
if __name__ == "__main__":
    url = create_paste("Test Title", "This is a test paste.", "10M", True)
    print(f"Paste URL: {url}")
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='pages')

@app.route('/', methods=['GET', 'POST'])
def display_profile():
    # Set the Discord API token
    token = 'PUT-YOUR-TOKEN-HERE'  # Replace it with your Discord API token

    if request.method == 'POST':
        # Get the user ID from the form submission
        user_id = request.form['user_id']

        # Make a request to the Discord API to get the user's public information
        headers = {
            'Authorization': f'Bot {token}'
        }
        r = requests.get(f'https://discord.com/api/users/{user_id}', headers=headers)
        user_info = r.json()

        # Extract the user's information from the response
        username = f"{user_info['username']}#{user_info['discriminator']}"
        avatar_hash = user_info['avatar']
        banner = user_info['banner']

        # Generate the URL for the user's avatar image
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png'

        # Get the banner hash from the user's public information
        banner_hash = banner

        # Generate the URL for the banner image
        if banner_hash:
            banner_url = f'https://cdn.discordapp.com/banners/{user_id}/{banner_hash}.png?size=1280'
        else:
            banner_url = "https://cdn.discordapp.com/attachments/1035656678579900467/1056217252447387780/image.png"
        print("id requested",username,avatar_hash,banner)
        return render_template('profile.html', username=username, avatar_url=avatar_url, banner_url=banner_url)
    print("index.html")
    return render_template('index.html')


if __name__ == '__main__':
	app.run()

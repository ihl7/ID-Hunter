import requests
from flask import Flask, render_template, request
from flask import Flask, render_template
from jinja2 import Template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def display_profile():
    # Set the Discord API token
    token = 'MTA1NjE5NDM0Nzg2OTE1NTM2MA.GAQCm_.YixOad7AByxE3JknYM9HtfiEo_iTHjDSH-qyNU'  # Replace with your Discord API token

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
        username = str(f"{user_info['username']}#{user_info['discriminator']}")
        avatar_hash = user_info['avatar']
        banner = user_info['banner']
        banner_url = "https://cdn.discordapp.com/attachments/1035656678579900467/1056217252447387780/image.png" 
        # Generate the URL for the user's avatar image
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png'

        # Get the banner hash from the user's public information
        banner_hash = banner
        if "None" in str(banner_hash):
            print("None")
        else:
            banner_url = f'https://cdn.discordapp.com/banners/{user_id}/{banner_hash}.png?size=1280'
            print(banner_hash)
        # Generate the URL for the banner image
        
        template = Template('''
            <html>
              <head>
                <title>Discord Profile</title>
                <style>
                  /* Style the container element */
                  .container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                  }

                  /* Style the card element */
                  .card {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
					padding: 20px;
					width: 400px; /* Adjust the width of the card /
					height: 500px; / Adjust the height of the card */
					background-color: #2f3136;
					border-radius: 10px;
					box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
					}
				  h1 {
					color: #ffffff;
					font-size: 32px;
					font-weight: bold;
					margin: 0;
					text-align: center;
				  }

				  /* Style the avatar image */
				  #avatar {
					width: 128px;
					height: 128px;
					border-radius: 50%;
					margin-bottom: 20px;
				  }

				  /* Style the username and discriminator elements */
				  #username {
					color: #ffffff;
					font-size: 24px;
					margin: 0;
				  }

				  #discriminator {
					color: #ffffff;
					font-size: 18px;
					margin: 0;
				  }

				  /* Style the banner image */
				  #banner {
					width: 100%;  /* Make the banner image span the full width of the card */
					height: 200px;  /* Adjust the height of the banner image */
					object-fit: cover;  /* Make the banner image cover the entire banner area */
				  }

				  /* Style the form element */
				  form {
					display: flex;
					flex-direction: column;
					align-items: center;
					width: 50%; /* Adjust the width of the form */
					}
				  input[type='text'] {
					width: 100%;  /* Make the text box span the full width of the form */
					padding: 12px 20px;
					margin: 8px 0;
					box-sizing: border-box;
					border: 1px solid #ccc;
					border-radius: 4px;
				  }

				  input[type='submit'] {
					width: 100%;  /* Make the button span the full width of the form */
					background-color: #4caf50;
					color: white;
					padding: 14px 20px;
					margin: 8px 0;
					border: none;
					border-radius: 4px;
					cursor: pointer;
				  }

				  input[type='submit']:hover {
					background-color: #45a049;
				  }
				</style>
			  </head>
			  <body style="background-color: #36393f;">  <!-- Set the background color of the page -->
				<!-- Add a container element to center the content on the page -->
                <h1>ID Digger</h1>
				<div class="container">
				  <!-- Add a form element to allow users to input a user ID -->
				  <form action="" method="post">
					<input type="text" placeholder="Enter user ID" name="user_id">
					<input type="submit" value="Get profile">
				  </form>
				  <!-- Add a card element to hold the user's information -->
				  <div class="card">
					<!-- Add a title element -->
					
					<!-- Add a banner image element -->
					<img id="banner" src="{{ banner_url }}" alt="Banner">
					<!-- Add an avatar image element -->
					<img id="avatar" src="{{ avatar_url }}" alt="Avatar">
					<!-- Add a username element -->
					<h2 id="username">{{ username }}</h2>
					<!-- Add a discriminator element -->
				  </div>
				</div>
			  </body>
			</html>
		''')
        return render_template(template,username=username, avatar_url=avatar_url, banner_url=banner_url)
    else:
        template = Template('''
			<html>
			  <head>
				<title>Discord Profile</title>
				<style>
				  /* Style the container element */
				  .container {
					display: flex;
					justify-content: center;
					align-items: center;
					height: 100vh;
				  }

				  /* Style the form element */
				  form {
					display: flex;
					flex-direction: column;
					align-items: center;
					width: 50%; 
					/* Adjust the width of the form */
					}
					              /* Style the text box and button */
              input[type='text'] {
                width: 100%;  /* Make the text box span the full width of the form */
                padding: 12px 20px;
                margin: 8px 0;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 4px;
              }

              input[type='submit'] {
                width: 100%;  /* Make the button span the full width of the form */
                background-color: #4caf50;
                color: white;
                padding: 14px 20px;
                margin: 8px 0;
                border: none;
                border-radius: 4px;
                cursor: pointer;
              }

              input[type='submit']:hover {
                background-color: #45a049;
              }
            </style>
          </head>
          <body style="background-color: #36393f;">  <!-- Set the background color of the page -->
            <!-- Add a container element to center the content on the page -->
            <div class="container">
              <!-- Add a form element to allow users to input a user ID -->
              <form action="" method="post">
                <input type="text" placeholder="Enter user ID" name="user_id">
                <input type="submit" value="Get profile">
              </form>
            </div>
          </body>
        </html>''')
        return render_template(template)
if __name__ == '__main__':
	app.run()


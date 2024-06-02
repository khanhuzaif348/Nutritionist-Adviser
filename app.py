import streamlit as st 
import google.generativeai as genai
import os 
from dotenv import load_dotenv
load_dotenv() # loading all environment variable
from PIL import Image



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt,image[0]])
    return response.text


def input_image_setup(uploaded_file):
    #  check for image upload or not
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {

                   
                "mime_type" : uploaded_file.type, # get the mime value of the uploaded file
                "data": bytes_data
        
            }
        ]
        return image_parts
    else :
              raise FileNotFoundError("No file uploaded")
    



## writing code for web view 

st.set_page_config(page_title ="Nutrition assistant app  ")


st.header("Nutrition assistant app")
uploaded_file  = st.file_uploader("choose an image...",type=["jpg","jpeg","png"])
image =""
if uploaded_file is not None: 
      image = Image.open(uploaded_file)
      st.image(image,caption="Uploaded Image.",use_column_width=True)
submit=st.button("Tell me about the total calories")      




input_prompt = """
you are an expert in nutritionist where you need to see the food items from the image
              and calculate the total calories, also provide the details of
              every food items with calories intake 
              in below format 
              1.Item 1 _ no of calories
              2. Item 2 - no of calorieds 
---
----

      Finally you can also mentiopn whether the food is healthy or not and and also
      mention the 
      percentage split of the ratio of carbohydrates,fats ,fibers ,sugar and other important 
      things required in our diet





      """
if submit : 
      image_data =input_image_setup(uploaded_file)
      response = get_gemini_response(input_prompt,image_data)
      st.header("The response is " )
      st.write(response)
    




import streamlit as st
import streamlit_authenticator as stauth

# Define the users, passwords, and cookie settings
users = ['user1', 'user2']
passwords = ['password1', 'password2']
names = ['User One', 'User Two']

# Create an authenticator object
authenticator = stauth.Authenticate(names, users, passwords, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

# Display the login form
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.write(f'Welcome {name}!')
    # Your main app code goes here
    st.title('Main Application')
    st.write('This is the main content of the application.')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

# Add a logout button
if authentication_status:
    if st.button('Logout'):
        authenticator.logout('main')
        st.experimental_rerun()







    

            
 




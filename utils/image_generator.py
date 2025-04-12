from openai import OpenAI
import requests

client = OpenAI()


def generate_image(prompt: str):
  print(f"Generating Logo!")
  response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1024x1024",
      quality="standard",
      n=1,
  )

  #print(response.data[0].url)
  image_url = response.data[0].url

  response = requests.get(image_url)

  if response.status_code == 200:
    with open("outputs/logo.png", "wb") as f:
      f.write(response.content)
      print("Logo image downloaded successfully.")
  else:
    print("Failed to download logo image. Status code:", response.status_code)

from openai import OpenAI

client = OpenAI()

resp = client.images.generate(
  model="dall-e-3",
  prompt="An older man sitting on sea otter, Giboni style.",
  n=1,
  style='vivid',
  size="1024x1024"
)

print(resp)
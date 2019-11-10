import torch
from torchvision import transforms, datasets, models
from PIL import Image
from pathlib import Path
import sys
import os
from gtts import gTTS
import mpg123
from torch.autograd import Variable

model = torch.load("wastemodel.pt")

loader = transforms.Compose([transforms.Resize(224), transforms.ToTensor()])

image = Image.open(Path("temp.jpg"))

image = loader(image).float()

image = Variable(image, requires_grad=True)

image = image.unsqueeze(0)

output = model(image)

print(output)
prediction = (int)(torch.max(output.data, 1)[1].numpy())
print(prediction)

if (prediction == 0):
    t ("Recycle that cardboard please!")
if (prediction == 1):
    t = "Recycle that glass please!"
if (prediction == 2):
    t = "Recycle that metal please!"
if (prediction == 3):
    t = ("Recycle that paper please!")
if (prediction == 4):
    t = ("Recycle that plastic please")
if (prediction ==5):
    t = "Throw that away!"

myobj = gTTS(text=t,lang='en',slow=False)

myobj.save("audiotemp.mp3")
os.system("mpg123 audiotemp.mp3")

os.remove("temp.jpg")

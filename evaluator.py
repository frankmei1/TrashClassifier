import torch
from torchvision import transforms, datasets, models
from pil import image
from pathlib import path
import sys

model = torch.load("wastemodel.pt")

model.batch_size = 1

transforms = transforms.compose([transforms.resize(224),
                                       transforms.totensor(),])

image = image.open('temp.jpg')

inp = transforms(image)

inp = inp.to(torch.device("cpu"))

inp = inp[none]

output = model(inp)

prediction = int(torch.max(output.data, 1)[1].numpy())
print(prediction)

if (prediction == 0):
    print ('cardboard')
if (prediction == 1):
    print ('glass')
if (prediction == 2):
    print ('metal')
if (prediction == 3):
    print ('paper')
if (prediction == 4):
    print('plastic')
if (prediction ==5):
    print('trash')

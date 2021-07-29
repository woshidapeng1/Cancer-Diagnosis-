#import torch
import torch
from PIL import Image
from torchvision import transforms


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Resize([224, 224]),
    transforms.ToTensor()])


def predict(image):
    model = torch.load('model.pkl', map_location='cpu')
    model.to(device)
    torch.no_grad()
    output = model(image)
    output = torch.softmax(output, dim=1)
    return output


def recognition():
    print("begin to recogition")
    test_img = Image.open('ISIC_0000013.jpg')
    trans_img = transform(test_img).unsqueeze(0)
    input_img = trans_img.to(device)
    result = predict(input_img)
    print(f'result:{result}')
    print(f'max:{torch.max(result, 1).indices[0]}')


if __name__ == "__main__":
    recognition()

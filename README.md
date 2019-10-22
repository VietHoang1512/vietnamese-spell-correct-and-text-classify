 # Vietnamese spell corrector and text classifier 

 ## Demo
 You have to download the model and data for the classifier in [model](https://drive.google.com/open?id=1PoZ39LpH1lOSLE_xNVJNc8ZkySFZN3O8) and put it to our folder
 
 Or the whole [project](https://drive.google.com/drive/folders/1EFoYtjXdUPGxrMoZKWRlW_iyGndnUpKS?usp=sharing)
 #### Windows
 
-Open your Command Prompt
```
>> cd <path to the folder which contains the app.py file>
>> pip install -r requirements.txt
>> set FLASK_ENV=development
>> flask run 
```
 Then take the address and open this link on your browser

## A/Spell corrector
- Data: 
  - [VNTC](https://github.com/duyvuleo/VNTC)     
  - [Wiki article](https://dumps.wikimedia.org/viwiki/latest/)      
- Prepocessing text, build the neural network and evaluate the accuracy:
  - [Train](https://drive.google.com/drive/folders/1L8chuTULzRwc0QSCcYiTd4R3D5vXGzte?usp=sharing)
   (I also have some trained models in this drive folder)
- Test the model:
  - Put your text to the add_noise.py file and it will return the corresponding noisy text
  - You can also edit that text like the way you want
  - Then put the noisy text to spell corrector program (on your browse) and see the result
   
 ##### This project was made by [Phan Việt Hoàng](https://www.facebook.com/hoang.phanviet.90)
 
 ## B/Text classifier
- Data: 
  - [VNTC](https://github.com/duyvuleo/VNTC)     
- Test the model:
  - Put the Vietnamese text to text classifier program (on your browse) and see the result
   
 ##### This project was made by [Lê Trọng Đức](https://www.facebook.com/TrongDucLe.HUST)
     
#### Many thanks to [Lê Mạnh Hùng](https://www.facebook.com/langtu.khongtuoi) for helping us to finish this project





 # Vietnamese spell corrector and text classifier 

 ## Demo
 You have to download the FULL model( including data) for the classifier in [model](https://drive.google.com/open?id=1PoZ39LpH1lOSLE_xNVJNc8ZkySFZN3O8) and put it to our folder
 
 Or the whole [project](https://drive.google.com/drive/folders/1EFoYtjXdUPGxrMoZKWRlW_iyGndnUpKS?usp=sharing)
 
 You also should take a look at our approach and implementation are presented in the Presentation.pptx 
 
 #### Windows
 

- Open your Command Prompt
```
>> cd <path to the folder which contains the app.py file>
>> pip install -r requirements.txt
>> set FLASK_ENV=development
>> flask run 
```
 Then take the address and open this link on your browser

## A/Spell corrector
- [Data](https://drive.google.com/drive/folders/1THy6bN6pwHEmRvLxfiGcW8dez5VwxzvG?usp=sharing): 
  - [VNTC](https://github.com/duyvuleo/VNTC)     
  - [Wiki article](https://dumps.wikimedia.org/viwiki/latest/)      
- Prepocess text, build the neural network and evaluate the accuracy:
  - [Training phase](https://github.com/KingLeo2000/Vietnamese-Spell-Correction)
- Test the model:
  - Put your text to the add_noise.py file and it will return the corresponding noisy text
  - You can also edit that text like the way you want
  - Then put the noisy text to spell corrector program (on your browser) and see the result
 - Result
 
 ![Picture2](https://user-images.githubusercontent.com/52401767/69839859-e4680d80-128b-11ea-827d-80edb0b959de.png)
  
 ## B/Text classifier
- Data: 
  - [VNTC](https://github.com/duyvuleo/VNTC)     
- Test the model:
  - Put the Vietnamese text to text classifier program (on your browser) and see the result
- Result

![Picture1](https://user-images.githubusercontent.com/52401767/69839826-c13d5e00-128b-11ea-84f2-61b9112a2058.png)
     
#### Many thanks to [Lê Mạnh Hùng](https://github.com/hungle00) for helping us to finish this project





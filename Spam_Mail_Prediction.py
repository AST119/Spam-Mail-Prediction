import pickle
import streamlit as st 

#loading the model
loaded_model=pickle.load(open("C:/Users/aadit/Machine Learning/Spam Mail Detection/spam_mail_model.sav",'rb'))
#Extracting features from input data
feature_extraction=pickle.load(open("C:/Users/aadit/Machine Learning/Spam Mail Detection/Feature_extraciton.sav",'rb'))

def Spam_Mail_Prediction(input_mail):
    # convert text to feature vectors
    input_mail_features=feature_extraction.transform(input_mail)
    
    # making predictions
    prediction=loaded_model.predict(input_mail_features)
    
    if(prediction[0]==1):
            return 'It is a ham mail.'
    else:
        return 'It is a spam mail.'

def main():
    
    #giving a title
    st.title('Spam Mail Prediction System')
    
    #taking input from user
    var=st.text_input("Enter Message Received in Mail")
    var=list(var)
        
    #code for prediction
    prediction=''
    if st.button('Predict'):
        prediction=Spam_Mail_Prediction(var)
    st.success(prediction)
    
if __name__=='__main__':
    main()
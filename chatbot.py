import pyttsx3
import speech_recognition as sr
import mysql.connector

engine = pyttsx3.init()  # object creation

""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 125)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


def speechtotext():
    r = sr.Recognizer()
    while (1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("Did you say " + MyText)
                engine.say(MyText)
                return MyText
            break

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")


def Kyc():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S@jha1234",
        database="chatbot"
    )
    engine.say("Hi There!!!")
    engine.say('what is your name?')
    engine.runAndWait()
    name = speechtotext()
    print(name)
    engine.say('what is your email-Id?')
    engine.runAndWait()
    email_Id = speechtotext()
    print(email_Id)
    engine.say('what is your address?')
    engine.runAndWait()
    address = speechtotext()
    print(address)
    engine.say('what is your Date Of Birth?')
    engine.runAndWait()
    DOB = speechtotext()
    print(DOB)
    engine.say('can you please let me know your pancard details ?')
    engine.say('Name As on your pancard ?')
    engine.runAndWait()
    name_pancard = speechtotext()
    print(name_pancard)
    engine.say('Pancard Number ?')
    engine.runAndWait()
    pan_no1 = speechtotext()
    pan_no2 = "".join(pan_no1)
    pan_no = int(pan_no2)
    print(pan_no)
    qry =" INSERT INTO user_data(name, email_Id, address, DOB, name_pancard, pancard_no) VALUES(%s, %s, %s, %s, %s, %s)"
    val = (name, email_Id, address, DOB, name_pancard, pan_no)
    mycursor = mydb.cursor()
    mycursor.execute(qry, val)
    mydb.commit()
    # data = {
    #     "name": name,
    #     "email_Id": email_Id,
    #     "address": address,
    #     "DOB": DOB,
    #     "name_pancard": name_pancard,
    #     "pancard_no": pan_no
    # }
    # print(data)
    # return data
    engine.stop()

# def check_connection_to_db():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="S@jha1234",
#         database="chatbot"
#     )
#     print(mydb)
#
# def ins_query_maker(a):
#     # mydb = mysql.connector.connect(
#     #     host="localhost",
#     #     user="root",
#     #     password="S@jha1234",
#     #     database="chatbot"
#     # )
#     keys = tuple(a)
#     dictsize = len(a)
#     sql = ''
#     for i in range(dictsize) :
#         if(type(a[keys[i]]).__name__ == 'str'):
#             sql += '\'' + str(a[keys[i]]) + '\''
#         else:
#             sql += str(a[keys[i]])
#         if(i< dictsize-1):
#             sql += ', '
#     query = "INSERT INTO user_data" + str(keys) + " VALUES (" + sql + ")"
#     mycursor = mydb.cursor()
#     mycursor.execute(query)
#     mydb.commit()


if __name__ == "__main__":
    Kyc()
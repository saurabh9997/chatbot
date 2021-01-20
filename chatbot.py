import pyttsx3
import speech_recognition as sr
import mysql.connector
import tensorflow as tf

engine = pyttsx3.init()
r = sr.Recognizer()

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
    while 1:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                engine.say("Did you say " + MyText)
                return MyText
            break

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")


def to_db(name, email_Id, address, DOB, name_pancard, pan_no):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S@jha1234",
        database="chatbot",
        auth_plugin='mysql_native_password'
    )
    engine.say('Adding it our database')
    engine.runAndWait()
    qry = " INSERT INTO user_data(name, email_Id, address, DOB, name_pancard, pancard_no) VALUES(%s, %s, %s, %s, %s, %s)"
    val = (name, email_Id, address, DOB, name_pancard, pan_no)
    mycursor = mydb.cursor()
    mycursor.execute(qry, val)
    mydb.commit()
    engine.say('Data Have been added to our database. Thanks!!!')
    engine.runAndWait()
    engine.stop()


def verify_user_data(name, email_Id, address, DOB, name_pancard, pan_no):
    engine.say("please verify data")
    engine.runAndWait()
    engine.say("your name is :-")
    engine.runAndWait()
    engine.say(name)
    engine.runAndWait()
    engine.say("your email-id is :-")
    engine.runAndWait()
    engine.say(email_Id)
    engine.runAndWait()
    engine.say("your address is :-")
    engine.runAndWait()
    engine.say(address)
    engine.runAndWait()
    engine.say("your Date Of Birth is :-")
    engine.runAndWait()
    engine.say(DOB)
    engine.runAndWait()
    engine.say("your name on pancard is :-")
    engine.runAndWait()
    engine.say(name_pancard)
    engine.runAndWait()
    engine.say("your pancard number is :-")
    engine.runAndWait()
    engine.say(pan_no)
    engine.runAndWait()
    engine.say("Is your data correct ?. Please Say Yes or No")
    engine.runAndWait()
    r = speechtotext()
    response = r.lower()
    if response == "yes":
        return True
    else:
        return False


def Kyc():
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
    print("your date of birth is:-" + DOB)
    engine.say('can you please let me know your pancard details ?')
    engine.say('Name As on your pancard ?')
    engine.runAndWait()
    name_pancard = speechtotext()
    print("name on pancard:" + name_pancard)
    engine.say('Pancard Number ?')
    engine.runAndWait()
    pan_no1 = speechtotext()
    pan_no = "".join(pan_no1)
    # pan_no = int(pan_no2)
    print("pancard number is:-" + pan_no)
    response_verify = verify_user_data(name, email_Id, address, DOB, name_pancard, pan_no)
    if response_verify:
        to_db(name, email_Id, address, DOB, name_pancard, pan_no)
    else:
        Kyc()
    engine.stop()


def generate_cibil_score():
    a = tf.random.uniform(shape=(), minval=650, maxval=900, dtype=tf.int32)
    cibil_score = a.numpy()
    print(type(cibil_score))
    engine.say("your cibil score is")
    engine.runAndWait()
    engine.say(cibil_score)
    engine.runAndWait()
    return cibil_score


def upload_bank_statement(cibil_score):
    in_range = tf.greater(cibil_score, 650)
    if in_range:
        engine.say('Please Upload Bank Statement of last 3 months')
        engine.runAndWait()
        total_transaction = tf.random.uniform(shape=(), minval=50000, maxval=1000000, dtype=tf.int64)
        engine.say(total_transaction.numpy())
        engine.runAndWait()
        engine.stop()
        return total_transaction.numpy()


def loan_not_applicable(cibil_score):
    in_range = tf.less(cibil_score, 650)
    if in_range:
        engine.say("your cibil score is less. So, No loan can be given. Thanks !!!")
        engine.runAndWait()
        engine.stop()


def case0(cibil_score, upload_docs):
    lower_tensor = tf.greater(cibil_score, 650)
    upper_tensor = tf.less(cibil_score, 750)
    in_range = tf.logical_and(lower_tensor, upper_tensor)
    if in_range:
        engine.say("can get 10,000 to 15,000 loan")
        engine.runAndWait()
        maximum_credit = tf.multiply(upload_docs, tf.divide(10, 100))
        max = maximum_credit.numpy()
        in_range = tf.less(max, 15000)
        if in_range:
            engine.say("Maximum loan amount you can get is:")
            engine.runAndWait()
            if max < 15000:
                engine.say(max)
                engine.runAndWait()
                tf.print(max)
                engine.stop()
            else:
                engine.say("15000")
                engine.runAndWait()
                tf.print("15000")
                engine.stop()
        else:
            engine.say("Maximum loan amount you can get is : 15000")
            engine.runAndWait()
            engine.stop()


def case1(cibil_score, upload_docs):
    lower_tensor = tf.greater(cibil_score, 750)
    upper_tensor = tf.less(cibil_score, 850)
    in_range = tf.logical_and(lower_tensor, upper_tensor)
    if in_range:
        engine.say("can get 25000 to 40000 loan")
        engine.runAndWait()
        minimum_credit = tf.multiply(upload_docs, tf.divide(20, 100))
        maximum_credit = tf.multiply(upload_docs, tf.divide(40, 100))
        max = maximum_credit.numpy()
        min = minimum_credit.numpy()
        in_max_range = tf.less(max, 40000)
        if in_max_range:
            engine.say("Minimum loan amount you can get is:")
            engine.runAndWait()
            if max < 40000:
                engine.say(min)
                engine.runAndWait()
                engine.say("Maximum loan amount you can get is:")
                engine.runAndWait()
                engine.say(max)
                engine.runAndWait()
                tf.print(max)
                engine.stop()
            else:
                engine.say("15000")
                engine.runAndWait()
                tf.print("15000")
                engine.stop()
        else:
            engine.say("Maximum loan amount you can get is : 40000")
            engine.runAndWait()
            tf.print("40000")
            engine.stop()


def case2(cibil_score, upload_docs):
    in_range = tf.greater(cibil_score, 850)
    if in_range:
        engine.say("can get 40000 to 80000 loan")
        engine.runAndWait()
        maximum_credit = tf.multiply(upload_docs, tf.divide(25, 100))
        max = maximum_credit.numpy()
        in_max_range = tf.less(max, 80000)
        if in_max_range:
            engine.say("Maximum loan amount you can get is:")
            engine.runAndWait()
            if max < 80000:
                engine.say(max)
                tf.print(max)
                engine.runAndWait()
                engine.stop()
            else:
                engine.say("80000")
                tf.print("80000")
                engine.runAndWait()
                engine.stop()
        else:
            engine.say("Maximum loan amount you can get is : 80000")
            engine.runAndWait()
            tf.print("80000")
            engine.stop()


def application():
    Kyc()
    b = generate_cibil_score()
    upload_docs = upload_bank_statement(b)
    """
    650<cibil<750 :- 10 to 15k loan
    750<cibil<850 :- 25 to 40k
    850 <cibil :- 40k to 80 k 
    """
    tf.switch_case(b, branch_fns={0: case0(b, upload_docs), 1: case1(b, upload_docs), 2: case2(b, upload_docs),
                                  3: loan_not_applicable(b)})

"""
To-do if want to process again in one go
issue :- not running in one go
"""
def process_again():
    engine.say("Want to do process again?")
    engine.runAndWait()
    r = speechtotext()
    if r.lower() == "yes":
        return True


if __name__ == "__main__":
    try:
        application()
    except TypeError:
        pass

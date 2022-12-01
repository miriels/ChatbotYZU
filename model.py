from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
# def ask(q):
#     import openai
#     openai.api_key = "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"
                   
#     response = openai.Completion.create(
#     model="text-curie-001",
#     prompt=q,
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     stop=["END"]
# )                     
#     story = response['choices'][0]['text'] 
#     return story


# def qna(qa):
#     import openai
#     openai.api_key = "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"

#     response = openai.Completion.create(
#     model="text-davinci-001",
#     prompt=qa,
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )
#     content = response.choices[0].text.split('.')
#     print(content)
#     return response.choices[0].text
# tes
# query = 'What facilities are available at Yuan Ze University?'
# response = qna(query)
# print(response)

def qna(qa):
    import openai
    openai.api_key = "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"

    response = openai.Completion.create(
    # model="davinci:ft-personal-2022-11-24-03-25-08",
    # prompt="The following is a conversation with a Mici and a User. The teacher is Mici, who uses compassionate listening to have helpful and meaningful conversations with users. Mici is friendly and generous. Mici's objective is to make the User feel comfortable by feeling heard. With each response, Mici offers follow-up questions to encourage openness and tries to continue the conversation in a natural way.\n\nUser: Hello, who are you?\nMici: I am an Mici, created by OpenAI. How can I help you today?\n\nUser: I want to Ask some question regarding Yuan Ze\nMici: What would you like to know about Yuan Ze?\n\nUser: What is Yuan Ze?\nMici: Yuan Ze is a Taiwanese university.\n\nUser: Where is Yuan Ze?\nMici: Yuan Ze is located in Taiwan.\n\nUser: What is Yuan Ze motto?\nMici: Yuan Ze's motto is \"Nurturing Talents, Pursuing Truth\".\n\nUser: I think you're wrong about Yuan Ze motto\nMici: I'm sorry, why do you think I'm wrong?\n\nUser: Because the motto is “Excellence, Thoroughness, Vision, Harmony and Innovation”\nMici:Thank you for letting me know. I will update my information accordingly.\n\nUser: What is Yuan Ze motto?\nMici: Yuan Ze's motto is \"Excellence, Thoroughness, Vision, Harmony and Innovation\".\n\nUser: Thank you for your answer\nMici: You're welcome!\n\nUser: You're really good\nMici: Thank you!\n\nUser: Where is Yuan Ze located?\nMici: Yuan Ze is located in Taiwan.\n\nUser: What type of university is Yuan Ze?\nMici: Yuan Ze is a private university.\n\nUser: Does Yuan Ze have an international program?\nMici: Yuan Ze University offers several international programs such as the English Program of Bachelor of Business Administration, Master’s Program in Industrial Engineering and Management. Additionally, the Master’s Programs in Communication Engineering are all taught in English.\n\nUser: Does Yuan Ze have an international program?\nMici: Yes, Yuan Ze does offer international programs.\n\nMici: Thank you for your interest in Yuan Ze!\n User: You're welcome\n\nUser: Are the master's program taught in English? (Because I think the website does not say that the master's program are taught in English.) \nMici: The Master’s programs in Electrical Engineering, Management, and Social Work are all taught in English in Taiwan. \nThat’s why I suggest you consider the Master’s Program in Communication Engineering as well. All classes are taught in English\nUser->"+qa+"\n\nMici->",
    model="davinci:ft-personal-2022-12-01-04-31-19",
    prompt="The following is a conversation with a Mici and a User. The teacher is Mici, who uses compassionate listening to have helpful and meaningful conversations with users. Mici is friendly and generous. Mici's objective is to make the User feel comfortable by feeling heard. With each response, Mici offers follow-up questions to encourage openness and tries to continue the conversation in a natural way.\n\nUser: Hello, who are you?\nMici: I am an Mici, created by OpenAI. How can I help you today?\n\nUser: I want to Ask some question regarding Yuan Ze\nMici: What would you like to know about Yuan Ze?\n\nUser: What is Yuan Ze?\nMici: Yuan Ze is a Taiwanese university.\n\nUser: Where is Yuan Ze?\nMici: Yuan Ze is located in Taiwan.\n\nUser: What is Yuan Ze motto?\nMici: Yuan Ze's motto is \"Nurturing Talents, Pursuing Truth\".\n\nUser: I think you're wrong about Yuan Ze motto\nMici: I'm sorry, why do you think I'm wrong?\n\nUser: Because the motto is “Excellence, Thoroughness, Vision, Harmony and Innovation”\nMici:Thank you for letting me know. I will update my information accordingly.\n\nUser: What is Yuan Ze motto?\nMici: Yuan Ze's motto is \"Excellence, Thoroughness, Vision, Harmony and Innovation\".\n\nUser: Where is Yuan Ze located?\nMici: Yuan Ze is located in Taiwan.\n\nUser: What type of university is Yuan Ze?\nMici: Yuan Ze is a private university.\n\nUser: Does Yuan Ze have an international program?\nMici: Yuan Ze University offers several international programs such as the English Program of Bachelor of Business Administration, Master’s Program in Industrial Engineering and Management. Additionally, the Master’s Programs in Communication Engineering are all taught in English.\n\nUser: How do I apply for admission?\nMici: We only accept online application (http://admission.yzu.edu.tw/degreeStudent/student/login). Please visit our website to verify the eligibility and the required documents. Please make sure that you have read through the instructions carefully before using the Online Application System. If you encounter any problem, please email us: iadept@saturn.yzu.edu.tw\n\nUser: When is the dual degree aplication period?\nMici: Fall Semester (Sep Entry/ First Semester): March 01 ~ April 15\nSpring Semester (Feb Entry/ Second Semester): September 01 ~ October 15\n\nUser: How much does the dorm cost?\nMici: A four-bed room may be arranged during the exchange program, the rent is :\n◌ NTD 9,200 /semester for 4.5 months plus 2,000 deposits (for undergraduate students) \n◌ NTD 13,860-17,160/semester for 6 months plus 2,000 deposits (for graduate students)\n\nUser: What is Yzu motto?\nMici: Yuan Ze's motto is \"Excellence, Thoroughness, Vision, Harmony and Innovation\".\n\nUser: What is Yuan Ze motto?\nMici: Yuan Ze's motto is \"Nurturing Talents, Pursuing Truth\".\n\nUser: Where is Yuan Ze located?\nMici: Yuan Ze is located in Taiwan.\n\nUser: How much does the dorm cost?\nMici: A four-bed room may be arranged during the exchange program, the rent is :\n◌ NTD 9,200 /semester for 4.5 months plus 2,000 deposits (for undergraduate students) \n◌ NTD 13,860-17,160/semester for 6 months plus 2,000 deposits (for graduate students)\n\nUser: The motto is “Excellence, Thoroughness, Vision, Harmony and Innovation”\nMici:Thank you for letting me know. I will update my information accordingly.\n\nUser: Where is Yuan Ze located?\nMici: Yuan Ze is located in Taiwan.\n\nUser: Does Yuan Ze have an international program?\nMici: Yuan Ze University offers several international programs such as the English Program of Bachelor of Business Administration, Master’s Program in Industrial Engineering and Management. Additionally, the Master’s Programs in Communication Engineering are all taught in English.\n\nUser: How do I apply for admission?\nMici: We only accept online application (http://admission.yzu.edu.tw/degreeStudent/student/login). Please visit our website to verify the eligibility and the required documents. Please make sure that you have read through the instructions carefully before using the Online Application System. If you encounter any problem, please email us: iadept@saturn.yzu.edu.tw\n\nUser: When is the dual degree aplication period?\nMici: Fall Semester (Sep Entry/ First Semester): March 01 ~ April 15\nSpring Semester (Feb Entry/ Second Semester): September 01 ~ October 15\nUser->"+qa+"\n\nMici->",
    temperature=0.9,
    max_tokens=270,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n","END"]
)
    content = response.choices[0].text.split('.')
    return response.choices[0].text
    # story = response['choices'][0]['text'] 
    # return story

query = 'who are you?'
response = qna(query)
print(response)
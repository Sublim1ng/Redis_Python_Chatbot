# Redis_Python_Chatbot
## Part 1: Build the Chatbot
1. I created a .yml file to create both Redis and Python containers and the connection between them.
2. run docker-compose up in the terminal and exec redis-cli and python bash. (See the screenshots below.)
<img width="573" alt="compose up" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/07e4c45a-9145-4050-a130-75820432e7ba">
<img width="569" alt="exec redis" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/fcfaa445-8462-4c09-9a5e-ab8be3f766cd">
<img width="572" alt="exec python" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/98e98f4e-bb6f-4a25-a2fe-f754ca22401d">

## Part 2: Write the run Chatbot.py file 

I define a chatbot class with the .py file with all the functions inside. <br> 
Something interesting here is to write the Redis command in Python. <br>
After running the .py file, it will return a fuction list. (See the photo below) <br>
You can always use "!help" to call the list.
<img width="543" alt="!help" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/16027201-5c6e-4c81-a25f-1f9ce1dcb78b">

## Part 3: Demonstration of the use of the chatbot

I use the **"MONITOR"** command in Redis to see the interaction in real-time. <br>
<img width="186" alt="Monitor OK" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/addcd601-1ff7-499c-9f97-5e8ab117b43c">

**In this demonstration, I will attach both Python outputs and "Monitor" outputs.**

**1. Add User** <br>
The first input of the bot is the personal information, asking for name, age, gender, and location.
<img width="472" alt="add user" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/144d53f2-e6de-42cc-99a6-b01b2e962283">
<img width="573" alt="Monitor Add user" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/25122296-a5b8-4882-9eb0-321bd1ff788e">

**2. Fun Fact** <br>
The **!fact** command retrive a random fun fact stored in the database. We can edit the database at any time. <br>
<img width="567" alt="!fact" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/667cdd5d-886d-4066-a9c6-c5761661290a">
<img width="509" alt="monitor fact" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/eb6e2d82-dc6b-496c-9b91-a2d6d46b6942">

**3. Weather** <br>
The **!weather <city>** command retrive the weather condition of the city. An example input is "!weather nashville".
<img width="250" alt="!weather nashville" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/33595636-5e48-4659-98c5-2a1234e6130d"> <br>
<img width="526" alt="monitor weather" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/1e22a1cb-987e-4d9f-b4c4-c06807738aab">

**4. Whoami** <br>
The **!whoami** command gets all the personal information about the user.
<img width="505" alt="whoami" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/20ce4888-508d-4f2a-9377-d060a766dd2e">
<img width="444" alt="monitor whoami" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/3dbc061e-019d-4b4c-9ca3-a2be557ef794">

**5. Join and Leave** <br>
The **!join** and **!leave** commands allow you to subscribe or unsubscribe a channel in Redis.
<img width="234" alt="join and leave " src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/8492b589-b44d-4a00-9a1a-94ff3a2b3fc3"> <br>
<img width="435" alt="monitor join and leave" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/cfd7c946-b36d-449f-911a-d5aac2b04442">

**6. listen and send** <br> 
The **!listen"** and **"send"** commands allow you to read or send messages in a specific Redis channel. <br>
Here I publish a sentence in the "sports" channel to see how the "!listen" works. <br>
<img width="453" alt="input listen" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/3f27ff43-98dd-4a1c-a5b9-98e29bde16bc"> <br>
*listen* <br>
<img width="326" alt="!listen" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/a73b7334-5acd-4971-a70b-df0eb2293c53">
<img width="558" alt="monitor send" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/b19099ca-9139-4d16-b66f-93866198eda7"> <br>
*send* <br>
<img width="441" alt="send" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/cc528b05-4b4a-4732-b850-0576ae6662c3">
<img width="558" alt="monitor send" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/1b45a2cf-4762-480f-abc7-57e1960107a2">





















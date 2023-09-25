# Redis_Python_Chatbot
## Part 1: Activate Redis and Python
1. I structure a .yml file to create both Redis and Python containers and their connection. <br>
2. Run docker-compose up in the terminal and exec redis-cli and python bash. (See the screenshots below.)
<img width="573" alt="compose up" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/07e4c45a-9145-4050-a130-75820432e7ba">
<img width="569" alt="exec redis" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/fcfaa445-8462-4c09-9a5e-ab8be3f766cd">
<img width="572" alt="exec python" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/98e98f4e-bb6f-4a25-a2fe-f754ca22401d">

## Part 2: Write and run Chatbot.py file 

I define a chatbot class in the .py file with all the functions inside. <br> 
Something interesting here is to write the Redis command in Python. <br>
After running the .py file, it will return a function list. (See the photo below) <br>
You can always use "!help" to call the list. <br>
<img width="543" alt="!help" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/16027201-5c6e-4c81-a25f-1f9ce1dcb78b">

## Part 3: Demonstration of the use of the Chatbot

I use the **"MONITOR"** command in Redis to see the interaction in real-time. <br>
<img width="186" alt="Monitor OK" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/addcd601-1ff7-499c-9f97-5e8ab117b43c">

**I will attach both Python and "Monitor" outputs in this demonstration.**

**1. Add User** <br>
The first input of the bot is personal information, asking for name, age, gender, and location.
<img width="472" alt="add user" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/144d53f2-e6de-42cc-99a6-b01b2e962283">
<img width="573" alt="Monitor Add user" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/25122296-a5b8-4882-9eb0-321bd1ff788e">

**2. Fun Fact** <br>
The **!fact** command retrieves a random fun fact stored in the database. We can edit the database at any time. <br>
<img width="567" alt="!fact" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/667cdd5d-886d-4066-a9c6-c5761661290a">
<img width="509" alt="monitor fact" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/eb6e2d82-dc6b-496c-9b91-a2d6d46b6942">

**3. Weather** <br>
The **!weather <city>** command retrieves the weather condition of the city. An example input is "!weather nashville".
<img width="250" alt="!weather nashville" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/33595636-5e48-4659-98c5-2a1234e6130d"> <br>
<img width="526" alt="monitor weather" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/1e22a1cb-987e-4d9f-b4c4-c06807738aab">

**4. Whoami** <br>
The **!whoami** command gets all the personal information about the user.
<img width="505" alt="whoami" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/20ce4888-508d-4f2a-9377-d060a766dd2e">
<img width="444" alt="monitor whoami" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/3dbc061e-019d-4b4c-9ca3-a2be557ef794">

**5. Join and Leave** <br>
The **!join** and **!leave** commands allow you to subscribe or unsubscribe to a channel in Redis.
<img width="234" alt="join and leave " src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/8492b589-b44d-4a00-9a1a-94ff3a2b3fc3"> <br>
<img width="435" alt="monitor join and leave" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/cfd7c946-b36d-449f-911a-d5aac2b04442">

**6. listen and Send** <br> 
The **!listen"** and **"send"** commands allow you to read or send messages in a specific Redis channel. <br>
I publish a sentence in the "sports" channel to see how the "!listen" works. <br>
<img width="453" alt="input listen" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/3f27ff43-98dd-4a1c-a5b9-98e29bde16bc"> <br>
*listen* <br>
<img width="326" alt="!listen" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/ad45412a-ee5d-4cf1-8ae7-25f29a7febde">
*send* <br>
<img width="441" alt="send" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/cc528b05-4b4a-4732-b850-0576ae6662c3">
<img width="558" alt="monitor send" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/1b45a2cf-4762-480f-abc7-57e1960107a2">

**7. Direct Message** <br>
The **!dm** command allows the user to send a private message to someone else. <br>
<img width="315" alt="!dm" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/3c9be146-5594-4060-9122-2fbe664dfe4b"> <br>
<img width="564" alt="monitor dm" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/086ec85b-695e-453d-9f67-a5309485ec7b">

**8. Keys** <br>
The **!keys** command helps to list all the existing keys for checking. <br>
<img width="157" alt="!keys" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/d3c7cd23-6759-4e97-9ae4-e0eb457ff078"> <br>
<img width="352" alt="monitor keys" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/991ac8db-afbb-4cdf-a87d-0c6f2b66f569">

**9. EXIT and Non-existing commands**
**EXIT** allows users to quit the chatbot. If the user enters some unknown commands, the bot will still generate a response and ask for a new input. <br>
<img width="166" alt="other commands" src="https://github.com/Sublim1ng/Redis_Python_Chatbot/assets/111295538/94e4507c-a14a-40cd-949e-1b3fcd0191e9">

What I have mentioned above is all about my mini chatbot. I will upgrade and make more progress in the future!

























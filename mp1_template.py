import redis
import json
import random

class Chatbot:
    def __init__(self, host='redis', port=6379):
    # deine the chatbot and connect to redis
        self.redis = redis.StrictRedis(host=host, port=port)
        self.pubsub = self.redis.pubsub()
        self.username = None
    # create weather and fun facts manually
        self.weather_data_key = "weather_data"
        self.fun_facts_key = "fun_facts"
        self.redis.hset(self.weather_data_key, "nashville", "Sunny and hot.")
        self.redis.hset(self.weather_data_key, "chicago", "Rainy and cold.")
        self.redis.hset(self.weather_data_key, "iowa city", "Snowy and freezing.")
        self.redis.sadd(self.fun_facts_key, "The Eiffel Tower can be 15 cm taller during the summer due to the expansion of the iron structure in the heat.")
        self.redis.sadd(self.fun_facts_key, "Whales sleep upside down.")
        self.redis.sadd(self.fun_facts_key, "A day on Venus is longer than a year on Venus.")

    def introduce(self):
    # Provide an introduction and list of commands
        intro = """
        Welcome to my chatbot.
        Here are the commands this bot supports:
        !help: List of commands
        !weather <city>: Weather update
        !fact: Random fun fact
        !whoami: Your user information
        !join <channel>: join a channel
        !leave <channel>: leave a channel
        !send <channel> <message>: send a message to a channel
        !listen <channel> : listen to a channel
        !dm <to_user> <message>: send a message to a specific user
        !keys: list all the existing keys
        EXIT
        """
        print(intro)

    def identify(self):
    # add user interface to type in their names for identification
        username = input("Please enter your username: ")
        age = input("Please enter your age: ")
        gender = input("Please enter your gender: ")
        location = input("Please enter your location: ")
    # Store user details in Redis
        user_key = f"user:{username}"
        self.redis.hset(user_key, mapping={
            "username": username,
            "age": age,
            "gender": gender,
            "location": location
        })
        self.username = username
        print(f"Hello, {username}! You are now identified.")
        pass

    def join_channel(self, channel):
    # Join a channel
        self.pubsub.subscribe(channel)
        pass

    def leave_channel(self, channel):
    # Leave a channel
        self.pubsub.unsubscribe(channel)
        pass

    def send_message(self, channel, message):
    # Send a message to a channel
        self.redis.publish(channel, message)
        pass

    def read_message(self, channel):
    # Read messages from a channel
        pubsub = self.redis.pubsub()
        pubsub.subscribe(channel)
    # Format the output message
        for message in pubsub.listen():
            if message["type"] == "message":
                print(f"[{channel}] {message['data'].decode('utf-8')}")
        pass

    def process_commands(self):
    # Handle special chatbot commands
    # User interface to type in the command
        message = input("Enter a message:")
    # Exit option
        if message == "EXIT":
            return "Byebye!"
    # Return introduce again if the command is "!help"
        elif message.startswith("!help"):
            return self.introduce()
    # Extract the city in the input and return the weather of that city
        elif message.startswith("!weather "):
    # Make the characters in <city> all in lowercase
            city = message[9:].strip().lower()
            weather_info = self.redis.hget(self.weather_data_key, city)
            if weather_info:
                return weather_info.decode('utf-8')
            else:
                return f"No weather for {city} in the database."
    # Randomly select a fun fact in our database to return
        elif message.startswith("!fact"):
            random_fact = self.redis.srandmember(self.fun_facts_key)
            return random_fact.decode('utf-8')
    # Return the personal informaton of the user
        elif message.startswith("!whoami"):
            user_key = f"user:{self.username}"
            user_info_bytes = self.redis.hgetall(user_key)
            user_info = {key.decode('utf-8'): value.decode('utf-8') for key, value in user_info_bytes.items()}
            return user_info
    # Extract the channel name and join that channel
        elif message.startswith("!join "):
            channel = message[6:].strip()
            self.join_channel(channel)
    # Extract the channel name and leave that channel
        elif message.startswith("!leave "):
            channel = message[7:].strip()
            self.leave_channel(channel)
    # Separate command to "channel" and "message", and send to redis
        elif message.startswith("!send "):
            parts = message.split(' ', 2)
            channel = parts[1]
            message_text = parts[2]
            self.send_message(channel, message_text)
    # Extract the channel name and listen to that channel
        elif message.startswith("!listen "):
            channel = message[8:].strip()
            self.read_message(channel)
    # Separate command to "user" and "message", and send to redis
        elif message.startswith("!dm "):
            parts = message.split(' ', 2)
            to_user = parts[1]
            message_text = parts[2]
            self.direct_message(to_user, message_text)
        elif message.startswith("!keys"):
            return self.list_keys()
    # If the command is not in the list, still generate the response
        else:
            return "Unknown Command!"
        pass

    def direct_message(self, to_user, message):
    # Send a direct message to someone else
        message_obj = {
            "from" : self.username,
            "message" : message
        }
        self.redis.publish(to_user, json.dumps(message_obj))
        pass
        
    def list_keys(self):
    # Add an extra command to show all the existing keys in redis
        keys = self.redis.keys("*")
        keys_str = "\n".join(key.decode('utf-8') for key in keys)
        return f"List of keys in Redis:\n{keys_str}"
        pass


if __name__ == "__main__":
# Main interaction loop here
    bot = Chatbot()
    bot.identify()
    bot.introduce()
# Continue asking for command inputs unless "EXIT"
    while True:
        result = bot.process_commands()
        print(result)
        if result == "Byebye!":
            break
    #result = bot.process_commands()
    #print(result)

        

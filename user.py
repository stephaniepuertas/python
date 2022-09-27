class User:
        def __init__(self, first_name, last_name, email, age,is_rewards_member=false,gold_card_points=0):
            self.first_name=first_name
            self.last_name= last_name
            self.email=email
            self.age= age

            # include as default attributes
            self.is_rewards_member= is_rewards_member
            self.gold_card_points= gold_card_points
            
# include these methods

# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.

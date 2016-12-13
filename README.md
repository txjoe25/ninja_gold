# Ninja Gold
This is a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. 
The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, 
your ninja can earn or LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display 
past activities of this ninja.

- They're two routes -- '/' and '/process_money' (reset can be another route if you implement this feature).
- Have /process_money determine how much gold the user should have.
- the forms are sent to "/process_money" and not any other URL.
- the activities are stored in the session. No need to store anything in the database. 

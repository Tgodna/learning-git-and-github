import random

player = str(input("Enter your name: "));
print("Welcome to the game of Rock, Paper, Scissors, " + player + "!" ); 
print("You will be playing against the computer. The rules are simple: ");
print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.");
print("You will be using emojis to represent your choice: ");
print("Rock: ✊, Paper: ✋, Scissors: ✌️");
rock = "✊";
paper = "✋";
scissor = "✌️";
emoji_options = ["✊", "✋", "✌️"];
player_choice = input("Enter your choice: ");
computer = random.choice(emoji_options);
if player_choice == computer:
    print("player: " + player_choice)
    print("computer: " + computer)
    print("It's a tie!")
elif player_choice == "✊" and computer == "✌️":
    print("player: " + player_choice);
    print("computer: " + computer);
    print("✊  breaks ✌️! You win!");
elif player_choice == "✊" and computer == "✋":
    print("player: " + player_choice);
    print("computer: " + computer);
    print("✋  covers ✊! You lose!");
elif player_choice == "✋" and computer == "✊":
    print("player: " + player_choice);
    print("computer: " + computer);
    print("✋  covers ✊! You win!");
else:
    print("player: " + player_choice);
    print("computer: " + computer);
    print("✌️  cuts ✋! You lose!");



red="\033[1;31m"
green="\033[1;32m"
function termux(){ 
  if [ "$(command -v python3)" ];then 
    echo -e $red "install python...!" 
    pkg install python
  else 
    echo -e $green"python installed :)"
  fi 
  sleep 1
  if [ "$(command -v requests)" ];then 
    echo -e $red "install requests...!" 
    pip install requests 
  else 
    echo -e $green"requests installed :)"
  fi 
  sleep 1
  if [ "$(command -v pyTelegramBotAPI)" ];then 
    echo -e $red "install telebot...!" 
    pip install pyTelegramBotAPI
  else 
    echo -e $green"pyTelegramBotAPI installed :)"
  fi
  sleep 1 
  if [ "$(command -v rich)" ];then 
    echo -e $red"install rich...!"
    pip install rich 
  else 
    echo -e $green"rich installed :)"
  fi 
}

function linux(){ 
  if [ "$(command -v python3)" ];then 
     echo -e $red "install python...!" 
     apt-get install python3
  else 
      echo -e $green "python installed :)"
  fi 
  sleep 1 
  if [ "$(command -v requests)" ];then 
    echo -e $red "install requests..." 
    pip install requests 
  else 
    echo -e $green "requests installed:)"
  fi 
  sleep 1 
  if [ "$(command -v pyTelegramBotAPI)" ];then 
    echo -e $red "install telebot" 
    pip install pyTelegramBotAPI 
  else 
    echo -e $green "pyTelegramBotAPI installed :)"
  fi
  sleep 1 

  if [ "$(command -v rich)" ];then 
    echo -e $red"install rich...!"
    pip install rich 
  else 
    echo -e $green "rich installed :)"
  fi 
}
echo -e $red """
# #    #  ####  #####   ##   #      #
# ##   # #        #    #  #  #      #
# # #  #  ####    #   #    # #      #
# #  # #      #   #   ###### #      #
# #   ## #    #   #   #    # #      #
# #    #  ####    #   #    # ###### ######
"""
echo -e $green """
y) install termux 
n) install linux 
""";read -p "--->" n10 
if [ "$n10" == "y" ];then 
  termux
elif [ "$n10" == "n" ];then 
  linux 
else 
  echo -e $red "invalid option system not found"
fi 


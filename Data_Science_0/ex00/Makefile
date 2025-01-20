# COLORS #

#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37

RED = @echo "\033[0;31m"
ORANGE = @echo "\033[0;33m"
GRAY = @echo "\033[0;37m"
BLACK = @echo "\033[0;30m"
YELLOW = @echo "\033[1;33m"
GREEN = @echo "\033[0;32m"
BLUE = @echo "\033[0;34m" 
PURPLE = @echo "\033[0;35m"
CYAN = @echo "\033[0;36m"
RESET = "\033[1;0m"

LIGHT_GRAY = @echo "\033[1;37m"
LIGHT_GREEN = @echo "\033[1;32m"
LIGHT_CYAN = @echo "\033[1;36m"
LIGHT_PURPLE = @echo "\033[1;35m"

all:
	docker-compose -f ./docker-compose.yml up --build

re: fclean all

fclean:
	docker-compose -f ./docker-compose.yml down --rmi all -v --remove-orphans


MAIN = src/main.py

MAIN_TEST = tests/main.py

NAME_TEST = unit_test

NAME = 301dannon

all: $(NAME)

$(NAME):
	cp $(MAIN) ./$(NAME)
	chmod +x $(NAME)

tests_run:
	cp $(MAIN_TEST) ./$(NAME_TEST)
	chmod +x $(NAME_TEST)
	coverage run --branch $(NAME_TEST)
	coverage report -m 

fclean:
	rm -f $(NAME)
	rm -f $(NAME_TEST)
	rm -f .coverage

re: fclean all

.PHONY: all fclean re
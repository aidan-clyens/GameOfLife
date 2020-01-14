from conway.game import Game


def main():
    game = Game([800, 600], 30)
    game.run()
    game.quit()


if __name__ == '__main__':
    main()

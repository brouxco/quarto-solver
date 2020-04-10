# quarto-solver

quarto-solver is a python program made to win every game of Quarto!

## Installation

Clone the project.

```bash
git clone https://github.com/brouxco/quarto-solver.git
```

## Features

- Play a game of Quarto.
- Suggest what piece you should give to your opponent.
- Suggest where to put the piece you were given.

## Usage

```bash
python3 quarto.py --help
usage: quarto.py [-h] [-b BOARD] [-p PIECE] [-i] [-spi] [-spo]

optional arguments:
  -h, --help            show this help message and exit
  -b BOARD, --board BOARD
                        The board state
  -p PIECE, --piece PIECE
                        The piece you were given
  -i, --interactive     Play your game and interact with the solver
  -spi, --solve-piece   Suggest a piece to give to the opponent
  -spo, --solve-position
                        Suggest where to put the piece you were given

```

## Tests

TODO: test the solver against a random player.

## Contributing

Pull requests are welcome.

## License

[ISC](LICENSE)

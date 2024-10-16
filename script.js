let board = ['', '', '', '', '', '', '', '', ''];
let currentPlayer = 'X';
let isGameActive = true;
let messageElement = document.querySelector('.message');

const handleCellClick = (index) => {
    if (board[index] !== '' || !isGameActive) {
        return;
    }

    board[index] = currentPlayer;
    renderBoard();
    checkForWinner();
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
};

const renderBoard = () => {
    const cells = document.querySelectorAll('.cell');
    cells.forEach((cell, index) => {
        cell.textContent = board[index];
    });
};

updateMessage(); // Вызов функции, чтобы обновить сообщение

const checkForWinner = () => {
    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    for (let condition of winningConditions) {
        const [a, b, c] = condition;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            isGameActive = false;
            messageElement.textContent = `${board[a]} выиграл!`;
            return;
        }
    }

    if (!board.includes('')) {
        isGameActive = false;
        messageElement.textContent = 'Ничья!';
    }
};

// Привязка событий к ячейкам
const cells = document.querySelectorAll('.cell');
cells.forEach((cell, index) => {
    cell.addEventListener('click', () => handleCellClick(index));
});

// Сброс игры
const resetGame = () => {
    board = ['', '', '', '', '', '', '', '', ''];
    currentPlayer = 'X';
    isGameActive = true;
    messageElement.textContent = '';
    renderBoard();
};

// Кнопка сброса
const resetButton = document.createElement('button');
resetButton.textContent = 'Сбросить игру';
resetButton.addEventListener('click', resetGame);
document.body.appendChild(resetButton);

// Инициализация
renderBoard();

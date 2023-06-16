<!DOCTYPE html>
<html>
<head>
    <title>Small Online Games</title>
    <style>
        canvas {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="400"></canvas>    
    <button id="startButton">Start Game</button>
    <button id="restartButton" disabled>Restart</button>
    <p><canvas id="canvas" width="300" height="300" style="background-color:#333"></canvas></p>

    <script>
        // Get the canvas element
        const canvas = document.getElementById('gameCanvas');
        const context = canvas.getContext('2d');

        // Set up the game state
        let characterX = 20;
        let characterY = 190;
        let score = 0;
        let isGameOver = false;

        // Set up the game objects
        const character = { x: characterX, y: characterY, width: 20, height: 20 };
        const coins = [
            { x: 50, y: 50, width: 10, height: 10 },
            { x: 70, y: 150, width: 10, height: 10 },
            { x: 250, y: 300, width: 10, height: 10 },
            { x: 20, y: 290, width: 10, height: 10 },
            { x: 100, y: 80, width: 10, height: 10 },
            { x: 200, y: 230, width: 10, height: 10 },
            { x: 150, y: 290, width: 10, height: 10 },
            { x: 300, y: 330, width: 10, height: 10 }
        ];
        const enemies = [
            { x: 150, y: 150, width: 15, height: 15, speedX: 2, speedY: 2 },
            { x: 350, y: 50, width: 15, height: 15, speedX: 3, speedY: 1.5 },
            { x: 250, y: 250, width: 15, height: 15, speedX: -3, speedY: -3 }
        ];

        // Add event listener for mouse move
        canvas.addEventListener('mousemove', handleMouseMove);

        // Add event listener for start button
        const startButton = document.getElementById('startButton');
        startButton.addEventListener('click', startGame);

        // Add event listener for restart button
        const restartButton = document.getElementById('restartButton');
        restartButton.addEventListener('click', restartGame);

        // Function to handle mouse move events
        function handleMouseMove(event) {
            const rect = canvas.getBoundingClientRect();
            characterX = event.clientX - rect.left;
            characterY = event.clientY - rect.top;
        }

        // Function to update the game state
        function updateGameState() {
            // Update character position
            character.x = characterX;
            character.y = characterY;

            // Check for collisions with coins
            coins.forEach(coin => {
                if (detectCollision(character, coin)) {
                    score++;
                    coin.x = -10;
                    coin.y = -10;
                }
            });

            // Check for collisions with enemies
            enemies.forEach(enemy => {
                if (detectCollision(character, enemy)) {
                    isGameOver = true;
                    restartButton.disabled = false;
                }

                // Update enemy position
                enemy.x += enemy.speedX;
                enemy.y += enemy.speedY;

                // Reverse direction if enemy hits the canvas boundaries
                if (enemy.x <= 0 || enemy.x + enemy.width >= canvas.width) {
                    enemy.speedX *= -1;
                }
                if (enemy.y <= 0 || enemy.y + enemy.height >= canvas.height) {
                    enemy.speedY *= -1;
                }
            });
        }

        // Function to check for collision between two objects
        function detectCollision(obj1, obj2) {
            return (
                obj1.x < obj2.x + obj2.width &&
                obj1.x + obj1.width > obj2.x &&
                obj1.y < obj2.y + obj2.height &&
                obj1.y + obj1.height > obj2.y
            );
        }

        // Function to draw the game objects
        function drawGame() {
            // Clear the canvas
            context.clearRect(0, 0, canvas.width, canvas.height);

            // Draw character
            context.fillStyle = 'blue';
            context.fillRect(character.x, character.y, character.width, character.height);

            // Draw coins
            context.fillStyle = 'yellow';
            coins.forEach(coin => {
                context.fillRect(coin.x, coin.y, coin.width, coin.height);
            });

            // Draw enemies
            context.fillStyle = 'red';
            enemies.forEach(enemy => {
                context.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
            });

            // Draw score
            context.fillStyle = 'black';
            context.font = '20px Arial';
            context.fillText('Score: ' + score, 10, 30);

            // Draw game over message if the game is over
            if (isGameOver) {
                context.fillStyle = 'black';
                context.font = '30px Arial';
                context.fillText('Game Over!', canvas.width / 2 - 80, canvas.height / 2);
            }
        }

        // Function to start the game
        function startGame() {
            startButton.disabled = true;
            restartButton.disabled = true;
            characterX = 20;
            characterY = 200;
            score = 0;
            isGameOver = false;
            coins.forEach(coin => {
                coin.x = Math.random() * (canvas.width - coin.width);
                coin.y = Math.random() * (canvas.height - coin.height);
            });
        }

        // Function to restart the game
        function restartGame() {
            startGame();
        }

        // Game loop
        function gameLoop() {
            if (!isGameOver) {
                updateGameState();
                drawGame();
            }
        }

        // Start the game loop
        setInterval(gameLoop, 20);
       

    </script>
</body>
</html>

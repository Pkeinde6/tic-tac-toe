<script setup>
import { ref, computed } from 'vue'

const board = ref(Array(9).fill(null))
const isXNext = ref(true)

const calculateWinner = (squares) => {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ]
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i]
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a]
    }
  }
  return null
}

const winner = computed(() => calculateWinner(board.value))
const isBoardFull = computed(() => board.value.every(square => square !== null))
const currentPlayer = computed(() => isXNext.value ? 'X' : 'O')
const gameOver = computed(() => winner.value !== null || isBoardFull.value)
const status = computed(() => {
  if (winner.value) {
    return `Gagnant: ${winner.value}`
  } else if (isBoardFull.value) {
    return "Égalité!"
  } else {
    return `Tour du joueur: ${currentPlayer.value}`
  }
})

const handleClick = (index) => {
  if (board.value[index] || winner.value) {
    return
  }
  const newBoard = [...board.value]
  newBoard[index] = currentPlayer.value
  board.value = newBoard
  isXNext.value = !isXNext.value
}

const resetGame = () => {
  board.value = Array(9).fill(null)
  isXNext.value = true
}
</script>

<template>
  <div class="game-container">
    <h1>Tic Tac Toe</h1>
    <div class="game-status">{{ status }}</div>
    <div class="game-board">
      <button
        v-for="(square, index) in board"
        :key="index"
        :class="['square', { 'x': square === 'X', 'o': square === 'O' }]"
        @click="handleClick(index)"
        :disabled="gameOver"
      >
        {{ square }}
      </button>
    </div>
    <button class="reset-btn" @click="resetGame">Nouveau Jeu</button>
  </div>
</template>

<style scoped>
.game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 20px;
}

h1 {
  color: white;
  font-size: 3em;
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.game-status {
  color: white;
  font-size: 1.5em;
  margin-bottom: 30px;
  font-weight: bold;
}

.game-board {
  display: grid;
  grid-template-columns: repeat(3, 100px);
  gap: 5px;
  background: rgba(0, 0, 0, 0.2);
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 30px;
}

.square {
  width: 100px;
  height: 100px;
  font-size: 2em;
  font-weight: bold;
  color: white;
  background: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.square:hover:not(:disabled) {
  background: #f0f0f0;
  transform: scale(1.05);
}

.square.x {
  color: #667eea;
}

.square.o {
  color: #764ba2;
}

.square:disabled {
  cursor: not-allowed;
}

.reset-btn {
  padding: 12px 30px;
  font-size: 1.1em;
  font-weight: bold;
  color: #667eea;
  background: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.reset-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.reset-btn:active {
  transform: translateY(0);
}
</style>

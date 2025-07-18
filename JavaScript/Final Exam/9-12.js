// All questions & Answers
const questions = [
    { question: "Столица Англии?", answer: "Лондон" },
    { question: "Столица Франции?", answer: "Париж" },
    { question: "Столица Испании?", answer: "Мадрид" }
];

let currentQuestion = 0;
let correctAnswers = 0;

function checkAnswer() {
    const userAnswer = document.getElementById('answerInput').value.trim();
    const correctAnswer = questions[currentQuestion].answer;
    const isCorrect = userAnswer.toLowerCase() === correctAnswer.toLowerCase();
    
    addResultToTable(questions[currentQuestion].question, userAnswer, isCorrect);
    
    if (isCorrect) {
        correctAnswers++;
    }
    
    currentQuestion++;
    if (currentQuestion < questions.length) {
        document.getElementById('question').textContent = questions[currentQuestion].question;
    } else {
        finishTest();
    }
    
    document.getElementById('answerInput').value = '';
}

function addResultToTable(question, answer, isCorrect) {
    const row = document.createElement('tr');
    row.className = isCorrect ? 'correct' : 'incorrect';
    
    row.innerHTML = `
        <td>${question}</td>
        <td>${answer}</td>
        <td>${isCorrect ? 'верно' : 'неверно'}</td>
    `;
    
    document.getElementById('resultsBody').appendChild(row);
}

function finishTest() {

    document.getElementById('answerInput').style.display = 'none';
    document.querySelector('button').style.display = 'none';
    document.getElementById('question').textContent = 'Тест завершен!';
    
    const grade = correctAnswers >= 3 ? 5 : correctAnswers >= 1 ? 4 : 3;
    
    const row = document.createElement('tr');
    row.innerHTML = `
        <td colspan="3" style="text-align: center; font-weight: bold;">Ваша оценка: ${grade}</td>
    `;
    document.getElementById('resultsBody').appendChild(row);
}
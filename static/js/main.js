document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('question-modal');
    const questionText = modal.querySelector('.question-text');
    const answerText = modal.querySelector('.answer-text');
    const showAnswerBtn = modal.querySelector('.show-answer');

    // Add click handlers to question cells
    const questionCells = document.querySelectorAll('.question-cell');
    questionCells.forEach(cell => {
        cell.addEventListener('click', function() {
            if (!this.classList.contains('answered')) {
                const question = this.dataset.question;
                const answer = this.dataset.answer;
                
                if (question && answer) {
                    showQuestion(question, answer, this);
                }
            }
        });
    });

    // Show question in modal
    function showQuestion(question, answer, cell) {
        questionText.textContent = question;
        answerText.textContent = answer;
        answerText.style.display = 'none';
        modal.style.display = 'block';
        
        // Mark the cell as answered when showing the question
        cell.classList.add('answered');
    }

    // Show answer button handler
    showAnswerBtn.addEventListener('click', function() {
        answerText.style.display = 'block';
    });

    // Close modal when clicking outside
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});

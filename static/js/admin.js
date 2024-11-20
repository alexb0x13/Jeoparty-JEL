document.addEventListener('DOMContentLoaded', () => {
    // Category Management
    const categoryForm = document.getElementById('category-form');
    if (categoryForm) {
        categoryForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const categoryName = document.getElementById('category-name').value;
            
            try {
                const response = await fetch('/api/categories', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ name: categoryName })
                });
                
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Failed to add category');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Failed to add category');
            }
        });
    }

    // Question Management
    const questionForm = document.getElementById('question-form');
    if (questionForm) {
        questionForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = {
                category_id: document.getElementById('category-select').value,
                value: document.getElementById('question-value').value,
                question_text: document.getElementById('question-text').value,
                answer_text: document.getElementById('answer-text').value
            };
            
            try {
                const response = await fetch('/api/questions', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });
                
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Failed to add question');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Failed to add question');
            }
        });
    }

    // Delete buttons
    document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            if (!confirm('Are you sure you want to delete this item?')) return;
            
            const id = btn.dataset.id;
            const type = btn.closest('.category-item') ? 'categories' : 'questions';
            
            try {
                const response = await fetch(`/api/${type}/${id}`, {
                    method: 'DELETE'
                });
                
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Failed to delete item');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Failed to delete item');
            }
        });
    });
});

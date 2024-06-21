document.getElementById('run-btn').addEventListener('click', async () => {
    const code = document.getElementById('code-input').value;

    try {
        const response = await fetch('http://127.0.0.1:5000/run_code', { // Đảm bảo địa chỉ này khớp với địa chỉ máy chủ Flask
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: code }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        document.getElementById('output-display').textContent = result.output;
    } catch (error) {
        document.getElementById('output-display').textContent = `Error: ${error.message}`;
    }
});



document.getElementById('reset-btn').addEventListener('click', () => {
    document.getElementById('code-input').value = '';
    document.getElementById('output-display').textContent = '';
    updateLineNumbers();
});


document.getElementById('state-vector-btn').addEventListener('click', () => {
    alert('State vector display is not implemented yet.');
});

document.getElementById('density-matrix-btn').addEventListener('click', () => {
    alert('Density matrix display is not implemented yet.');
});

document.getElementById('bloch-sphere-btn').addEventListener('click', () => {
    alert('Bloch sphere display is not implemented yet.');
});


function updateLineNumbers() {
    const codeInput = document.getElementById('code-input');
    const lineNumbers = document.getElementById('line-numbers');
    const lines = codeInput.value.split('\n').length;
    lineNumbers.innerHTML = '';
    for (let i = 1; i <= lines; i++) {
        const lineNumber = document.createElement('div');
        lineNumber.textContent = i;
        lineNumbers.appendChild(lineNumber);
    }
}

function syncScroll() {
    const codeInput = document.getElementById('code-input');
    const lineNumbers = document.getElementById('line-numbers');
    lineNumbers.scrollTop = codeInput.scrollTop;
}

// Initialize line numbers on page load
updateLineNumbers();

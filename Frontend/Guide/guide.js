document.addEventListener('DOMContentLoaded', () => {
  const selector = document.getElementById('Ex-nums');
  const contentDispla = document.getElementById('ex-code-input');
  
  selector.addEventListener('change', () => {
    const selectedOptio = selector.value;

    switch (selectedOptio) {
        case 'op1':
          contentDispla.textContent = `reset 2\nwrite 1\nnot 0\nmeasure `;
          break;
        case 'op2':
          contentDispla.textContent = `reset 2\nwrite 3\nphase 360 1\ncnot 1 0\nwrite 1\nmeasure`;
          break;
        case 'op3':
          contentDispla.textContent = `reset 5\nwrite 14\nhadamard 0\ncnot 3 0\ncnot 4 0\nchadamard 4 1\nchadamard 4 1\nreset 4\nmeasure`;
          break;
        case 'op4':
          contentDispla.textContent = `reset 4\nwrite 8\nrotatex 225 1\nwrite 4\nrotatex 180 3\nwrite 13\nphase 135 2\nmeasure`;
          break;
        case 'op5':
          contentDispla.textContent = `reset 2\nwrite 0\ncnot 1 0\nrotatey 360 0\nmeasure`;
          break;
        default:
          contentDispla.textContent = '';
    }
    contentDispla.classList.add('active');
});
// Trigger the change event on page load to display the content for the first option
selector.dispatchEvent(new Event('change'));
});

document.addEventListener('DOMContentLoaded', () => {
  const selector = document.getElementById('Ex-nums');
  const contentDisplay = document.getElementById('output-ex-display');
  const click = document.getElementById('run-ex-btn');
  
  selector.addEventListener('change', () => {
    const selectedOption = selector.value;

    switch (selectedOption) {
        case 'op1':
            contentDisplay.textContent ='';
            click.addEventListener('click', () => {
              contentDisplay.textContent = `State: 00,  Probability: 1.0\nState: 01,  Probability: 0.0\nState: 10,  Probability: 0.0\nState: 11,  Probability: 0.0`
              ;});
            break;
        case 'op2':
          contentDisplay.textContent ='';
          click.addEventListener('click', () => {
            contentDisplay.textContent = `State: 00, Probability: 0.0\nState: 01, Probability: 0.0\nState: 10, Probability: 0.0\nState: 11, Probability: 1.0`
            ;});
            break;
        case 'op3':
          contentDisplay.textContent ='';
          click.addEventListener('click', () => {
            contentDisplay.textContent = `State: 0000, Probability: 1.0\nState: 0001, Probability: 0.0\nState: 0010, Probability: 0.0\nState: 0011, Probability: 0.0\nState: 0100, Probability: 0.0\nState: 0101, Probability: 0.0\nState: 0110, Probability: 0.0\nState: 0111, Probability: 0.0\nState: 1000, Probability: 0.0\nState: 1001, Probability: 0.0\nState: 1010, Probability: 0.0\nState: 1011, Probability: 0.0\nState: 1100, Probability: 0.0\nState: 1101, Probability: 0.0\nState: 1110, Probability: 0.0\nState: 1111, Probability: 0.0`
            ;});
            break;
        case 'op4':
          contentDisplay.textContent ='';
          click.addEventListener('click', () => {
            contentDisplay.textContent = `State: 0000, Probability: 0.0\nState: 0001, Probability: 0.0\nState: 0010, Probability: 0.0\nState: 0011, Probability: 0.0\nState: 0100, Probability: 0.0\nState: 0101, Probability: 0.0\nState: 0110, Probability: 0.0\nState: 0111, Probability: 0.0\nState: 1000, Probability: 0.0\nState: 1001, Probability: 0.146\nState: 1010, Probability: 0.0\nState: 1011, Probability: 0.854\nState: 1100, Probability: 0.0\nState: 1101, Probability: 0.0\nState: 1110, Probability: 0.0\nState: 1111, Probability: 0.0
            `;});
            break;
        case 'op5':
          contentDisplay.textContent ='';
          click.addEventListener('click', () => {
            contentDisplay.textContent = `State: 00, Probability: 1.0\nState: 01, Probability: 0.0\nState: 10, Probability: 0.0\nState: 11, Probability: 0.0`
            ;});
            break;
        default:
            contentDisplay.textContent = '';
    }

    contentDisplay.classList.add('active');

});

// Trigger the change event on page load to display the content for the first option
selector.dispatchEvent(new Event('change'));
});


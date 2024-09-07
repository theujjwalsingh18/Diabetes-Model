const form = document.getElementById('data');
const popup = document.getElementById('popbox');
const resultText = document.getElementById('result');
let box = document.querySelectorAll('input');


form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData();
  formData.append('Pregnancies', document.getElementById('ip1').value);
  formData.append('Glucose', document.getElementById('ip2').value);
  formData.append('blood_pressure', document.getElementById('ip3').value);
  formData.append('skin_thickness', document.getElementById('ip4').value);
  formData.append('insulin', document.getElementById('ip5').value);
  formData.append('bmi', document.getElementById('ip6').value);
  formData.append('diabetes_pedigree_function', document.getElementById('ip7').value);
  formData.append('age', document.getElementById('ip8').value);
  console.log(formData);
  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(Object.fromEntries(formData))
    });
    const data = await response.json();
    console.log(data);
    resultText.textContent = data.result;
    popup.classList.add('openpopup');
    box.forEach(function(input) {
      input.disabled = true;
    });
  } catch (error) {
    console.log('Error:', error);
  }
});

function closePopup() {
  popup.classList.remove('openpopup');
  box.forEach(function(input){
    input.value = '';
    input.disabled = false;
  });
}
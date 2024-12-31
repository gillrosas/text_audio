    let textarea = document.querySelector('#textarea')
    let select = document.querySelector('#voices')
    let button = document.querySelector("#button")

    button.addEventListener('click', () =>{
        if(textarea.value.trim() !==""){
            let ut = new SpeechSynthesisUtterance(textarea.value);
            window.speechSynthesis.speak(ut);
        }

    });
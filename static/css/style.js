$(document).ready(function() {
    let i = 0, text;
    let text = "Prognosis Research";

    function typing() {
        if (i < text.length) {
            $('.landing-text').innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, 500)
        }
    }
    typing();
})